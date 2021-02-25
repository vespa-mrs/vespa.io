# Extending PyGAMMA
PyGAMMA was built using SWIG.

While the SWIG interface and methodologies (www.swig.org) can take a while to learn, a simple way to make modifications it always to copy what has already been done. This is a brief tutorial and quick start-up guide in using swig for python - as applied to the GAMMA/PyGAMMA project.

Below is a case study, and a simple cheat sheet for Swigging files. 

## Case Study
It was uncovered that 3 methods were not available in pyGamma (i.e not available from Python after importing pygamma):
  * Sxpuls
  * Sypuls
  * Sxypuls

These methods were located in the file PulseS.h/.cc which had not been swigged yet. To see if a file was swigged, check for a file with the same root name and with the extension ".i".  For example "PulseS.i".  Since it did not exist, it was not swigged.

*Here is my step by step process for Swigging GAMMA files:*

  * First check the file make/MakeMods and confirm that the file you are about to SWIG is included in the build process. If it is not, you will be wasting your time (unless it's a new file that needs to be added to the regular build process).

  * Open the .i and .h file for some previously swigged files (e.g. src/HSLib/GenOp.i and src/Basics/SinglePar.i), and use these as examples.

  * Copy the PulseS.h file into PulseS.i.

  * Change the file name in the comment field at the very top of the file to PulseS.i

  * Add this comment on the second line (i.e. just below the '/* PulseS.i */'),
```
// Swig interface file.
```
  * For any STL imports, e.g. vector.h, string.h, etc., '%import' a similarly named ".i" file like this:
```
%include "std_vector.i"
%include "std_string.i"
```
  * Replace all the remaining ".h" header files, e.g.
```
#include <GamGen.h>			// Know MSVCDLL (__declspec)
#include <HSLib/SpinSys.h>		// Know about base spin systems
#include <Matrix/matrix.h>		// Know about matrices
```
  with a statement like the one below. This will pull-in all the header files that PulseS.h imported.
```
%{
#include "HSLib/PulseS.h"
%}
```
  * Remove all #ifdef's, #ifndef, stuff, near the top of the file - i.e. remove this kind of stuff:
```
#ifndef SpinOp_h_			// Is file already included?
#  define SpinOp_h_ 1			// If no, then remember it
#  if defined(GAMPRAGMA)		// Using the GNU compiler?
#    pragma interface			// This is the interface
#  endif
```
  * Remove most of comments as they will still exist in PulseS.h, and keeping them will create a double maintenance problem. Note: Functions that are already commented out, but are not obviously junk, I have been changing the comment from "//" to "///". This way, when I comment out stuff for other reasons in the ".i" file, the pre and post swigging commented-stuff can be distinguished.

  * Remove any Microsoft specific function defintion prefixes, e.g. "MSVCDLL". 
    So this:
```
MSVCDLL gen_op SxpulsB(...)
```
    would be replaced by this:
```
gen_op SxpulsB(...)
```
  * Remove any precompiled code (usually at the end of the file) regarding PYGAMMA, as in this:
```
#ifdef PYGAMMA 
    // Declare something
#endif
```
  This is a previous implementation of PYGAMMA and swig will not need this.

  * At the beginning of the file, add the 'rename' statement appropriate for each _operator_ function defined in the .i/.h file (like "operator+") so they will work in Python, e.g.:
```
%rename(__add__)  complex::operator+;
```
  This will allow python to recognize the "+" operator in C++ as the addition operator (i.e. "+") in Python.

  * Here is a partial list of override functions (for the class gen_op):
```
%rename(__add__)  gen_op::operator+ const;
%rename(__iadd__) gen_op::operator+=;

%rename(__sub__)  gen_op::operator- const;
%rename(__neg__)  gen_op::operator-() const;
%rename(__isub__) gen_op::operator-=;

%rename(__mul__)  gen_op::operator* const;
%rename(__imul__) gen_op::operator*=;
%rename(__idiv__) gen_op::operator/=;

%rename(__iand__) gen_op::operator&=;

%rename(__eq__)  gen_op::operator== const;
%rename(__ne__)  gen_op::operator!= const;
%rename(__lt__)  gen_op::operator<  const;
%rename(__gt__)  gen_op::operator>  const;

%rename(__assign__) gen_op::operator=;
```
  A complete list is included [here](/wiki:SwigOperatorRenaming/).

  * Friend functions can be problematic, so by default I usually comment them out (in some cases they were deleted - so look at the .h file if you want to try and convert them to Python). However, many of them can be moved outside the class and have the friend classifier removed (and still work).

  * Methods that refer to a stream (return values or input) are commented out, as I'm not up to speed on how to handle them and don't think we need them anyway (so far we have not). Generally we'd want to handle the IO in the native language.

  e.g. comment out this type of function:
```
std::ostream& printBase(std::ostream &ostr) const;
std::ostream& print(std::ostream &ostr, int full=0) const;
```

  * Here are some special considerations when dealing with operator functions. In some cases the semantics of C++ and python differ. In particular if you are trying to overload a function of a class that implements the "operator*=", "operator+=", or "operator=", etc.  
  In C++, these functions modify the initial variable you are applying it to, e.g. the B in "B += 5".  However in Python, B becomes a reference to the new object that is returned after 5 is added to B. So the return value is ignored in C++, but matters a lot in Python. 

  Many of these types of functions were written, in GAMMA, as "void operator +=", etc. It is now generally accepted that one should use something like this "MyObject & operator += ". However, in C++ this form is not necessary for proper behavior. Of course hind-site is always 20/20. So when swigging this type of function - with the older semantics - it is necessary to make changes to the *.h and the .cc* files in order to return a reference to an object. 

  Besides changing 'void' to 'MyObject & (.i, .h, and .cc), you will also have to have the function in the .cc file return '*this'. For example, in the .cc file...

  e.g. Change this:
```
void gen_op::operator *= (const complex& z)
{ 
    if(WBR) 
    { 
        setOnlyWBR(); 
        WBR->RepMx *= z; 
    } 
}
```
  To this:
```
gen_op & gen_op::operator *= (const complex& z)
{ 
    // This section remains the same...
    if(WBR) 
    { 
        setOnlyWBR(); 
        WBR->RepMx *= z; 
    } 

    // Add this code...
    // Dereference the "this" pointer, and return it.
    return *this;
}
```
  and change this:
```
void PulWaveform::operator = (const PulWaveform& PWF1)
{
  WFsteps = PWF1.WFsteps;		// Copy the number of steps
  WFname  = PWF1.WFname;		// Copy pulse waveform name
  WFtp    = PWF1.WFtp;			// Copy pulse waveform length
  WFvals  = PWF1.WFvals;		// Set PT waveform steps
  WFtimes = PWF1.WFtimes;		// Set PT waveform step lengths (sec)
  rad     = PWF1.rad;			// Copy the radians flag
}
```
  to this:
```
PulWaveform& PulWaveform::operator = (const PulWaveform& PWF1)

{
  // Keep this section the same...
  WFsteps = PWF1.WFsteps;		// Copy the number of steps
  WFname  = PWF1.WFname;		// Copy pulse waveform name
  WFtp    = PWF1.WFtp;			// Copy pulse waveform length
  WFvals  = PWF1.WFvals;		// Set PT waveform steps
  WFtimes = PWF1.WFtimes;		// Set PT waveform step lengths (sec)
  rad     = PWF1.rad;			// Copy the radians flag

  // Add this code...
  // Dereference the "this" pointer, and return it
  return *this;

}
```

  * Include this new file "PulseS.i" in the file called "hslib.i" located in the same directory, using the %include directive. hslib.i is included in pygamma.i (located in the gamma/trunk/src directory), and by virtue of %include process, is included in the swigged code. In general, there will be a file in each src directory with an all lower case name equal to the directory name with a ".i" extension. If that name is used already, then there should be (or you should create) a file, all lower case, with the name <directory-name>_inc.i  with the "_inc.i" indicating it is and include file. For the case being discussed in this example, the following code would be added to hslib.i:
```
%include "PulseS.i"
```

  * Add the prefix name of the new .i file (e.g. "PulseS" for PulseS.i ) to the file called MakeMods (in gamma/trunk/make) in the section/line with the list called <directory>_IBASE (e.g. HSLIB_IBASE) if it exists. If this section/line does not exist then create a new one for your directory: See an example of BASICS_IBASE. This procedure will have it included in the list called ALLIFILES (i.e. that's ALL-I-FILES).

  * You should re-build PyGAMMA and make sure there are no syntactical errors, e.g. "make pysg" on Linux. Note, any error with the *pygamma_wrap.cxx* file is probably one that was caused by your changes - as this is the file that swig will create from all the ".i" files. If you see an error with this file, you will need to look at what caused it. For example, you might get a syntactic error if you forgot to remove the MSVCDLL style descriptors at the beginning of functions.

  * Before checking all your changes into subversion (e.g. after swigging a few files), do the following:
    * Rerun the tests (e.g. on Linux, in the build directory, type "make test") and make sure you didn't break anything!
    * Then [PyGamma#BuildingPyGAMMA build PyGAMMA for an install] (e.g. "make pysgdist"). and [PyGamma#InstallingPyGAMMA install pygamma] (e.g. go to gamma/pygamma and run "sudo python setup.py install"). With pygamma installed you can start up a python session and make sure you can "import pygamma as pg". If this fails, it will probably give an error indicating that a symbol was undefined, like this:
```
>>> import pygamma as pg
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.6/dist-packages/pygamma/__init__.py", line 15, in <module>
    from pygamma import *
  File "/usr/local/lib/python2.6/dist-packages/pygamma/pygamma.py", line 7, in <module>
    import _pygamma
ImportError: /usr/local/lib/python2.6/dist-packages/pygamma/_pygamma.so: undefined symbol: _Z7acquireR6gen_opS0_R6HSpropid
```
    This implies that a function that was defined in the ".i" (and ".h") file could not be found in the ".cc" file. The text "_Z7acquireR6gen_opS0_R6HSpropid" is the mangled C++ function name. To try and resolve this issue, take a look at the function signatures and make sure that the declared function was also defined, by looking at the .cc file. While swigging GAMMA, I found numerous instances of functions of this nature (declared in the .h file, but not defined in the .cc file).
    Solutions:
      * 1) You can comment out the undefined function from the .i and the .h files. 
      * 2) You can define the missing function if it seems clear how to do that.

    * Finally, after importing pygamma into Python try to create a simple object from pygamma [e.g. complex(1,2)] and if possible, one from your class..., and make sure it works.

  * Add the new file (e.g. "PulseS.i") to subversion and check in.

## See Also
[GammaSwigImplementation Additional notes on Swigging GAMMA]