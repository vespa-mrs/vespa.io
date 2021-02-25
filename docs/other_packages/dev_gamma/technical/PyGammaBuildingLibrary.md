# How To Build PyGamma
This document describes how to build PyGamma. Note that we offer
[PyGamma#InstallingPyGamma pip-installable binaries] for many platforms.

## Overview
Building PyGamma consists of 3 general steps --
1. Satisfying prerequisites
1. Building PyGamma
1. Installing PyGamma

These steps are explained in detail below.

## Satisfy Prerequsities (All Platforms)
1. Follow the [GammaBuildingLibrary#DownloadtheCode instructions for downloading the code].
1. Install Python if you haven't already.
1. Install [SWIG](http://www.swig.org/).
1. Install a compiler (see platform-specific instructions below).

## Compiler (Unix[-Like] Platforms)
PyGamma builds with `gcc` 4.x and 5.x. It also builds with `clang/LLVM`.

*Linux users*, in addition to installing `gcc` (and possibly
`gcc-c++`), you might also need to install the development package for
your version of Python. If the build complains that `Python.h` is missing,
you need to install a package called something like `python-dev`.

*Under OS X*, download
[XCode/Developer XCode](https://developer.apple.com/xcode/)
to get the build tools you need.

If you're not on OS X, you might want to consider installing an
[GammaWithBlasLapack optimized linear algebra library]
before building, although this is not essential and will complicate the build.
OS X already has such a library
installed, and PyGamma can take advantage of it.

## Compiler (Windows)
PyGamma is known to build with MSVC 2008. Note that under Windows, Python
extensions like PyGamma must be compiled with the same compiler as was used
to compile Python. MSVC 2008 is used to build Python 2.7.

## How To Build on Unix[-Like] Platforms (OS X, Linux, etc.)
Once you have the prerequisites installed, go to a command line and then
change to the `gamma/platforms` directory. Once there, change into the
subdirectory appropriate for your platform. Then, execute this command --
```
make pysgdist
```

That will build PyGamma and place the relevant build output files in a place
where `setup.py` can find them. When this process completes, you're ready to
install PyGamma as explained below.


## How To Build on Windows
1. Open file `gamma/platforms/msvc2008e/dynamic/gamma.sln` in Visual Studio.
1. Ensure that `python.exe` is in your PATH.
1. Either ensure that `swig.exe` is in your PATH, or edit the build properties
 to supply an explicit path to `swig.exe` on your machine.

 If you opt for the
 latter, open the Visual Studio _Project-->Properties_ menu.
 Then select _Configuration Properties --> Build Events --> Pre-Build Events_
 and then edit the _Command Line_ property. Change "swig" to an explicit
 path. The result will look something like this:
```
 "C:\Program Files\swigwin-2.0.0\swig.exe" -c++ -python -outdir ..\..\i686-pc-msvc  -I..\..\src -o ..\..\i686-pc-msvc\pygamma_wrap.cxx pygamma.i
```
1. Hit F7 to start the build.

The steps above will build PyGamma and place the relevant build output files
in a place where `setup.py` can find them. When this process completes, you're ready to
install PyGamma as explained below.


## Installing PyGamma (All Platforms)
1. `cd gamma/pygamma`
1. `python setup.py install`

## Testing PyGamma (All Platforms)
Once PyGamma is installed, you can run an automated test under any Unix-like
operating system from the command line. Change directory to `gamma/platforms`
and then move into the appropriate platform (Linux, OSX, etc.). From there,
execute `make pytest`.

This runs the tests in `gamma/src/pyTest`. You can also run the `.py` files
there manually.

Under Windows, you can run the automated tests from within Visual Studio.
Right click on the `pytest` project and build it to run all the tests in the
`gamma/trunk/src/pyTests` directory.
