# PyGAMMA: Garbage Collection, SWIG and Unpredictable Behavior
## Introduction
GAMMA is written in C++, and the PyGAMMA wrapper is automatically generated
by a very useful program called [SWIG](http://www.swig.org/). SWIG handles some, but not 
all of the differences between C++ and Python memory management. Specifically,
Python provides automated garbage collection while C++ does not. SWIG tries to
make this transparent but does not always succeed when dealing with C++ objects that reference other objects.

Due to these differences in memory management, code that worked fine in C++ may _not_ work properly if you simply translate the C++/GAMMA code directly to Python/PyGAMMA syntax. The consequences are familiar to anyone who has
written C/C++ code: a reference to deallocated memory generates a segfault,
bus error, or data that changes without writing anything to it.

In general terms, here's how this problem can arise when using PyGAMMA. 
A class, BigClass, manages another, SubClass. A BigClass instance is created in a function. BigClass has a method, sub(), that returns a pointer or reference to SubClass. When using SubClass in pure C++, all is well. But in PyGAMMA, the BigClass instance will be garbage collected once it is no longer referenced, *and so will the SubClass instance*. After that, the pointer or reference to SubClass is invalid. The next time your code accesses the SubClass instance, the outcome will probably be bad.

```
#!python

def a_function():
    big = BigClass()
    a_sub = big.sub()
    # The BigClass instance will be destroyed when this function
    # exits, and the subclass instance along with it!
    return a_sub

a_sub = a_function()
a_sub.do_something() # Bad things happen here.
```


We have a complete [BigClassExample BigClass example], and a real PyGAMMA
example below. One can also read [SwigGoryDetails all the gory details about SWIG and memory management].

## A PyGAMMA Example
Let's look at a real example that causes the problem.
Notice that in the function 'sequence(...)' we are creating an acquire1D object, ACQ. Then we are calling ACQ's method, 'table(sigma0)' and assigning it to mx. Finally, sequence returns mx.

```
#!python
import pygamma

def sequence(spin_system):

    H   = pygamma.Hcs(spin_system) + pygamma.HJ(spin_system) 
    D   = pygamma.Fm(spin_system, "1H") 
    ACQ = pygamma.acquire1D(pygamma.gen_op(D), H, 0.000001) 

    sigma  = pygamma.sigma_eq(spin_system) 
    sigma0 = pygamma.Iypuls(spin_system, sigma, "1H", 90.0) 

    mx = ACQ.table(sigma0)

    # The ACQ instance will be destroyed when this function
    # exits, and the mx instance along with it!
    
    return mx


def binning(mx, field, spin_count):
    
    ppm   = pygamma.DoubleVector(0)
    area  = pygamma.DoubleVector(0)
    phase = pygamma.DoubleVector(0)

    mx.calc_spectra(ppm, area, phase, field, spin_count,  0.0015, 50.0, 0.0, 10.0)


field = 64.0
spin_count = 3

sys = pygamma.spin_system(spin_count)
sys.Omega(field)

sys.isotope(0, "1H")
sys.isotope(1, "19F")
sys.isotope(2, "19F")

print "Calling the sequence code"
mx = sequence(sys)

print "Calling the binning code"
binning(mx, field, spin_count)

print "Done"
```

The problem is that mx is a reference to the TTable1D that is "owned" by ACQ (the acquire1D object). After sequence() returns, the ACQ object is garbage collected, along with the underlying TTable1D object - and mx is now a pointer to nothing (or stale data). 

The error pops up right after this line:
```
print "Calling the binning code"
```
i.e. when we try to access the mx object that is not there. 

If you copy the above code into a file (e.g. test_error.py) and run it, you might see this:
```
~/dev/gamma/pygamma$ python test_error.py

Calling the sequence code
Calling the binning code
Segmentation fault
```

Obviously the behavior can vary, but on Linux we usually see a segmentation fault.


## How To Avoid This Pitfall
Here are a few ways to avoid this problem.

### 1 - Make Copies
Change this line,

```
#!python
mx = ACQ.table(sigma0) 
```

to this:

```
#!python
mx = TTable1D(ACQ.table(sigma0))
```

This creates a new TTable1D object (and assigns it to mx), by copying values from the object returned by ACQ.table(sigma0). This new object will not be garbage collected when the function returns.

Most PyGAMMA objects have a creation method that takes an instance of it's own type as an input. For example: 

```
my_new_ObjectX = ObjectX(old_objectX)
```


### 2 - Flatten Your Code
Flatten out the code so that ACQ is not destroyed until you are done with mx.
In other words, get rid of 'sequence(...)' as a subroutine. Note that this
isn't an option in a [simulation:wiki Vespa Simulation] pulse sequence
because the sequence and binning code is always separate.

```
#!python
import pygamma

# Moved 'sequence(..)' code into main flow of program (see below)


def binning(mx, field, spin_count):
    
    ppm   = pygamma.DoubleVector(0)
    area  = pygamma.DoubleVector(0)
    phase = pygamma.DoubleVector(0)

    mx.calc_spectra(ppm, area, phase, field, spin_count,  0.0015, 50.0, 0.0, 10.0)


field = 64.0
spin_count = 3

sys = pygamma.spin_system(spin_count)
sys.Omega(field)

sys.isotope(0, "1H")
sys.isotope(1, "19F")
sys.isotope(2, "19F")

# print "Calling the sequence code"

# Sequence code moved here

H   = pygamma.Hcs(spin_system) + pygamma.HJ(spin_system) 
D   = pygamma.Fm(spin_system, "1H") 
ACQ = pygamma.acquire1D(pygamma.gen_op(D), H, 0.000001) 
sigma  = pygamma.sigma_eq(spin_system) 
sigma0 = pygamma.Iypuls(spin_system, sigma, "1H", 90.0) 

mx = ACQ.table(sigma0)

print "Calling the binning code"
binning(mx, field, spin_count)

print "Done"
```


### 3 - Move the Construction of mx
Change the method 'sequence(...)' to return all the objects that would be needed to generate mx, in this case, ACQ and sigma0.

```
#!python
import pygamma

def sequence(spin_system):

    H   = pygamma.Hcs(spin_system) + pygamma.HJ(spin_system) 
    D   = pygamma.Fm(spin_system, "1H") 
    ACQ = pygamma.acquire1D(pygamma.gen_op(D), H, 0.000001) 

    sigma  = pygamma.sigma_eq(spin_system) 
    sigma0 = pygamma.Iypuls(spin_system, sigma, "1H", 90.0) 

    # mx = ACQ.table(sigma0)
    # return mx

    return (ACQ, sigma0)


def binning(mx, field, spin_count):
    
    ppm   = pygamma.DoubleVector(0)
    area  = pygamma.DoubleVector(0)
    phase = pygamma.DoubleVector(0)

    mx.calc_spectra(ppm, area, phase, field, spin_count,  0.0015, 50.0, 0.0, 10.0)


field = 64.0
spin_count = 3

sys = pygamma.spin_system(spin_count)
sys.Omega(field)

sys.isotope(0, "1H")
sys.isotope(1, "19F")
sys.isotope(2, "19F")

print "Calling the sequence code"
acq, sigma = sequence(sys)
mx = acq.table(sigma)

print "Calling the binning code"
binning(mx, field, spin_count)

print "Done"
```


### 4 - Get a Fresh Copy of Your Object
Pick a new function that returns a fresh copy of the object. 

When creating PyGAMMA, we did not want to change the signature of this function:

```
const TTable1D& table(const gen_op& sigmap);
```

...since some users in C++ (and python) may be using the fact that it is a reference back to the original TTable1D that is part of the acquire1D object.

So, we created a new function that would take a snapshot of the current TTable1D and return that new object.

```
const TTable1D table_snapshot(const gen_op& sigmap);
```

and solving the problem that way. Perhaps there is a similar function available (or could be written) for the issue you are trying to solve. Here is how this would look in solving our current issue.

```
#!python
import pygamma

def sequence(spin_system):

    H   = pygamma.Hcs(spin_system) + pygamma.HJ(spin_system) 
    D   = pygamma.Fm(spin_system, "1H") 
    ACQ = pygamma.acquire1D(pygamma.gen_op(D), H, 0.000001) 

    sigma  = pygamma.sigma_eq(spin_system) 
    sigma0 = pygamma.Iypuls(spin_system, sigma, "1H", 90.0) 

    mx = ACQ.table_snapshot(sigma0)
    
    return mx


def binning(mx, field, spin_count):
    
    ppm   = pygamma.DoubleVector(0)
    area  = pygamma.DoubleVector(0)
    phase = pygamma.DoubleVector(0)

    mx.calc_spectra(ppm, area, phase, field, spin_count,  0.0015, 50.0, 0.0, 10.0)


field = 64.0
spin_count = 3

sys = pygamma.spin_system(spin_count)
sys.Omega(field)

sys.isotope(0, "1H")
sys.isotope(1, "19F")
sys.isotope(2, "19F")

print "Calling the sequence code"
mx = sequence(sys)

print "Calling the binning code"
binning(mx, field, spin_count)

print "Done"
```


### 5 - Get mx Differently
Change the 'sequence(...)' function to return ACQ, and then apply a different table method to get mx (i.e. with no arguments).

```
import pygamma

def sequence(spin_system):

    H   = pygamma.Hcs(spin_system) + pygamma.HJ(spin_system) 
    D   = pygamma.Fm(spin_system, "1H") 
    ACQ = pygamma.acquire1D(pygamma.gen_op(D), H, 0.000001) 

    sigma  = pygamma.sigma_eq(spin_system) 
    sigma0 = pygamma.Iypuls(spin_system, sigma, "1H", 90.0) 

    # NOTE: this call to table(sigma0) actually changes the 
    # internal table as well as returns a reference to it.
    ACQ.table(sigma0)
    
    return ACQ


def binning(mx, field, spin_count):
    
    ppm   = pygamma.DoubleVector(0)
    area  = pygamma.DoubleVector(0)
    phase = pygamma.DoubleVector(0)

    mx.calc_spectra(ppm, area, phase, field, spin_count,  0.0015, 50.0, 0.0, 10.0)


field = 64.0
spin_count = 3

sys = pygamma.spin_system(spin_count)
sys.Omega(field)

sys.isotope(0, "1H")
sys.isotope(1, "19F")
sys.isotope(2, "19F")

print "Calling the sequence code"
ACQ = sequence(sys)
mx = ACQ.table()

print "Calling the binning code"
binning(mx, field, spin_count)

print "Done"
```


### 6 - Shuffle the Location of References
You can create the object before the subroutine is called, and pass it into the subroutine - as in this slightly artificial example.

```
#!python
import pygamma

def sequence(spin_system, ACQ):

    sigma  = pygamma.sigma_eq(spin_system) 
    sigma0 = pygamma.Iypuls(spin_system, sigma, "1H", 90.0) 

    mx = ACQ.table(sigma0)
    
    return mx


def binning(mx, field, spin_count):
    
    ppm   = pygamma.DoubleVector(0)
    area  = pygamma.DoubleVector(0)
    phase = pygamma.DoubleVector(0)

    mx.calc_spectra(ppm, area, phase, field, spin_count,  0.0015, 50.0, 0.0, 10.0)


field = 64.0
spin_count = 3

sys = pygamma.spin_system(spin_count)
sys.Omega(field)

sys.isotope(0, "1H")
sys.isotope(1, "19F")
sys.isotope(2, "19F")

H   = pygamma.Hcs(sys) + pygamma.HJ(sys) 
D   = pygamma.Fm(sys, "1H") 
ACQ = pygamma.acquire1D(pygamma.gen_op(D), H, 0.000001) 

print "Calling the sequence code"
mx = sequence(sys, ACQ)

print "Calling the binning code"
binning(mx, field, spin_count)

print "Done"
```


### Advanced Solution(s)
SWIG offers some avenues for dealing with this problem, but they're non-trivial and require considerable SWIG and C++ expertise (not to mention
time), and we're not 100% sure that they would solve the problem.

  * In some cases it may be possible to set the SWIG disown flag to zero. 
  * It may also be possible to deal with this situation using typemaps.

