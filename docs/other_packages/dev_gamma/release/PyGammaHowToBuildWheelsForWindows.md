# How To Build PyGamma Wheels for Windows
This document describes how to build PyGamma wheels for Windows.

## Introduction
This document assumes you are building a 64-bit PyGamma, although the 
build procedure is the same for both 32- and 64-bit.

## Setup
1. Install MS Visual Studio 2008 Professional version. 
1. Ensure a modern 64-bit Python is in your path.
1. `pip install wheel`
1. Install [SWIG](http://www.swig.org).

Note that the free MS VS 2008 Express cannot create 64-bit executables.

## Build PyGamma
1. Get the GAMMA source code via SVN.
1. (optional) If you need to change the version number, do so now before building, in `gamma\VERSION` file
1. Via Windows Explorer, open `gamma/platforms/msvc2008e/dynamic/gamma.sln`
1. Set the build type to 'Release' (not debug) and the platform to 'x64'.
1. From the Build menu, select 'Rebuild Solution'.
1. In the `gamma\pygamma` directory, open a cmd window, type `python setup.py bdist_wheel`

The wheel file will be in the `dist` directory.