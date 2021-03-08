---
sort: 2
---

# HLSVDPro

This package is a Python wrapper around an algorithm based on the 2002 Laudadio JMR paper that fits of a model function (sum of Lorentzian) to time-domain data via the state space approach. This algorithm uses the PROPACK SVD library to calculate the first (user specified) N singular values, and then create an N line approximation to the data.

As of version 2.0.0 we also provide access to the PROPACK SVD function calls. 

**References/Timeline:**

- The state space approach is described in S.Y. Kung, K.S. Arun and D.V. Bhaskar Rao, J. Opt. Soc. Am. 73, 1799 (1983).

- HLSVDPro version 1.x implementation was based on the algorithm described in W.W.F. Pijnappel, A. van den Boogaart, R. de Beer, D. van Ormondt, J. Magn. Reson. 97, 122 (1992). 
  - Dependencies on PROPACK version 1.x and FFTW.
  - Algorithm code was written in FORTRAN and accessed by Python wrapper using CTYPES front end.
  - Package focused entirely on retuning a 'fitted' model of Lorentzian lines to the data 
  - Output was a set of amplitude, frequency, phase and damping values that described the fit for the first (user specified) N model lines. 
  - Used the PROPACK (version 1.x) SVD algorithm to calculate the first N singular values.

- HLSVDPro version 2.x implementation is based on the algorithm described in T. Laudadio and N. Mastronardi and L. Vanhamme and P. Van Hecke and S. Van Huffel, "Improved Lanczos algorithms for blackbox MRS data quantitation", Journal of Magnetic Resonance, Volume 157, pages 292-297, 2002. 
  - Dependency on PROPACK version 2.2 library.
  - Structured more modularly, so HLSVDPro module also allows access to the PROPACK SVD function calls.
  - Uses f2py front end to access PROPACK SVD calls
  - HLSVDPro algorithm is organized in Python now, with calls to PROPACK or Scipy for computing the 'fitted' Lorentzian model lines


## Usage From Python
We have a description of [HlsvdproHowToUseFromPython how to call this library from Python].

## About the Experimental Python Port
[HlsvdproPort  HLSVDPro has been ported to pure Python] although the result has a few problems that make it unsuitable for daily use.

## Related Projects of Interest
We know of two other implementations of the PROPACK library that's at the core of HLSVDPRO.

Jake Vanderplas [project that provides a Python wrapper for a version of the PROPACK library](https://github.com/jakevdp/pypropack). 
His code is BSD licensed.

Michael P. Friedlander wrote [a PROPACK implementation](https://github.com/dpo/nlpy/blob/develop/nlpy/linalg/propack.py) 
that's part of a larger project. That code is GPL licensed.


## Developer/Maintainer Documentation
 * HowToBuildWheels - How to build wheels for public release
 * HlsvdproHowToUploadWheels - How to upload wheels.
 This document was written for PyGamma but the process for
 HLSVDPRO is the same.
 * HlsvdproHowToReleaseNewVersion - How to release a new version
 * HowToBuildWheelsWindowsSetup - One-time setup of Windows for 
 building wheels
 * HowToBuildWheelsLinuxSetup - One-time setup of Linux for 
 building wheels
 * HowToBuildWheelsOsxSetup - One-time setup of OS X for 
 building wheels
 * HlsvdproLibraryDependencies - How dependencies are satisfied
 * HlsvdproHowToSetUpCentOs - How to create a CentOS machine for building HLSVDPro Linux wheels
 * [gamma:wiki:PyGammaWhyNoSourceDistribution This document about PyGamma] applies to HLSVDPRO as well

----------
# A Little History of version 2.x
HLSVDPro v2.x is based on the extended algorithm in the 2002 JMR paper by Laudadio.
 - It uses PROPACK v2.2 and does not have an FFTW dependency. 
 - The algorithm is now written in Python, but that mainly just calls a few Numpy, Scipy and PROPACK functions. 
 - The speed is about the same as the original CTYPES wrapped code.
 - We now have access to the PROPACK functions directly for performing sparse SVD calculations.

In creating the HLSVDPro v2.x package, I started with the Jake Vanderplas code for just the PROPACK v2.2 libray.  I had to modify it quite a bit. As our wiki states, we developed HLSVDPro to work within the 'Vespa' project (https://scion.duhs.duke.edu/vespa/project) and wanted it to be as self contained as possible.  For HLSVDPro v2.x that meant that I could not assume that there would be a 'system LAPACK or BLAS' available. 

So to create the PROPACK v2.2 library, I had to add in all the missing library files for those calls that PROPACK needed.  And I could not assume that the gfortran library would be available, so I had to figure out how to statically link that in.  So basically, I'm breaking all the rules of 'reusable code' in the name of making it work on Windows.

Anyway, I added all the files to PROPACK source tree for the single, double, complex and dcomplex versions of the library.  I used f2py to generate some of the wrapping code for calling FORTRAN from Python. But I had to 'hand wrap' Makefiles to enforce static linking, and just use trusty old 'make' to do the actual compiling. I then created LOTS of different libraries, because f2py had to be linked against whatever version of Python was going to call it. 

There are libraries for: 1) single, double, complex, dcomplex PROPACK, 2) Python 27, 36, 37, 38, and 3) Linux, Windows, MacOS ... so, LOTS, like 48.  The Makefiles help with some of this. But, eventually, I have to make Python wheels for the different versions. Just FYI, the main reason for using f2py (from Jake Vanderplas) was to allow a user to define the matrix product function call (Aprod) as a Python function and then pass that into the FORTRAN call.  This required that (d)complex numbers be sent in, and CTYPES does not handle those types. So, f2py to the rescue and more complexity. But now, back to our story ...

Now that I had the PROPACK v2.2 library available in Python, I worked on porting the HLSVDPro algorithm from FORTRAN to Python.  That ended up being pretty easy, since all the necessary LAPACK calls  seemed to either be available in Scipy.lapack, or equivalent calls were present in Numpy or Scipy themselves. 

The actual Python algorithm (without comments) is only about 15 lines long and runs about as fast as pure FORTRAN, but with more flexibility. 
