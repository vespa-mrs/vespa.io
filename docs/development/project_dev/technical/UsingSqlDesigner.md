We make all of our changes to the database structure with a tool called
[WWW SQL Designer](http://ondras.zarovi.cz/sql/demo/), so this document is 
dedicated to explaining that tool and how we use it.

# About WWW SQL Designer
WWW SQL Designer is a BSD-licensed, browser-based 
tool by Ondrej Zara that offers a graphical 
interface for database design without trying to do too much. It displays
a database as an 
[entity relationship diagram](http://en.wikipedia.org/wiki/Entity-relationship_model), 
or ERD for short. WWW SQL 
Designer can generate SQL from an ERD, and that's how we use it.


## What It Is and What It Isn't
*What It Is*: Handy.

*What It Isn't*: Necessary. We use it as a convenience. You can always
go back to hand-editing your `.sql` files. (See 
[#LifeWithoutWWWSQLDesigner Life Without WWW SQL Designer],
below.) _However_, note that you can't
mix use of WWW SQL Designer with hand editing of `.sql` files. 

The reason is that WWW SQL Designer saves the ERD in an XML
file. If you edit the SQL directly to create v1.0.1 of that file but the XML
file is still at v1.0.0, then the next time you load that file into SQL
Designer and generate SQL, the SQL will regress to v1.0.0. The changes you
made to produce v1.0.1 of the SQL will be lost.

WWW SQL Designer is similar to wxGlade in this respect. wxGlade generates a
.py file that we store in our auto_gui directory, while wxGlade saves its work
in a .wxg file (which happens to be XML). One can directly edit the .py file
in auto_gui, but doing so makes it out of sync with the .wxg file.

## Using WWW SQL Designer
WWW SQL Designer features a cheap but effective way to save and re-open the
ERD and SQL it generates -- copy & paste. The moving parts of WWW SQL Designer
are written in Javascript and I think it's rather difficult for Javascript to
read & write arbitrary files from/to your hard disk. WWW SQL Designer steps
around the problem by putting what you need in a textbox and letting you copy
& paste to/from files that you've saved.

### Opening Vespa's ERD
1. Open WWW SQL Designer in your Web browser.
1. Open `common/resources/erd.xml` in your favorite editor and copy its   
 entire contents to the clipboard.
1. Click the Save/Load button at the top of WWW SQL Designer's tool menu thingy
 on the right.
1. Paste into WWW SQL Designer's Input/Output textbox.
1. Click the "Load" button. WWW SQL Designer will display a graphical layout
 of Vespa's tables.

### Saving Changes
If you've made some changes and want to save your work, here's what to do.

1. Click the Save/Load button at the top of SQL Designer's tool menu thingy
   on the right.
1. Click the "Save XML" button. WWW SQL Designer will populate the Input/Output 
   textbox with XML that describes the ERD.
1. Copy the contents of the textbox to the clipboard.
1. Open `common/resources/erd.xml` in your favorite editor.
1. Paste into `erd.xml` and save it.
1. In WWW SQL Designer, click "Generate SQL (SQLite)". SQL Designer will populate
   the Input/Output textbox with SQL that matches the ERD.
1. Open `common/resources/create_tables.sql` in your favorite editor.
1. Paste into `create_tables.sql` and save it.


## WWW SQL Designer and Our Custom Types
SQLite is an odd database in that it allows one to define columns that have datatypes
of which SQLite knows nothing, like TIMESTAMP, BOOLEAN or BANANAS. The first
two are particularly useful. Python's `sqlite3` module (which we use) 
automatically converts the data in TIMESTAMP columns to `DateTime` objects.
Similarly, our `db.py` code has two small functions that translate BOOLEAN
column data into Python's `True` or `False`. *Vespa relies on this behavior.*

Vespa assumes that these columns will be translated into the appropriate 
objects, therefore it's important
to declare these columns with the appropriate types. By default, 
WWW SQL Designer doesn't know about TIMESTAMP and BOOLEAN columns, but it's
easy to add custom types.

### Adding Custom Types
WWW SQL Designer saves datatype information in the XML file it generates, so
if you paste our `erd.xml` into WWW SQL Designer, it will automatically know
about TIMESTAMP and BOOLEAN.

Suppose you want to add the custom type BANANAS. All you'd have to do is 
open `erd.xml` in a text editor and add the following line below all of 
the other `<type>` elements.

```
<type label="Bananas" default="" length="0" sql="BANANAS" quote="'" color="yellow" />
```


## Life Without WWW SQL Designer

Above I mentioned how 
WWW SQL Designer is similar to wxGlade in the way it affects what files one
can and cannot hand edit. Well, they're dissimilar in that building GUIs
like Vespa's by hand (without wxGlade) is pretty intimidating, but 
designing and edit a database without a GUI tool like WWW SQL Designer is 
not a big deal. 

So If you don't want to use this tool at some point, that's 
fine. You can edit Vespa's `.sql` files in a text editor. Just don't go back 
to using WWW SQL Designer without rebuilding your ERD from scratch!



