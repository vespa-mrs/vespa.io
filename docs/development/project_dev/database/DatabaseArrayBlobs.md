# Array BLOBs in the Database
Some of our arrays (e.g. the ppms, areas and phases arrays in the simulations
table) are stored as SQLite BLOBs. The BLOBs are written in a language-neutral
format, meaning that you can read them not only with Python, but with C, 
MATLAB,  Perl, etc. This document describes the format in which they're read and written.

In this context, "array" always means "numpy array". 


## Python Code
The Python code we use to convert numpy arrays to/from BLOBs are in 
[browser:trunk/common/util/db.py db.py]. Look for the functions
`_numpy_array_to_blob()` and `_blob_to_numpy_array()`. 


## The Raw Data
Each BLOB contains an array of unspecified length. We construct the BLOB with
the following algorithm:

  1. Flatten the array into a 1D list.
  2. Use [XDR](http://en.wikipedia.org/wiki/External_Data_Representation) to
  turn the array into an architecture- and language-neutral format.
  3. Call Python's `sqlite3.Binary()` method to make the XDR-ed data 
  palatable to SQLite.
  4. Insert the data.
  
The arrays are represented as 
[XDR variable-length arrays](http://tools.ietf.org/html/rfc4506#section-4.13).

## The Metadata
Observant readers will note that the description above makes no provision
for two important pieces of metadata that one would require to reconstruct
a numpy array from the BLOB. Those pieces of metadata are _shape_ and
_datatype_.

As of this writing, we don't explicitly store this information anywhere in the 
database because our current BLOBs don't need it. (Those BLOBs are the 
`ppms`, `areas` and `phases` columns of the `simulations` table.) Those
arrays are always 1D and have a datatype of Python `float` (equivalent to
`numpy.float64` or a `C double`). For 1D arrays, the shape is implied by the 
length which we know from XDR.

In the future, if we have more complicated arrays to store, we might have to
consider metadata storage. However, how we'll store it will be decided on a
case-by-case basis. 

For instance, if we have arrays that always have a shape of (1, 4, N) where N
is the only number that varies, then we still won't need to store shape
information in the database because it can be inferred from the length of the
array (which XDR provides) and the two fixed dimensions. On the other hand, if
we have an array where the shape varies with each row, for example (2, X, Y,
Z) then we'd need to add a shape column to the table.


## Complex Numbers
XDR doesn't understand complex numbers, so when writing complex numbers to
BLOBs we first split them into (real, imaginary) pairs.


