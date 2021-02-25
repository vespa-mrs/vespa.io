# Testing GAMMA and PyGAMMA
Here are the steps that are used to make sure that nothing major is broken...

## To Do
  1. *Add more tests. If we have more tests we'll be better off.*
  1. *Add unit tests.*

## Testing Plan for Linux (and OSX)
The following sequence of builds and tests should work without any issues. You may need to be sudo or root to execute some of these items. 

Select items on this list require a working version of Python (>= 2.5) to be installed, and are marked with a (P). And some items require Swig (S). 

Go to the build instructions for [GAMMA](/wiki:GammaBuildingLibrary/) and [PyGAMMA](/wiki:PyGamma#BuildingPyGAMMA/) for details.

We're assuming you start in the gamma/platforms/Linux or gamma/platforms/OSX directory.

  * make all
  * make install
  * make test (P)
  * make pysgdist (P,S)

  * Install and test pygamma (P)
    * cd ../../pygamma
    * python setup.py install
    * open up a python shell and try to "import pygamma"
    * from within that shell try "c = pygamma.complex(3,4)"
    * and thev confirm that c is a swig object. i.e. c <enter>
    * exit python.
    * cd ../platforms/Linux

  * Test gamma utility
    * cd  ../../src/Tests
    * gamma par_xixA.cc
    * ./a.out
    * make sure this at least begins to run, and asks for user input.
    * control-C
    * cd ../platform/Linux

  * make pytest (P)
