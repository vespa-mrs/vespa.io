# Gamma/PyGamma Build and Test Situation on Windows
We need to compile Gamma and PyGamma with the [same compiler used to compile the CPython](/wiki:WhatCompilerIsMyPython/) on which we intend to import Gamma/PyGamma. For Python 2.7 that was Visual Studio 2008 and for Python 3.7 it was Visual Studio 2017. Since Python 2.7 is no longer officially supported, I'm only going to go over how we build and test for Python 3. And as of this writing, we've only tested for Python 3.7, but I'm sure there will be more to come eventually.

## Advice for setting up a Windows Build environment
Install Visual Studio 2019 Community edition, which is free. While on the Installer dialog's configuration page (where you can pick what it installs), select the "Desktop development with C++" module from the icons in the left column. Then on the right column, you can select more/less options within that module. Be sure to select the "Windows 10 SDK" and "MSVC v141 - VS 2017 C++ x64/x86 build tools". This will allow you to compile Gamma using the VS 2017 compiler within the VS 2019 IDE.

The gamma.sln files in either the msvc2019\dynamic or msvc2017\static should open up within VS 2019 after it installs with all the appropriate settings already selected. I usually right click on the gamma.sln entry in the Solution Explorer and select "Build Solution" to create the library, but that's just me.  This isn't a tutorial on VS 2019.

There are two other programs needed to perform a Build. SWIG has to be installed. For Python 3.x we have been using version 4.0.1. The SWIG executable should be discoverable on your PATH environment variable.  There are also some calls to Python scripts, so Python has to be discoverable on your PATH environment variable. NB. the first Python install found in PATH is the one that will be used for all steps in the Build.  So if you have multiple Python installtions (e.g. 3.5, 3.6, 3.7 etc) make sure that the first one in PATH is the one against which you want to compile PyGamma.  I usually do this in the Environmental Variable dialog where I edit PATH and just 'move up' the Python paths that I want to the top of the list.

## Overview of the Static and Dynamic project and where is PyGamma?
Honestly, our true fixation is creating PyGamma, which uses the DLL created in the 'dynamic' project. However, Gamma is easier to test if it is statically linked to the test programs. So we have the two different solutions 'static' and 'dynamic' which allow us to do both things.  

The static project has nothing to do with PyGamma, just for testing that Gamma (and any changes we have made to Gamma) is working. And honestly, it only tests the things in the various test programs we have. So, if you add any code to the Gamma library and want to test it, you should consider extending these tests which live in `gamma\src\Tests`.

The dynamic project is where PyGamma actually gets created and compiled with Gamma.  There is a step in building the solution where the SWIG program (needs to be in your PATH environmental variable) is run that creates the python.py and pygamma_wrap.cxx source files.  The pygamma_wrap.cxx file is compiled as part of the DLL that the dynamic project outputs (as a file named _pygamma.pyd) and the pygamma.py module contains the Python source code to access the objects in the DLL.

In both the static and dynamic projects, there are Pre- and Post-Build Events (seen in Properties->Build Events->Pre-Build Event, etc.) that help move things along. Like making sure that the 'i686-pc-msvc' directory exists at the top level directory of the gamma hierarchy. And running various Python scripts like write_python_include_path.py, python copy_python_lib.py and post_build.py, that do all sorts of useful moving, copying and creating actions before and after the Build.

In the case of the static project, the Post-Build Event in the 'static\test' sub-project actually automatically triggers the run_tests.py script that we use to confirm the functionality of the Build. It reports test results in the VS 2019 Console window.

For the dynamic project (and subsequent creation of the pygamma module) tests cannot be automatically run because a pygamma wheel has to be created and installed in Python.  Since there may be multiple Python installations, we let the user manually perform these steps. This is generally done using a command line window, changing to the gamma\pygamma directory and running `python setup.py bdist_wheel` command which will create the wheel in the 'dist' subdirectory. Change to the dist directory, run 'pip uninstall pygamma' command to remove any existing version (important if you are not changing the version number) then run `pip install <wheel name>` to install the new pygamma library.  Remember, this will install pygamma into whatever Python installation is 'active' in your command window. I recommend that you use something like the 'miniconda' package manager to organize your different Python environments. Then you can just activate whichever one you want to use to test your new library.

# Summary
## Do once ...
1. Install Visual Studio 2019 (IDE and 2019/2017 compilers)
1. Install [SWIG](http://www.swig.org) (version 4.0.1 - needed for Python 3.x build)
1. Ensure a modern 64-bit Python3 is in your path.
1. `pip install wheel`
1. Check out the PyGamma/Gamma repository

## Do each time you want to Build ...
1. Change Python directory in your PATH variable to reflect the installation for which you are building
1. Run VS 2019
1. Open `gamma\platforms\msvc2017\static\gamma.sln`
1. Clean/Build this solution .. it should report results for QA tests in the Console window after compiling
1. ... assuming no compile or test errors in static build and Gamma C++ tests
1. (optional) C++ tests can also be run manually by changing to `gamma\src\Tests` directory, type `python run_tests.py -v -p ..\\..\\i686-pc-msvc\\`
1. Open `gamma\platforms\msvc2017\dynamic\gamma.sln`
1. Clean/Build this solution 
1. In the `gamma\pygamma` directory, open a cmd window, type `python setup.py bdist_wheel`
1. (optional) In the `gamma\pygamma\dist` directory, type `pip uninstall pygamma` to remove current package
1. In the `gamma\pygamma\dist` directory, type `pip install <wheel name>` to install package
1. Change to `gamma\src\PyTests` directory, type `python ..\Tests\run_tests.py -v `
1. PyGamma test results will print out in cmd window


----


# Notes on How We Developed out Tests and PyTests Process
We needed a simple set of tools for building and running test code, and for evaluating and reporting the success of the results.

It needed to do all of the following:
  * Build Test Code.
  * Run test code and make sure no errors.
  * Compare output files with some verified standard.
  * Compare stdout with a verified standard (golden file).
  * Read and manage input files (for test cases).

## Note on unit testing
  - Evaluated the code in the src/Testing directory. It is basically a testing harness but seemed too complex for our needs.  

  - Also Evaluated 3rd party testing tools.  I was impressed by Google's C++ testing framework, and was also intrigued by CppUnit and CxxTest. If I was going to do ongoing development I would have gone further in this direction, but since we are moving more toward the python world, learning a new testing tool was not a priority at this time.  However, if there is more development work on the C++ version of the code, then one of these, or it's replacement would be worth considering.  Wikipedia has a good listing of C++ unit testing tools: http://en.wikipedia.org/wiki/List_of_unit_testing_frameworks#C.2B.2B