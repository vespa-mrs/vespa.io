# Simulation Concepts
This is a combination of logical concepts and limitations that determine
how Simulation works. These rules are enforced through the application and,
to some extent, the database.

The main objects in the system are experiments, simulations, spectra, pulse 
sequences and metabolites. Experiments are the primary objects; everything 
else is secondary. Here's how they're related --

 * Each experiment has zero to many simulations. Simulations are the whole
 point of an experiment, and there's not much to an experiment besides the
 metadata that defines the simulations. Since entering the experiment metadata
 is pretty trivial, we don't let users save experiments that define zero simulations. 
 Experiments with zero simulations can exist, but only in memory.
 They are never saved to the database or an export file.

 * Each experiment makes use of and refers to exactly one pulse sequence, but 
 the experiment may 
 define one or more timing sets for the pulse sequence.

 * Each simulation creates one spectrum.

 * Each spectrum has zero or more lines. Zero is an unusual case, but possible.

 * Each spectrum line has a one PPM, area and phase value in it.

We expect users to share data via Simulation's export and import functions.
For this reason, several of Simulation's objects (experiments, pulse sequences
and metabolites) have 
[universally unique ids (UUIDs)](http://en.wikipedia.org/wiki/Uuid) rather 
than just ordinary integer ids.

## The "Big Three"
Experiments, metabolites and pulse sequences have a number of things in 
common. 

 * Simulation assigns each object a UUID when it's created and the UUID remains
 the same for the life of the object.
 * Simulation also sets the _created_ timestamp when the object is created.
 That doesn't change either.
 * Their names must be unique among their kin. In other words, metabolite 
 names must be unique among metabolites, experiment names must be unique
 among experiments, etc. It's OK (although perhaps a little strange), if 
 for example a metabolite has the same name as a pulse sequence.
 * As of this writing, valid characters in a name are dash, dot (period), 
 slash, space and alphanumeric characters plus underscore (as enumerated 
 by the regex \w; 
 see Python re module docs). This rule is goverened by the regular expression
 `NAME_REGEX` in `constants.py`.
 * Metabolites and pulse sequences used in (i.e. referred by) an existing 
 experiment may not be deleted. See States (below).
 * All of these objects may be _cloned_. Cloning an object makes a copy of
 it with a brand new UUID. It's as if you clicked the "new" button and typed
 in fresh data yourself.
 If you've read the section on States (below), you'll understand
 when I say that since the result of a cloning is new, it's also private 
 and not in use (and therefore not frozen).
 
 


## Experiments
Experiments are the main focus of the Simulation application. An experiment's 
_raison d'etre_ is to run a set of simulations. This set of simulations
is the experiment's _results space_. 

Currently, that space is defined by two to four nested loops. The first loop 
covers the list of metabolites the user has involved in the experiment. The
other one, two or three loops are user-defined lists of numbers. 

The attachment `results_space.png` is a visual representation of a 3D
results space (one set of metabolites and two lists of user-defined numbers).

Simulations themselves know nothing about one another and are agnostic to the
order in which they're run. Thus, while the existing code is geared towards
generating a very regular results space that we iterate over in a very
straightforward order, more complex result spaces and iteration orders are
possible. The sky's the limit, really, provided you can dream up a GUI that
allows users to describe the results space.

There's more about the results space in the section on simulations. 

 * Once an experiment has been saved, the following attributes become 
   read-only: pulse sequence, investigator, user parameters, b0, isotope, 
   peak_search_ppm_low, peak_search_ppm_high, blend_tolerance_ppm, 
   blend_tolerance_phase. 

 * One can associate additional metabolites with an experiment, but 
   once it is associated and the experiment is saved, the metabolite remains 
   with the experiment forever. In other words, a metabolite can't be removed 
   from a saved experiment.
   
 * An experiment's b0 value is always stored in megahertz.
 


## Pulse Sequences
 * A loop without a label name will be treated as a "non-loop". That is, the 
   loop control will not show up in the Visualization widget. All loops used 
   in a pulse sequence must have a label.

 * A user defined parameter must have a name and default value listed. The 
  default values should be such that the pulse sequence will run with only 
  default values being used, but Simulation will not check for this, only 
  suggest it be so in the documentation.

 * The pulse sequence sequence_code field cannot be empty. Simulation is
 not responsible for checking to see that the code is syntactically correct,
 working PyGamma code (although that would be nice).

 * The pulse sequence binning_code field is populated with default 
 binning code. The user can replace this with their own code if they wish to.
 Simulation is
 not responsible for checking to see that the code is syntactically correct,
 working PyGamma code (although that would be nice).


## Metabolites
The main fields of a metabolite are UUID and name. They also have one or 
more spins and zero or more J couplings. The number of J couplings will depend
on the number of spins, but may contain all zeros depending on the underlying
physics.

 

## Spins and J Couplings
Spins are always associated with a specific metabolite. Their main 
attributes are isotope (e.g. 1H) and chemical shift (a float). 

A J Coupling describes the relationship between two spins. It has a float 
value (in Hertz) and the two spins to which it refers are always on the 
same metabolite. 

 * Each metabolite has one or more spins.
 
 * The order of the spins isn't important. For sanity's sake, we always 
   retain the order that the user provided.
 
 * Our app imposes a somewhat arbitrary limit of 14 spins per metabolite.
   As of this writing, the limit derives from only one place -- a constant
   in the metabolite editing dialog. In theory, one can change that constant
   and Simulation will take it in stride. 
 
 * Each metabolite has zero or more J couplings. There's one J coupling
   per unique combination of spins, which works out to be the `sum(n)` 
   where n == the number of spins. All couplings can be set to zero or any
   other float number.
   
 For instance, if there's three spins,
 there are three J couplings (1-2, 1-3, and 2-3). If there's, four spins,
 there's six J couplings (1-2, 1-3, 1-4, 2-3, 2-4 and 3-4). The following
 very long line of Python will list the spin count-J coupling relationship.
 
```
#!python
print "spins\tj-coups\n" + "\n".join(["%d\t%d" % (i, sum(range(i))) for i in range(1, 15)])
```
 
 That prints something very much like the table below.
   
 ||spins||J couplings||
 ||1||0||
 ||2||1||
 ||3||3||
 ||4||6||
 ||5||10||
 ||6||15||
 ||7||21||
 ||8||28||
 ||9||36||
 ||10||45||
 ||11||55||
 ||12||66||
 ||13||78||
 ||14||91||

## Isotopes
The isotopes associated with each spin are restricted to those on the 
following list (which is
reflected in the isotopes table in our database):
```
1.   
1.   
1.   
 6LI  
 7LI  
10B  
11B  
13C  
14N  
15N  
17O  
19F  
29SI 
31P  
```

Note that the list is not ordered alphabetically but by atomic mass.
   
## Simulations
In the context of this application, the word "simulation" has a specific 
meaning that clashes a little with the real world. 

Recall that an experiment runs a loop over two to four dimensions and that's
called the results space. In the real world, people are apt to call the entire 
results space a simulation but we're  calling it an experiment. In the context 
of this app, we use the term slightly differently: each point in the results 
space is one _simulation_.

 * Each simulation has a value for metabolite, dimension 1, dimension 2, and
 dimension 3.
 
 * Each combination of these values is unique within an experiment. 
 
 * Each simulation produces a spectrum as output.
 
See the attachment `results_space.png` for a visual representation of the 
simulations run by an experiment.
 
## Spectra
A spectrum is the output from a simulation. There's exactly one spectrum
produced by each simulation. Since an experiment comprises
a 3D block of simulations, then the output of an experiment is a 3D block of
spectra.

 * A spectrum is composed of a number of lines.
 
 * Each line has the values PPM, area and phase.

 * When visualized graphically, the PPM values represent the X axis and so
   we always sort lines by PPM.


## States Within Simulation
### Active and Deactivated (Metabolites)
Metabolites are _active_ by default. _Deactivating_ a metabolite reduces
clutter by taking it "out of service". Inactive metabolites don't 
show up in the list of available metabolites when creating a new experiment.
That's the only effect of active/inactive status.

You can change a metabolite from active to inactive and vice versa any time
you like.

### Private and Public (Experiments, Metabolites and Pulse Sequences)
All of these objects start life _private_. That means they're only in 
your database; no one else has seen them.

Once exported, objects become _public_. That means that their definition
has been shared with the world. Public objects are _frozen_ (see below).

Once a private object has become public, it can never become private again.
Cloning, however, will create a new, private object with exactly the
same properties (but a different UUID).

### In Use (Metabolites and Pulse Sequences)
When you select a metabolite or pulse sequence for use in an experiment, 
that experiment refers to the object for as long as the experiment exists in
your database. Metabolites and pulse sequences that are referred to by 
an experiment are _in use_ by that experiment.

Objects that are in use may not be deleted and are _frozen_ (see 
below).

There's no limit on the number of experiments that can refer to a given 
metabolites or pulse sequence.

Once all of the experiments referring to an object are deleted, the object
is no longer in use.

### Frozen (Experiments, Metabolites and Pulse Sequences)
_Frozen_ objects are mostly uneditable -- only the name and comments can
be changed. Objects are frozen for one of two reasons. 

*In use objects (metabolites and pulse sequences) are frozen* because 
they're referred to by an experiment,
and changing the underlying objects that the experiment uses would corrupt
the experiment.

*Public objects are frozen* because once you've shared an object with 
others (or you've imported an object that they've shared with you),
you need to be able to trust that you're talking about exactly the same 
object.

Here's a table summarizing when an object is frozen.

||*Private?*||*In Use?*||*Frozen?*||
||Yes||No||No||
||Yes||Yes||Yes||
||No (public)||No||Yes||
||No (public)||Yes||Yes||

The _in use_ concept doesn't apply to experiments, so for them only 
private/public matters but the connection to frozen is still the same.

Note that _frozen_ only refers to whether or not the fundamental 
attributes of the object can be edited. It doesn't affect whether or not
it can be deleted. 


