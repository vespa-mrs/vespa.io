# Summary
The interface between Simulation and your pulse sequence code changed in
version 0.1.2 of Vespa. The new interface is not compatible with the old one.
Your existing pulse sequence code won't run under the new interface without
some changes.

We're written [a practical guide to upgrading to 0.1.2](/wiki:UpgradingTo_0_1_2/).
This document explains the details behind the change, such as -- 


 * [#HowSimulationRunsaPulseSequence How Simulation Runs a Pulse Sequence]
 * [#WhyWeChangedtheInterface Why We Changed the Interface]
 * [#WhattheNewInterfaceLooksLike What the New Interface Looks Like]

## How Simulation Runs Your Pulse Sequence (A Brief Review)
Each pulse sequence consists of two pieces of code -- the sequence code and
the binning code. The sequence code is generally where we put PyGAMMA code
that describes the simulation and generates the results. The binning code can
subsequently be used to simplify these results (e.g. the combination of
degenerate lines - hence, the name 'binning'). The binning step is optional.

## Why We Changed the Interface
The interface in versions < 0.1.1 were based around Python's 
[`exec` statement](http://docs.python.org/release/2.6.6/reference/simple_stmts.html#the-exec-statement).
It executed pulse sequence code in the same context as Simulation's code,
just as if your code had been magically pasted into Simulation at runtime. 
This means that 
Simulation's code and your pulse sequence code shared local and global
namespaces. While convenient, the disadvantages of this outweigh the 
advantages in the long run.

### Disadvantages of the `exec` Approach
1. The shared namespace means that module and variable names in our code 
 could pollute your code
 and vice versa. We took steps to minimize this pollution but those
 steps were error-prone and hard to maintain.
1. The shared namespaces means that you were forced to use our naming 
 convention (e.g. `sys` referred to the spin system rather than the Python
 standard library module).
1. When an exception is raised in `exec`-ed code, it's hard to report
 relevant line numbers.
1. Most people aren't familiar with `exec`, so its behavior may be surprising.
1. The top of every `.py` file in Vespa contains 
 [`from __future__ import division`](http://www.python.org/dev/peps/pep-0238/)
 to ease porting Vespa to Python 3 (should that ever happen). This 
 statement affected your code as well as ours. In other words, we were 
 changing how integer division behaved in your code. We shouldn't have been 
 making this decision for you.
1. Similarly, Vespa's code contains no 
 [explicit encoding declarations](http://www.python.org/dev/peps/pep-0263/)
 which means that our `.py` files can contain only ASCII. Since your 
 pulse sequence code is mixed with Simulation's code, the presence of any
 non-ASCII characters in your code would raise an exception when Simulation 
 attempted to `exec` it.
1. [PEP 8](http://www.python.org/dev/peps/pep-0008/) recommends not mixing
 spaces and tabs in Python code. Simulation uses spaces for indentation. If 
 Simulation wanted to ensure it didn't mix tabs and spaces (which not only 
 violates PEP 8, it can confuse the parser), it needed to parse your code 
 for indentation tabs and convert them to spaces.


## What the New Interface Looks Like
*Simulation imports your code as modules.* Importing a module should 
be familiar
to anyone who has used Python, and that's how Simulation uses your pulse 
sequence code. The sequence and binning code segments you provide are saved
to temp files and then Simulation imports those files as two individual
modules: one module for the sequence code and another module for the
binning code.

This means that your sequence code is in its own namespace and your 
binning code is in its own separate namespace. It's as if they were in 
modules named `my_sequence_code.py` and `my_binning_code.py`. 

Since your code is now in independent modules and is no longer "inside" 
Simulation, it must explicitly import `pygamma` and any other modules 
it uses.


*Simulation calls the `run()` function in your code.* 
Calling a function
in an imported module should also be familiar to anyone who has used Python.
In this case, you provide a function called `run()` in both your
sequence and binning code. 
Those functions each accept a single parameter as described below.


*Simulation passes a class instance to your code instead of a dictionary.*
Simulation passes an instance of a class that describes the simulation 
with a well-defined set of 
attributes. This is not too different from the old style of passing a 
dictionary with well-defined keys.

The class contains attributes like `field`, `peak_search_ppm_low`, `dims`, 
etc. It also contains an attribute called
`spin_system` that returns a spin system for the current simulation.

For a full list of the class attributes, 
[browser:trunk/simulation/src/simulation_description.py examine the class definition] 
or consult the Simulation documentation.

The same object is passed to both the sequence and binning code, so it's 
easy to "pass" a variable created in the sequence code to the binning code.
Just assign it to an attribute on the object. For instance, to make the 
transition table matrix available to the binning code, add this to 
your sequence code:

```
#!python
sim_desc.mx = pygamma.TTable1D(ACQ.table(sigma0))
```

This demonstrates a larger point: once the simulation description object is
passed to your code, Simulation doesn't use it. Your code is free to
manipulate it as you see fit. Not only can you add attributes and methods, you
can delete and overwrite them too.


*Simulation passes 8 bit strings.* All strings passed to your code in the
simulation description are UTF-8 encoded 8 bit strings. If you don't
know what this means, you can probably just ignore it. Specifically, it means 
that the strings are [gamma:wiki:PyGammaAndPythonStrings safe for PyGAMMA].


*Your code returns results via a `return` statement.*
Your code (sequence or binning, as explained below) should return a 3-tuple 
of lists (or other iterables) 
of floats that represent the ppm, area, and phase values. The phrase 
_"...(or other iterables)..."_ means that the elements of the 3-tuple can 
be lists, tuples, `pygamma.DoubleVector` objects, `numpy` arrays, etc. They 
don't even have to be of the same type. For instance, this is a valid
set of results:
```
#!python
return ( [0, 0, 0], numpy.zeros(3), pygamma.DoubleVector(3) )
```

The tuple elements must be the same length. If they're not,
Simulation discards your results and raises a ValueError.


*You can return results from the sequence or binning code.*
Since not everyone will want to run a binning step, we've made it easy to
skip. If your sequence code returns a 3-tuple of results as described
above, Simulation won't call your binning code. If your sequence code 
returns `None` (or doesn't have a `return` statement at all), then 
Simulation will call your binning code which must return the 3-tuple of
results.


*Results must contain only Python `float`, `int` or `long` objects.*
The type of every element in the ppm, area and phase lists must be
`float`, `int` or `long`. One can't return, for example, Python complex 
numbers, PyGAMMA complex numbers, or `ctypes.c_float` objects. 

If this rule is violated, 
Simulation discards your results and raises a ValueError.
