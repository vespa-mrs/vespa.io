# Deflate and Inflate
The classes of the "Big Three" Simulation objects (experiments, metabs and
pulse sequences) and their subobjects all implement methods called `deflate`
and `inflate`. This document explains the purpose of those methods and how
they work.

## Nomenclature
The names are from 
[the Wikipedia article on serialization](http://en.wikipedia.org/wiki/Serialization)
which describes what these functions are for. In short, `deflate` turns
reduces object to raw data in some other format (e.g. XML) while `inflate` 
reverses the process.

The names `serialize` and `deserialize` would probably have worked just as 
well or even better. When I chose `deflate/inflate` I had in mind that the
functions might do more than just convert the objects to/from a disk-friendly
format. That has not and probably will not happen, so the more standard terms
serialize and deserialize might be a better choice.

## Formats
The functions recognize two formats: Python dictionaries and XML stored in 
an ElementTree object (more on this below).
Both are used by `inflate` while `deflate` uses only the
ElementTree format.

### ElementTree Format
The default format is 
[a Python standard library ElementTree](http://docs.python.org/release/2.5/lib/module-xml.etree.ElementTree.html).
This is a very useful representation as it's dead easy to turn it into an 
XML file. The library even handles encoding issues, which is nice. Since
this is the default and also the format on which Simulation relies for all
of its exports and imports, considerable time & attention has been invested 
in the code.

### Dictionary Format
The other format supported by `inflate/deflate` is that of Python 
dictionaries. In practice, the delfate-to-dict path is unused (see below
for why); only `inflate` uses dicts. Dictionaries are passed 
to `inflate` when reconstituting an object from the database. 

Side note: The previous sentence is not strictly true, but is "true enough"
thanks to Python's duck typing. SQLite returns row objects to our database
code. SQLite's row objects are tuple-ish with one dict-like feature.
Specifically, the columns are accessible by column name.
We improved the dict-ishness of SQLite's default row object with our
`_BetterRow` class which is implemented in `db.py`. It's actually 
`_BetterRow` objects which get passed to `inflate`, but `_BetterRow` objects
are sufficiently dict-like that the `inflate` code can treat them as dicts.
One could also pass real dicts to `inflate`, and early versions of Simulation 
did just that but we don't do so anymore.

Here's a subtle but important point -- when inflating from a dict, 
`inflate` compares the dict
keys with the object's attribute names. When it finds a match, it assigns 
the value associated with the key to the attribute of the same name. Keys
that don't match any attribute names are ignored, and attributes that 
don't match any key names are left untouched. 

For example, suppose an Experiment object's `inflate` method is passed
this dict: 
```
{ 
    "name" : "Fred's Experiment", 
    "foo"  : 42 
}
```

Since Experiment objects have a "name" attribute and the dict has a key of
the same name, "Fred's Experiment" is assigned to `experiment.name`. The
experiment object's other attributes (`created`, `investigator`, etc.) are
unchanged because their names aren't represented in the dict keys. And the 
"foo" key is ignored because Experiment objects have no attribute called 
`foo`. 

As mentioned above, SQLite returns rows keyed by column names. In general, 
our database column names match our object attribute names, so the 
dict-like rows returned by SQLite can be passed directly to `inflate` 
without alteration. For instance, the SQL statement 
`SELECT name FROM experiments` will produce rows containing keys called 
"name". 

Occasionally this relationship falters. A good example is in the 
PulseSequenceParameter object which has an attribute called `default`. That's
fine for Python, but `default` is a reserved word in SQL so the corresponding 
column
is called `default_value`. In this case, the database code renames the key
from `default_value` to `default` before passing the dict to `inflate`


### Why We Don't Deflate to Dicts
Our code inflates and deflates using ElementTrees and inflates using dicts, 
so why doesn't it also deflate using dicts? What's with the inconsistency?

Just as deflating to an ElementTree happens when an object is about to 
be written to XML, the natural place for deflating to a dict would be when 
the object is about to be written to the database. We could do that, and it
would make the code more consistent. However, it wouldn't provide much
benefit.

Regardless of whether or not the database code is passed a dict or one of 
our custom Vespa objects, it still has to know a bit about the object in
order to represent it correctly in the database. In that light, it doesn't 
make much difference whether the data comes from a dict or a Vespa object.
And since the data is already in a Vespa object, deflating it into a dict
would just be an extra step that provides no benefit.
