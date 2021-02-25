# How To Build PyGamma Wheels for OS X
This document describes how to build PyGamma wheels for OS X.

## Introduction
As of this writing (March 2016), we have created our last 32-bit PyGamma.
This document assumes you are building a 64-bit PyGamma.

## Setup
1. Install XCode to get the OS X build toolchain.
1. Ensure a modern 64-bit Python is in your path.
1. `pip install wheel`
1. Install [SWIG](http://www.swig.org).

## Build PyGamma
1. Get the GAMMA source code via SVN.
1. `cd gamma/platforms/OSX`
1. `make pysgdist`
1. `cd ../../pygamma`
1. `python setup.py bdist_wheel`

The wheel file will be in the `dist` directory.

Note that the OS X Makefile and PyGamma's setup.py contain some special code to 
ensure the PyGamma wheel automatically gets the correct name. 