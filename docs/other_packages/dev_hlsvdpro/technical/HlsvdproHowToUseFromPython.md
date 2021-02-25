# How to Use HLSVDPro from Python
This document describes how to call HLSVDPr ofrom Python.

## Background
The HLSVDPro project creates a Python module called 'hlsvdpro' that is a 'blackbox' algorithm for modelling time domain signals as a sum of Lorentzian lines. It calls the PROPACK SVD algorithm as one of its steps. The remainder of the hlsvdpro algorithm is performed in Python via Numpy and Scipy calls. 

The PROPACK library is written in Fortran and compiled to a library
(DLL/shared object/dylib) as part of the HLSVDPro build. The PROPACK library functionality is accessed through the hlsvdpro.propack module. This is a Python wrapper to all the various FORTRAN flavors (single, double, complex and dcomplex) that are available. The wrapper determines automatically which one to call. The 'svdp()' method is the access point for the PROPACK functionality.

To call the HLSVDPro algorithm, add 'import hlsvdpro' at the top of your script and call the hlsvdpro.hlsvd() method. 

The binary libraries have been built in 64-mode only. It's possible to build them for 32-bit mode but we don't support that.

## Demo Code
We have [source:trunk/hlsvdpro/simple_test.py code that demonstrates calling HLSVDPRO]. That code also interprets the results and displays a plot of the observed vs. estimated values.

[source:trunk/hlsvdpro/hlsvd.py The Python wrapper] contains an extensive docstring
that describes inputs and outputs.

## Testing
HLSVDPRO is [HlsvdTesting difficult to test] without inspecting the results manually.


---------

# Deprecated Information for version 1.x
The Python code in HLSVDPRO is simple and is compatible with Python 2 and 3.

## Background
HLSVDPRO is written in Fortran and compiled to a library
(DLL/shared object/dylib). It only exposes one function which is
`hlsvdpw_python()` in [source:trunk/hlsvdpro/src/hlsvdpro.f hlsvdpro.f]. That
function is a convenience wrapper (in Fortran) around the core
functionality.

Since there's only one function to call, we chose to wrap it using `ctypes`.

The [source:trunk/hlsvdpro/hlsvd.py Python code] is a single-function convenience
wrapper around the Fortran convenience wrapper. The Python code handles
loading the binary library and passing data via `ctypes`.

The binary libraries have been built in 64-mode only. It's possible to
build them for 32-bit mode (see the 
[source:trunk/hlsvdpro/src Makefiles] in the `src` directory) but we 
don't support that.

## Demo Code
We have
[source:trunk/hlsvdpro/demo/demo.py code that demonstrates calling HLSVDPRO].
That code also interprets the results and displays a plot of the observed
vs. estimated values.

[source:trunk/hlsvdpro/hlsvd.py The Python wrapper] contains an extensive docstring
that describes inputs and outputs.

On Linux, you'll need to install `libfftw3` before running HLSVDPRO.


