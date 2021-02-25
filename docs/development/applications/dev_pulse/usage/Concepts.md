# Pulse Concepts
This is a combination of logical concepts and rules that determine
how Pulse works. These rules are enforced through the application interface and,
to some extent, the database.

The main objects in the system are pulse designs. Designs contain
transforms and each transform eventually contains a result.
Here's how they're related --

 * Each design has some simple metadata (name, comments, machine 
 specifications, etc.).
 
 * Each design has zero to many transforms. A brand new design has zero
 transforms. Until some transforms are added, a design isn't very
 meaningful. Typically, a pulse design has two or more transforms.

 * A transform consists of the transform's parameters(e.g.
 bandwidth, number of points, dwell time, etc.) and an output result from the 
 transform's algorithm (a waveform, time axis and (optional( gradient).

 * Transforms are organized (visually and conceptually) in a list that
 flows left to right. The output (result) of a transform is the
 input for its right-hand neighbor.
 
 * Changing a transform implies a recalculation for all of the
 transforms downstream (to the right).
 
 * Transforms can be classified into two categories: create transforms
 and modify transforms.
 
 * The first transform of every design must be a create transform. A design 
 can have only one create tranformation. All subsequent transforms must be 
 modify transforms.
 
 * Changes to the "hard" properties of a pulse designs (a.k.a. "master
 specifications", see below) implies a change to all of its transforms. 
 By "hard"  properties we mean the properties that describe the science/hardware, 
 like bandwidth type and field strength. These are in contrast to "soft" 
 properties like the design name and comments.


We anticipate that users will want to share data with each other via Pulse's 
export and import functions. For this reason, pulse designs have 
[universally unique ids (UUIDs)](http://en.wikipedia.org/wiki/Uuid) rather 
than just ordinary integer ids.

## Pulse Projects
 * A design's "master specifications" describe some global variables that 
 apply for the design of theRF pulse. At present, they are the calculation 
 resolution and the pulse bandwidth convention (e.g. full width at half height).

 * Pulse assigns each design a UUID when it's created and the UUID remains
 the same for the life of the object.
 
 * Pulse also sets the _created_ timestamp when the object is created.
 That doesn't change either.
 
 * A design's name must be unique.
 
 * As of this writing, valid characters in a name are dash, dot (period), 
 slash, space and alphanumeric characters plus underscore (as enumerated 
 by the regex \w; 
 see Python re module docs). This rule is goverened by the regular expression
 `NAME_REGEX` in `constants.py`.
 
 * A design may be _cloned_. Cloning an design makes a copy of
 it with a brand new UUID. It's as if you clicked the "new" button and typed
 in fresh data yourself.
 If you've read the section on States (below), you'll understand
 when I say that since the result of a cloning is new, it's also private 
 and not in use (and therefore not frozen).
 
 * Pulse designs can be saved at any time. Saving a design will overwrite 
 the results currently in the database for that design.
 


## Transforms
Transforms create and modify the pulse. Users can use the Tranform Kernel 
Editor dialog to create new transforms with their own algorithms.


### Create Transforms
The first transform in every pulse design must be a create 
transform. It doesn't make sense to have multiple create transforms
in the same design.


### Modify Transforms
Every transform after the create transform must be a modify
transform. Users can add as many of these as they like.

At present, our GUI only permits appending transforms. It's conceptually
(and programatically) possible and perhaps desirable to allow transforms
to be inserted before existing general transforms instead of just 
appending; however, to effect an 'insert' of a transform at this time, a 
user would have to delete transforms from the end of the list up to the 
point of insertion and subsequently append those transforms afterwards.


## States Within RF Pulse

### Private and Public (Pulse Projects)
All designs start life _private_. That means they're only in 
your database; no one else has seen them.

Once exported, designs become _public_. That means that their definition
has been shared with the world. Public objects are _frozen_ (see below).

Once a private design has become public, it can never become private again.
Cloning, however, will create a new, private design with exactly the
same properties (but a different UUID).

### Frozen (Pulse Projects)
_Frozen_ objects are mostly uneditable -- only the name and comments can
be changed. Public objects are frozen because once you've shared a design with 
others (or you've imported a design that they've shared with you),
you need to be able to trust that you're talking about exactly the same 
object.


Note that _frozen_ only refers to whether or not the fundamental 
attributes of the object can be edited. It doesn't affect whether or not
it can be deleted. 


