# GAMMA/PyGamma Technical Documentation
This page is a collection of various technical documents about GAMMA and
PyGamma. Some of it is for GAMMA's maintainers, some is for those who might
like to change or extend GAMMA, and some is general troublehsooting 
information.

## For GAMMA/PyGamma Developers
  * [project:wiki:CppCodingStandards C++ Coding Standards]: Useful C++ references 
    and a first pass on coding standards. 
  * [Gamma/PyGamma Build and Testing Overview for Windows](/wiki:Gamma/PyGammaBuildAndTestingForWindows/) - some history and details on how we set up and test a build
  * GammaTestingTools - Tools and environment setup for testing GAMMA.
  * GammaToDoList - Item that are necessary, or just good, to
  implement for the GAMMA code base and project.
  * TestingGamma - Procedures for testing a build, to guarantee that you didn't break anything (or at least that you didn't break anything that is being tested).
  * [ExtendingPygamma Extending PyGamma] can be relatively simple.


## For GAMMA/PyGamma Release Managers
  * [wiki:Versioning] - Our versioning guide for GAMMA and PyGamma, including
  instructions on how to release a new version of PyGamma.
  * PyGammaHowToBuildWheelsForLinux - How to build PyGamma wheels for Linux
  * PyGammaHowToBuildWheelsForOsx - How to build PyGamma wheels for OS X
  * PyGammaHowToBuildWheelsForWindows - How to build PyGamma wheels for Windows
  * PyGammaHowToUploadWheels - How to upload PyGamma wheels to PyPI.
  * PyGammaHowToSetUpCentOs - How to create a CentOS machine for building PyGamma Linux wheels


## Issues With PyGamma
### SWIG, and Garbage Collection
While PyGamma mostly behaves as happy normal Python, there are a few instances where this is not true. In those cases, a little bit of care must be taken to write code that does not have unpredictable behavior.

The reasons for this include the fact that Python has reference counting and garbage collection and C++ does not. And while SWIG (the tool used to create PyGamma from GAMMA) has some support for keeping track of object ownership, it is not complete (for good reasons) - and in some cases there are ambiguities as to what it should do. In addition, C++ has copy semantics and Python has pointer semantics.

So, code that worked fine in C++ may *not* work properly if you simply copy the code, and change it's syntax to that of Python. And code written using Python semantics may, in certain circumstances, not perform as expected.

If you accidentally invoke one of these cases, your code will cause a segfault (segmentation fault), or other serious and/or strange errors during execution.

[Details of this Issue and Work-arounds](/wiki:SwigGarbageCollection/).

### Unicode Strings
Be aware that 
[PyGammaAndPythonStrings PyGamma can't accept Python's Unicode strings].


## Performance
 * GammaVsPyGamma - The performance of PyGamma (the swigged version of 
 GAMMA) relative to "native" GAMMA.

 * GammaVsSpin - GAMMA Performance as a function of the number of spins in
 the metabolite being studied.

 * GammaWithBlasLapack - Speeding up GAMMA with Lapack/Atlas, etc.



## Historical Notes
We (the Vespa team) took over maintenance of a dormant GAMMA late in 2009.
It had probably been about six years since GAMMA was actively advanced, and
it took us some time to get GAMMA to compile with modern compilers. We also
added the SWIG interface, which is entirely new.

These documents contain some notes from that time when we were working on 
releasing our first version which was GAMMA 4.2.0.

 * CodeChangesToCompile - Changes we made to get GAMMA to
 compile on gcc 4.3.3 (on Ubuntu 9.04), Visual Studio 2008 Express (Windows 
 XP), and gcc 4.0.1 (Mac OSX).

 * GammaSwigIssues - Found while getting
 environment setup and testing the basic functionality of SWIG. While using gcc
 4.3.3/Ubuntu 9.04/Swig 1.3.9/python2.5 and 2.6

 * GammaSwigImplementation - Swig Implementation notes, including
 organization of code, some (potentially remaining) issues, and Makefile and
 visual-studio modifications.

 * GammaMergerwithZurich - Merging C++ code with that from Zurich (Matthais
 Ernst), changes, issues, etc.

 * CodeCleanup - Code Cleanup Notes. Those who were familiar with the
 old version of GAMMA might be interested in some of the files we got rid of.