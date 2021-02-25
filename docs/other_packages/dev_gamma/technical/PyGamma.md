# PyGamma
PyGamma is a Python-wrapped version of [GammaDetailedDescription GAMMA]. It combines the power 
of the GAMMA library with the convenience of working in 
[the Python programming language](http://www.python.org/). Python is open 
source, object-oriented, and considerably easier to write than C++. 

PyGamma works with Python 2.7. We haven't tested it with Python 3.

The PyGamma wrapper was created using [SWIG](http://www.swig.org/). Most,
but not all of GAMMA is [SwiggedGammaListing available to Python through PyGamma]. 

We have are some [tips on exploring and using PyGamma](/wiki:PyGammaUsageTips/).

The [GammaVsPyGamma performance of PyGamma] for compute-intense calculations 
is very comparable to that of GAMMA.

## Installing PyGamma
As of version 4.3.3, PyGamma is installable via pip, Python's preferred installer program.

We strongly recommend upgrading to the latest version of pip before installing 
pygamma.

To upgrade pip, use this command --
```
python -m pip install --upgrade pip
```

To install PyGamma, use this command --
```
pip install pygamma
```

If pip isn't installed, get it via the the instructions here:
https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py

## How To Build a Custom PyGamma
Most people will be able to use one of the prebuilt, pip-installable PyGamma packages. But if a package isn't available for your platform, or you want to do something special with the build,
we have instructions for [PyGammaBuildingLibrary how to build PyGamma].