# GAMMA & PyGAMMA with BLAS/LAPACK/ATLAS
[BLAS](http://www.netlib.org/blas/) and [LAPACK](http://www.netlib.org/lapack/)
are optimimzed linear algebra libraries (the latter uses the
former). [ATLAS](http://math-atlas.sourceforge.net/) is an implementation of 
BLAS and portions of LAPACK. Some or all of these libraries are available
on just about every platform.

Regardless of the acronyms involved, one can build GAMMA to take advantage
of these libraries if they're installed. The procedure for doing so varies 
from one operating system to another and is detailed below.

GAMMA is faster when built with these libraries. Quantifying the performance
increase is discussed below.

## OS X
OS X is the easiest platform to discuss since OS X ships with Apple-optimized
[BLAS and LAPACK implementations](http://developer.apple.com/hardwaredrivers/ve/vector_libraries.html).
which are always present. *GAMMA's OS X Makefile uses BLAS and LAPACK by default.*

However, we've found that 
[ticket:22 mixing a BLAS-enabled PyGAMMA with Python's multiprocessing library is toxic]
and so use of BLAS is disabled by default when building PyGAMMA. (Note that this just applies to BLAS. 
PyGAMMA for OS X still uses LAPACK.)


## Linux
BLAS, LAPACK and ATLAS are widely available under Linux, but the details
vary from on distribution to another. As a result, 
*GAMMA's Linux Makefile does not use BLAS, LAPACK or ATLAS by default.*

If you plan to use a BLAS-enabled PyGamma with Python's multiprocessing library (as Vespa) 
does, be aware that 
[ticket:22 some BLAS implementations don't work with Python's multiprocessing library]. We don't
know if this affects PyGamma on Linux.

### Linux - GOTOBLAS2
As of this writing (June 2011), our Linux Makefile is set up to use 
[GOTOBLAS2](http://www.tacc.utexas.edu/tacc-projects/gotoblas2). That BLAS
implementation has a good reputation but is unfortunately no longer being
developed. It's also not available via the package manager of many popular
Linux distributions.

If you want to enable use of GOTOBLAS2 under Linux, you'll need to install
GOTOBLAS2 and then edit the Makefile
sections marked "lapack" appropriately for your platform and
[GammaBuildingLibrary build your own GAMMA].

### Linux - OpenBLAS
At least one user has reported success with [OpenBLAS](http://xianyi.github.com/OpenBLAS/)
which is a direct offspring of GOTOBLAS2. As of this writing (January 2013), it is a live and
active project.

### Linux - GNU Scientific Library (GSL) BLAS
We are aware that GSL provides BLAS support and is available in the package
manager of many popular Linux distros. We would like to see GSL BLAS support
in GAMMA but we haven't yet found the time to do it ourselves. We'd love 
a patch! Feel free to [contact us](/wiki:Contact/) about this.


## Solaris
The Sun Studio compiler which is used by default in Solaris comes with an
optimized BLAS/LAPACK library. However, the CBLAS interface is missing and
libcblas needs to be installed separately.
*GAMMA's Solaris Makefiles use BLAS and LAPACK by default.*

## Windows
BLAS, LAPACK and ATLAS are available under Windows, but since GAMMA under 
Windows has a completely different build system than under all other 
platforms, we haven't found the time to set up use of these libraries.
*GAMMA's Windows build does not use BLAS, LAPACK or ATLAS.*

If you get GAMMA to build on Windows using BLAS, LAPACK or ATLAS, please 
let us know how you did it. We'd welcome the contribution and all GAMMA
Windows users would benefit.


## Performance Benefit
The linear algebra libraries undoubtedly improve performance for matrix
operations. In some specific cases when multiplying large matrices 
(> 256 x 256) we saw runtime reduced by as much as 90%. Note that this was 
doing matrix operations in isolation, not as part of GAMMA.

It's difficult to say how much an average GAMMA user will benefit from
using BLAS/LAPACK. The first problem of course, is to define what an 
"average" GAMMA user is. The second would be to test a variety of GAMMA 
operations under various operating systems both with and without 
BLAS/LAPACK/ATLAS.

We'd rather not invest time in generating benchmarks of questionable value.
Instead we merely recommend that you use BLAS/LAPACK/ATLAS with GAMMA
if possible on your platform. If you can help us to make it easier for others
to do that too, we'd appreciate it.

## Earlier work and notes
Listed here is a discussion of [initial work](/wiki:GammaWithLapackAtlas/) done on this project.
