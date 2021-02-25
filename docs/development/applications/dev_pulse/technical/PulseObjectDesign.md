# Pulse Object and DB Design

## Object Design
The main object in the Pulse program is a PulseDesign.

A PulseDesign starts with the Basic information about the user and the project (name, creation date, etc).

In addition PulseDesigns also contains machine specifications, and a few "master parameters".

Finally, they contain a list of Transforms that describe the creation of the pulse, and all the changes that it is put through. The complete set of available transforms can be seen in the Management->Manage Transform Kernels menu selection.

Each transform contains a set of input parameters - that is specific to the type of transform - and a set of results.

The result of each transform is a a Transform object that contains a TransformKernel object (input values and algorithm) and a RfResult object that contains an RF Waveform, a (optional) Gradient and a time axis array.

This is the general format for the program, and the best way to see the details is look at code (at least at this point).



## DB Design
The database was designed using the tool at this website:

http://ondras.zarovi.cz/sql/demo/

One can load in a file called erd.xml (currently located in vespa/common/resources) into this website and view the current state of the database.
