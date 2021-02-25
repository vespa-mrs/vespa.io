# Tips on Exploring and Using PyGAMMA
This page gives some very basic advice as to how to explore and use PyGAMMA. As users make greater use of this facility, and have time to give back to the GAMMA/PyGAMMA community we encourage their contributions to this page.

## Basics
If you are new to [Python](http://www.python.org/), you will first need to get comfortable with that language.

It will be assumed below that you [PyGamma#DownloadingPyGAMMA downloaded and installed the PyGAMMA library].

The next step is to get familiar with what functions are available in GAMMA. There is currently no official documentation for this, but one can look into the *Swig interface files* to see what functions have been converted to Python and learn more about their interfaces. Here is a listing of what files have been "Swigged" so far: [Swigged GAMMA Files](/wiki:SwiggedGammaListing/).

## Exploring PyGAMMA (Via the Swig Interface Files)
Say you want to create a spin system. You discover in the directory src/HSLib there are three promising files, SpinSystem.cc, SpinSystem.h and SpinSystem.i. The first two files are C++ code. The third file, SpinSystem.i, is the Swig interface file. All commands in files with a ".i" extension - that are not commented out - are available in Python.  Swig knows how to convert Python strings, integers, floating point numbers, and arrays (lists, numpyarrays, etc) to and from C++ strings, integers, floats or doubles, and std::vector and std::list, etc.

The listing below is a truncated version of SpinSystem.i. 

```

// SpinSystem.i
// Swig interface file.

%{
#include "HSLib/SpinSystem.h"
%}


%include "std_string.i"
%include "std_vector.i"
%include "HSLib/SpinSys.i"

%rename(__assign__) spin_system::operator=;


class spin_system: public spin_sys
{

public:

spin_system(int spins=0);
spin_system(const spin_system &sys);

virtual       ~spin_system ();
spin_system&  operator= (const spin_system &sys);

virtual void   shifts(double shift=0);
virtual void   shift(int, double);
virtual double shift(int)          const;

double maxShift()                  const;
double maxShift(const std::string& Iso) const;
double minShift()                  const;
double minShift(const std::string& Iso) const;
double medianShift()               const;
double lab_shift(int)              const;	// Typically ~10^8 !

// ...REMOVED THIS SECTION OF CODE FOR BREVITY..

};

```

You can see that there are two was to create a new spin system. One involves using an integer as an input to specify the number of spins,
```
spin_system(int spins=0);
```

The other requires a previous spins system as an input,
```
spin_system&  operator= (const spin_system &sys);
```

We'll put that knowledge to use very shortly.

## Using PyGAMMA
We list here two ways to use PyGAMMA. You can use PyGAMMA interactively from a command line Python session, or you can write a PyGAMMA file/program that you will call/run from the command line (see below) with python.

1. Using PyGAMMA from a Python command line session.
  * Start a python session
  * Import pygamma (and assign an alias to it, if you want)
  * Use pygamma, e.g. to create a new spin system. Note, you can see that the variable sys in fact "points" to a proxy of a Swig spin_system.

```
C:\>python
Enthought Python Distribution -- http://www.enthought.com
Version: 6.2-2 (32-bit)

Python 2.6.5 |EPD 6.2-2 (32-bit)| (r265:79063, May  7 2010, 13:28:19) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import pygamma as pg
>>>
>>> sys = pg.spin_system(3)
>>>
>>> sys
<pygamma.pygamma.spin_system; proxy of <Swig Object of type 'spin_system *' at 0x00A6F8F0> >
>>>
```

2. Using PyGAMMA "code" from a file.

_ *Here is a working example, that includes a spin system* _

The listing below could be typed into a Python command line session, but if your going to use something over and over again it's better to create a file and save your PyGAMMA python code. The following text in from the file called fid.py:

Listing for [browser:trunk/src/pyTests/fid.py fid.py]:

```
from __future__ import division

import pygamma as pg 

infile = 'gsh_test.sys' 
outfile = "gsh_fid_pytest.txt" 
h1 = "FID Simulation Test"
h2 = "using input sys file: " + infile
outname = "test_lines"
header = (h1, h2)
sys = pg.spin_system() 
sys.read(infile) 
specfreq = sys.Omega() 
H = pg.Hcs(sys) + pg.HJ(sys) 
D = pg.Fm(sys) 
ac = pg.acquire1D(pg.gen_op(D), H, 0.001) 
ACQ = ac 
sigma = pg.sigma_eq(sys) 
sigma0 = pg.Ixpuls(sys, sigma, 90.0) 
mx = ACQ.table(sigma0) 
mx.dbwrite(outfile, outname, specfreq, sys.spins(), 0, header);   # Print Table
```

This file/program can be run by typing this at the command line:

```
python fid.py
```

Here is the listing for the input file needed to run fid.py, called gsh_test.sys:

```
SysName (2) : gsh_test
NSpins  (0) : 3  - Chemical shifts for gsh and H2O.
Iso(0) (2) : 1H
Iso(1) (2) : 1H
Iso(2) (2) : 1H
PPM(0) (1) : 3.77
PPM(1) (1) : 6.0
PPM(2) (1) : 4.7
J(0,1) (1) : 6.5
J(0,2) (1) : 0.0
J(1,2) (1) : 0.0
MutExch(0) (2) : (1,2)
Kex(0)	   (1) : 5.0
Omega  (1) : 170.67
```

This example is currently part of our python test listed in the src/pyTests directory.

## Accessing PyGAMMA Object Data
Since the code underlying PyGAMMA is fundamentally C++ code there will be a few differences in how you make use of it in Python from how you might expect.

For example, in Python all classes have member variables that are "public" meaning that anyone who has access to the object can access the member variables. In C++ however, there are frequently cases where internal class variables are defined as "private" meaning that only this class and a few select and well defined other classes can access it's members. So when accessing a C++ private variable's value, you often need to use "getter and setter" methods.

Here is an example for the PyGAMMA class IsotopeData.

We could create this Isotope Data for "Hyper Spin Hydrogen" and assigned it to the variable "id". 
```
>>> id = pg.IsotopeData(1,"17H","Hyper Spin Hydrogen","Hydrogen",1,17,42,101,33)
>>>
>>> id
<pygamma.pygamma.IsotopeData; proxy of <Swig Object of type 'IsotopeData *' at 0x1c253930> >
```

You can always check what attributes and methods are available in an object such as id (in this case of class IsotopeData) by using the python dir command, e.g.
```
>>> dir(id)
['HS', '__assign__', '__class__', '__del__', '__delattr__', '__dict__', '__doc__',
 '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', '__swig_destroy__', '__swig_getmethods__',
 '__swig_setmethods__', '__weakref__', 'electron', 'element', 'mass', 'momentum', 'name',
 'number', 'printStrings', 'qn', 'recept', 'rel_freq', 'symbol', 'this', 'weight']
```

Let's say you wanted to check id's mass; you might try to access it directly using id.mass, but this would not get you what you wanted...
```
>>> idm = id.mass
>>> idm
<bound method IsotopeData.mass of <pygamma.pygamma.IsotopeData; proxy of <Swig Object of type 'IsotopeData *' at 0x1c253930> >>
```

This would only get you the address of the member function mass. 

Instead you will need to call the method mass like this, id.mass().
```
>>> idm = id.mass()
>>> idm
17
```

Most of pygamma's objects are meant to be used internally but can be converted to python/numpy objects (providing a set of such functions
is a good future pygamma project). E.g. if you want to convert a pygamma complex number to a numpy complex number you could do the
following:
```
>>> import pygamma as pg
>>> import numpy as np
>>> n = pg.complex(3,2)
>>> p = np.complex(n.Rec(),n.Imc())
>>> p
(3+2j)
```

And recall that you could have discovered the Rec() and Imc() methods for producing the real and imaginary components of n by running dir(n).

Happy Trails exploring PyGAMMA!
