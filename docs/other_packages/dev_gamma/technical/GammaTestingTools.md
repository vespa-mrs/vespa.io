# Gamma Testing Situation
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

## Test Directory and Organization
### Overview
Created a new sub-directory of /src called "Tests", with a subdirectory called "golden".
Created a script to run the test code, and compare the results with the results listed in the golden directory.
Then modified Linux Makefile, and visual studio project to build the test code and call the script.

### Linux
```
# New Test routines

test:  ${BINDIR}/${LIB_NAME}  $(BINDIR)/runtests  run

TESTS       = Tests

TESTSBASE   = testsuite runtests

TESTSHDR    = testsuite.h



TESTCCFILES += $(addsuffix .cc, $(addprefix $(TESTS)/, $(TESTSBASE)))

ALLHFILES  += $(addprefix $(TESTS)/, $(TESTSHDR))

TESTOBJFILES  += $(addsuffix .too,  $(addprefix $(BINDIR)/, $(TESTSBASE)))


CPP_TESTFLAGS = -Wall $(SRCDIRINCL_FLAG) -DGSTATIC=1 
CXX_TESTFLAGS = 
LD_TESTFLAGS = 

${BINDIR}/%.too : ${SRCDIR}/${TESTS}/%.cc

	$(CXX) -c $(CPP_TESTFLAGS) $(CXX_TESTFLAGS) $< -o $@

$(BINDIR)/runtests : $(TESTOBJFILES)
	$(CXX) -static -o $@ $(LD_TESTFLAGS) ${TESTOBJFILES} -L${BINDIR}/ -lgamma 

RUNDIR = ./../../src/Tests
CURDIR = ./../../primal/Linux

run: force
	@echo 
	@echo Running tests:
	@echo
	@cd $(RUNDIR); python$(PYVERSION) run_tests.py -v -p $(BINDIR)/; cd $(CURDIR)
	@echo 
```

### Windows
The modifications on windows involved adding the script as a "Post-Build Event" to the test project, which was included in with the 'static' gamma visual studio 2008 project:

```
cd ..\..\src\Tests
python run_tests.py -v -p ..\\..\\i686-pc-msvc\\
cd ..\..\msvc2008e\test
```


### Test script
Test script was written in python for portability, and is called:
*run_tests.py*

...and is now part of the svn repository.









