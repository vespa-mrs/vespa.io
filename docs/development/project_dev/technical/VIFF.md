# VIFF (*V*espa *I*nterchange *F*ile *F*ormat) Overview
This document gives an overview of VIFF, the Vespa interchange file format. 
Vespa apps allow you to export complex objects (like metabolites, experiments
and pulse projects) to a file that can reconstitute the exact same object
anywhere that Vespa is installed. In addition, Analysis uses VIFF as its native
file format.

VIFF is XML which makes it possible for 3rd parties (humans or computer
programs) to read and extract useful information from it. We have been careful
to avoid making it specific to Python, so the XML (including the data blobs) can be 
parsed with C, MATLAB, Perl, etc. 

In addition, VIFF offers a way to get 3rd party information into Vespa. (See 
[#ImportingNon-VespaData Importing Non-Vespa Data] below.)

This documentation covers the basic structure of VIFF and some of the less
obvious elements. It's written for Vespa programmers but is of value to
anyone who wants to read or write VIFF.

## Examples
The first time Vespa runs, it builds its database from VIFF files so a 
fresh Vespa install contains working VIFF file examples in the 
[browser:/trunk/common/resources common/resources directory]. 
[browser:/trunk/common/resources/metabolites.xml Metabolites.xml] is a
fairly simple file. 
[browser:/trunk/common/resources/experiments.xml Experiments.xml] is an 
example of objects (experiments) that contain exportable 
subobjects (metabolites and pulse sequences).
[browser:/trunk/common/resources/pulse_projects.xml Pulse_projects.xml] 
contains an example of how VIFF stores binary data.
 


## General Structure
The root element of each VIFF file is `vespa_export`. This constant is
defined as `Export.ROOT_ELEMENT_NAME` in 
[browser:/trunk/common/constants.py constants.py]. 

There's just a little root-level information. The main item of note is a
comment that's present for the benefit of anyone reading the XML but isn't
used otherwise. The root also contains a timestamp from when the file was
created.

The root's children are Vespa's exportable objects. (At present, these are
pulse projects, experiments, metabolites, pulse sequences and datasets.) 
There's no 
limit on the number of objects in a VIFF file nor is there a limit on the
type. For instance, it's perfectly OK to construct a VIFF file that contains
both pulse projects and metabolites as siblings (children of the root). Vespa
doesn't construct such files itself, but if presented with one it would be
happy to import the available objects.

This document doesn't cover the structure of the exportable objects 
themselves. In general they map pretty closely to the objects' classes which
in turn mirror the GUI. We hope the XML is self-explanatory in most cases.


## Id Attributes
High level objects (currently pulse projects, experiments, metabolites and
pulse projects) each have a [UUID](http://en.wikipedia.org/wiki/Uuid) in 
the `id` attribute. Vespa assigns a UUID to each object when it is created
and the id stays with the object for its entire life.

If Vespa attempts to import an object and finds that an object with the same
UUID is already present in the database, the object is not imported. 


## Integrity
Assigning UUIDs to objects is meant to guarantee that e.g. metabolite
`a1b9f07b-3665-4ce8-ba4a-5f454baf9681` will always be a specfic definition
of aspartate. However, nothing prevents a user from exporting that 
aspartate and hand-editing the XML to change aspartate's definition. 
Guarding against this sort of tampering is out of the scope of Vespa.


## Importing Non-Vespa Data
Although Vespa expects to find UUIDs on certain objects during an import (as
described above), it doesn't fail if they're not present. Instead, it simply
assigns the object a UUID before storing it in the database. This opens import
to the possibility of importing objects that Vespa didn't create. For
instance, suppose you have a spreadsheet describing 110 metabolites in detail
(including J coupling values, etc.) and you want those metabolites to appear
in Simulation. Rather than entering them by hand, you could write a small
program to massage the data from spreadsheet to VIFF, and then ask Vespa to
import the resulting file.


## Binary Data
Vespa sometimes stores arrays of binary data (e.g. a waveform) in VIFF files. 
(Note: the term "array" is meant in the general mathematical sense and doesn't
specifically refer to a Python list, `array` object nor a `numpy` array.)

Binary data in VIFF always has the attributes necessary to reconstitute it to its
original form. This consists of the data type, encoding method, and, in the
case of numpy arrays, shape information.

The data type is one of the numpy data type strings (e.g. "float64" and
"complex128" for Python floats and complex numbers) even if the data isn't
from a numpy array.

The encoding attribute explains the steps that turned the data from a list or
array into an XML-compatible string. In order to turn the convert the XML
string back into numeric data, reverse the encoding steps.

For instance, Vespa currently encodes numeric arrays with steps of "xdr zlib
base64". That means the data was made portable with
[XDR](http://en.wikipedia.org/wiki/External_Data_Representation), compressed
with `zlib`, and then [Base64](http://en.wikipedia.org/wiki/Base64) encoded. To
make it an array once again, reverse those steps. Start by using a Base64 decoder on the XML
string. The result will be `zlib`-compressed data. Decompress it, and then run
the result of the decompression through an XDR unpacker.

Vespa's [browser:trunk/common/util/xml_.py XML utility code] contains 
functions for converting arrays to XML and back again. 

Since XDR has no native representation for complex numbers, complex arrays
are converted into pairs of (real, imaginary) before being encoded for VIFF.

If a VIFF element has a `shape` attribute, that means it started life as 
a numpy array. The shape is written as a comma-separated list that makes it
easy to pass to the numpy array's `.reshape()` method.


## Timestamps

Timestamps in VIFF files are always in 
[combined ISO format](http://en.wikipedia.org/wiki/ISO_8601), 
e.g. `2010-04-30T15:14:56` as specified by the XML
standard. The seconds field is always present, and there's never time zone
information.

Timestamps are always in the local time of the machine that wrote them.
Using local time isn't ideal for files that are meant to be shared globally, 
but time zone information in Python isn't easy to deal 
with and we opted not to.


## Missing Fields
In general, our import code doesn't care if optional fields are present
and empty or simply not present. If it's not present, our code assigns
a default value. 

For instance, a blank comment can be represented as `<comment />` or 
simply not present at all.

It's not valid for mandatory fields to be missing; e.g. each metabolite 
element must contain at least one spin element.


## Version Attributes
Many elements contains a `version` attribute (e.g. `1.0.0`). This allows us to
change the XML that we write should we need to. 

For instance, suppose we add an element to experiments called "location" which
records in which castle the experiment was performed because we know from
watching Young Frankenstein that all scientists work in castles. Vespa,
however, still needs to be able to read older VIFF files that don't 
contain "location" elements. The `version` attribute makes this possible.
Vespa won't look for location elements in VIFF files that contain the
pre-location version number (e.g. "1.0.0") but will in all others (e.g. with
versions >= "1.0.1").

We have [XmlVersionNumbers an entire document dedicated to XML version numbers in VIFF].


## Booleans
Vespa follows the XML specification which states that, "An instance of 
a...boolean can have the following legal literals {true, false, 1, 0}." Vespa
always writes booleans as `true` or `false` for clarity, but accepts any
of the valid XML literals.


## Compression
Vespa gives the option of compressing the export files it creates. Compression
is done with the 
[gzip module in Python's standard library](http://docs.python.org/release/2.5/lib/module-gzip.html) 
and is compatible with the free, open
source gzip utility. Vespa encourages the user to name compressed files with
an extension of ".xml.gz" but that's not strictly necessary.

When importing a file, Vespa automatically detects whether or not the file is
compressed. Vespa examines the file contents; the filename makes no
difference.

In short, compression is transparent to the user and nearly transparent to the
app.


## Experiments Expressed in VIFF
Expressing experiments in VIFF is a bit complicated because they contain
exportable subelements of a pulse sequence and one or more metabolites. The
pulse sequence isn't difficult to deal with because there's at most one so its
XML nodes are simply included as a subtree of the experiment.

The metabolite definitions are children of the experiment, just as the pulse
sequence is. However, each metabolite is also referenced from one or more
(probably many more) simulations that are also part of the experiment.
Repeating the metabolite definitions inside the simulations would be (a) an
inefficient use of space and (b) redundant. Instead, simulations contain only
references (by UUID) to the metabolites. It is guaranteed that any metabolite
which is referred to by a simulation has its full definition in the
experiment.

