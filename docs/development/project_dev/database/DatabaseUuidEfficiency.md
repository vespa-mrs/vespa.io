# Efficiency, UUIDs and SQLite
A [UUID](http://en.wikipedia.org/wiki/Universally_unique_identifier) can 
be represented in at least three ways: as a 32 or 36 character string using 
printable ASCII,
a 16 byte string (with each byte in the range 0x00 - 0xff, making the
string non-printable) or a 16 byte integer.

We store our UUIDs in the most readable format which is also the 
fattest -- as a 36 character string like 
`e8d1860e-0a09-41b89357-c3024e8394b2`. (It's the same UUID with or
without the four dashes which is why they can be represented as 32 or
36 character strings.)

This document examines the pros and cons of storing UUIDs this way
and examines alternatives.

If you like, you can jump straight to the [#Conclusion conclusion].

## Advantages and Disadvantages of the Current Scheme
The advantages of this scheme are simple. The UUID
strings are recognizable to some as UUIDs (to some) and easy to read
for everyone. They also match the strings we write to XML files.

The disadvantage is mainly that of space. It's my understanding that
SQLite is generally very good at not wasting space. Nevertheless,
a 36 character string is going to take at least 36 bytes to store.

However, for almost all of the tables in the current database, the
difference hardly matters. Most tables that contain
UUIDs will contain at most maybe 2000 rows (and often more like 200).
2000 * 36 = 72000, and 72000/1024 = 70 kilobytes of data. In other
words, peanuts.

However, the simulations and experiment_dims tables are likely to be large 
(tens of thousands of rows or more) and they contain one UUID each. That 
means there's 36 UUID bytes per row. Assuming one million rows, that's 34 
megabytes of UUIDs.

In terms of available disk space on the average computer, that's still
peanuts. But in terms of the amount of data that SQLite needs to read from
disk during a query, it's bad. The operating system reads from the disk in
blocks (4k is a common size) and the more rows that can fit in a block, the
more likely it is that a row will be cached in memory when SQLite requests it
from disk. Bigger rows mean fewer rows per block and fewer rows cached in
memory.

It would be nice to shrink our UUID storage. Is that possible?

## Shrinking UUIDs - INTEGERs and REALs
As mentioned above, a 36 character UUID can also be represented as a 128 bit
(16 byte) integer. Unfortunately, SQLite's INT type is 64 bit (8 bytes) and it
offers no facility for storing larger ints.

SQLite has a REAL type which is a 64 bit/8 byte IEEE float. It's 
possible to convert a 16 byte integer into an 8 byte float, but the
number doesn't survive the round trip due to floating point noise. 
Here's an example from a Python interpreter session:

```
#!python
>>> import uuid
>>> my_uuid = uuid.uuid4()
>>> my_uuid
UUID('379cdd33-f231-4122-b78d-7481557f13c1')
>>> my_uuid.int
73922024606215418702568719629565236161L
>>> # It's possible to recreate my_uuid from this int value
... 
>>> my_uuid == uuid.UUID(int=73922024606215418702568719629565236161L)
True
>>> # But I can't do so if the value passes through float() on the way
... 
>>> my_uuid == uuid.UUID(int=long(float(my_uuid.int)))
False
>>> # ...and we can see why...
... 
>>> uuid.UUID(int=long(float(my_uuid.int)))
UUID('379cdd33-f231-4200-0000-000000000000')
```

## Shrinking UUIDs - Double INTEGERs
A 128 bit integer can be represented as two 64 bit integers. This would
require two columns to represent each UUID, however. That could possibly be
made transparent on some level with clever use of VIEWs and possibly custom
functions, but this is too complicated for us.

## Shrinking UUIDs - BLOBs
A SQLite BLOB can store arbitrary data and can be indexed. By use of the
(undocumented!) `sqlite.Binary()` call, one can convert a UUID into a BLOB.
This works, but see the "Real World Testing" section below.


## Shrinking UUIDs - Shadow ids
Remember that the problem isn't so much the UUIDs on the unique objects
themselves, it's the table(s) that point to these objects. Instead of trying
to shrink UUIDs, an alternative is to give each object a second, more compact
unique identifier. A traditional AUTOINCREMENT INTEGER is an obvious choice.
This id would be randomly assigned by the database and would have nothing to
do with the UUID other than occupying the same row. In other words, it would
shadow the UUID, following it around but always subordinate to it.

Integers are very compact in SQLite. They use 1 to 9 bytes; as little 
space as necessary is allocated to represent the number. Most of
the ids we would use would fit into 2-4 bytes which is a lot smaller
than 36.

Another way to implement shadow ids is to create a table that maps UUIDs
to integer ids and vice versa. The UUID would still be the "public" id of the 
object, but it wouldn't appear in any tables except the mapper table.
Internally, the tables would use the integer ids. This is a bit nicer than
embedding the shadow ids directly in the tables alongside the UUID since
this solution doesn't violate normalization.

It would be possible to implement shadow ids for some tables and not
others. 

In any case, using shadow ids would require rewriting Vespa' SQL for all of 
the affected tables. The rewrite wouldn't be extensive, but it would 
touch most queries.


## Real World Testing
I compared our current UUID representation (36 byte strings) to a 16 byte
BLOB representation.

I generated one million (1m) UUIDs and wrote them to a text file. Next, I
created two SQLite databases, each with just one table with one primary key
column called `id`. The only difference is that in one database, `id` was
`CHAR` and in the other it was `BLOB`. I then inserted the 1m UUIDs into each
database.

The text database was 94M while the BLOB database was 51M. This averages out
to about 98 bytes/row for the text representation versus 53 bytes/row for the
BLOB representation. It's a significant difference.

I tested to see how this would affect select times. I read the 1m UUIDs from
the text file, converted them to UUID objects, and then used Python's
`random.choice()` to select a UUID and select it from the database. I repeated 
that loop 100,000 times. 

Results were inconclusive. According to Python's profiler (`cProfile`),
selecting from the BLOB database was about 8% faster. However, that's if we
only measure the `execute()` method.

The BLOB method was slower if we consider the time it takes to convert the
BLOB into the UUID string that we actually need. How much slower depends on
how the code is structured. When using text UUIDs, we never need to convert
them to or from strings. When using BLOBs, given a variable `uuid` that
contains a string, we have to call
`sqlite.Binary(uuid_module.UUID(uuid).bytes)` to convert a UUID for use in a
query and `str(uuid_module.UUID(bytes=result))` to convert the BLOB result
returned by the database to a UUID string. Those calls chew up a significant
amount of time.

I don't know how this would play out in the real world. Since the select
improvement when using BLOBs is < 10% and the increase is cancelled out 
by time spent in the `uuid` module, I don't think the real world change 
would be more then +/- 5%.

The sparsely-commented code that I used to run these tests is attached 
as `test.py`.


# Conclusion
Storing a more compact UUID representation in SQLite via Python might be
possible, but it isn't easy. More to the point, it's not worth the 
trouble for us.

If the size of UUIDs becomes too painful at some point, the best solution is
probably using some variant of the shadow ids described above.
