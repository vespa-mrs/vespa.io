# Gamma To Do List

## Higher Priority Items
  * SWIG any remaining bits of the public interfaces. Convert some of the "friend" functions to regular functions - either member functions of the class or external to the class - and make them available via Swig.
  * Consider doing SWIGing AND _building_ of C++ code using Distutils, from a new /gamma/trunk/src/pybuild  directory.
  * Parallelize the code using OpenMPI and iPython.
  * Further speed up code by implementing CUDA, or new NVIDIA development libraries (part of Fermi Architecture).

## Lower Priority Items
  * See if Linux Makefile works with Cygwin.
  * Shorten the run time on tests.
  * Move build intermediate output to a sub-directory of the "make" directory (/primal/Linux) and only put real build end products in the "build" directory, (e.g. i-686-pc-Linux).

#### *Completed Items *  * Get code to compile on modern compilers [Linux, Windows, OSX]. _(DCT)_
  * SWIG the C++, exporting required methods to python for basic tests _(DCT)_
  * Create a testing facility for regression tests on C++ code (unit testing would be good eventually if we continue working on the C++ code-base)  _(DCT)_
  * Integrate Code base with code received from Zurich and Matthias Ernst. _(DCT)_
  * Automatically create build directory on windows. _(DCT)_
  * Split DBwrite into a line blending procedure and code to output the results, and export the line blending code to python. _(DCT)_
  * Organize and clean up code base, eliminating clutter and unnecessary code. _(Philip, DCT)_
  * Fix runtests.py for non-matching numerical data.  This is needed to get a complete match on tests run on windows. _(DCT)_
  * Explore the possibility of replacing the linear algebra code to speed up simulations (Blochlib, Atlas, LaPack++, etc).  Considering the use of the Armadillo library ( http://arma.sourceforge.net/ ). _(DCT)_ 
  * Added a pytest target to run the python tests. _(DCT)_
  * Documented SWIG-ed code oddities, and also how to Swig. _(DCT, aka David)_
  * Much of the linear algebra code has been migrated to use the new lapack on OSX and the Makefiles have been modified to use them on other operating systems if some a few lines are uncommneted (assuming the libraries are installed). _(Matthias)_
  * Makefiles and Source code was cleaned up and the old pygamma code removed. _(Philip, Matthias, Karl, David)_
  * Most of the rest of the public API's were Swigged (still a bit more to be done there). _(Karl, David)_
  

## Just a thought ...
  * Add tests from the 2003 W.B. Blanton paper to our test suite.
  * Build some unit tests (need to add a C++ unit testing environment, like google's..http://code.google.com/p/googletest/ based on xUnit)
  * Is it worth exploring the potential benefits from using boost libraries to export interfaces to python.
