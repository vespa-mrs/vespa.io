# Merging our code base with that received from Matthias Ernst in Zurich
## Just prior to code integration
Code revision in SVN just prior to beginning the merger process was 67.
```
r67 | dtodd | 2009-10-29 11:23:49 -0700 (Thu, 29 Oct 2009) | 9 lines
```

## After completing code integration & Linux test integration
Code Revision in svn was at 116.

## Pre-merger code differences
Overview and samples of file diffs between our code and Matthais' code:

```
A few files have had their names changed by Matthais.
The new names are more oriented toward consistency of naming style.

I added or moved declarations of functions that were originally friend declarations. 
They were moved outside of the class definitions.

I moved evolve and prop functions out of HSprop and into a new Evolve class.

Matthais changed long to int32_t in a few classes.
(I assume Matthias' includes <stdint.h> somewhere)
Note: this is not officially supported in visual studio 2008, but can be accommodated.

Matthais removed support for older versions of the gcc compiler.

I made many changes for compatibility with windows:
This include adding "#include <stdlib>"  
AND 
numerous #ifdef _MSC_VER 
... to many files.

Matthais' moved many of these functions into the class definition.
Spin_T_fatality() --> Spin_T.Spin_T.fatality(), etc.

I removed unnecessary class specifications (WBRExch::) from
the header files in which the class was defined.
WBRExch::ask_relax() --> ask_relax()

There seemed to be some logic changes in matrix.h/cc
Mattais changed for instance:
blockDiag = true --> blockDiag = false

In n_matrix.cc/h, Matthais' included many changes, including logic changes.

Also, in h_matrix.cc/h, the following change:
< virtual std::vector<int> BlockDiag(_matrix*    (&BD), std::vector<int> &U); // Matthais'
---
> virtual std::vector<int> BlockDiag(_matrix*    (&BD), _matrix* (&U));  // Scott's old code.

I changed float to double in d_matrix.cc (write commands)

Changes in sys_dynamic.cc and multilib.cc, multiexchange.cc

I added new functions to TTable.cc and row_vector for testing.

I removed "CoordFrame::" from class definitions as it caused issues on OSX (discussed above)

Ovserved some variable name changes
e.g. in IntDip.cc 
II ---> ii
DS --> DSc
SS --> ss

Matthais made significant changes to XWinFid.cc

```

## Finished First Pass of Code Integration
Accomplished at Revision 100.
Currently, on Linux, our test suite (with 7 tests) has no errors.
On Windows we have one issue with one of the tests, an error in rounding of a number in the 5th (or 6th) decimal place.

List of significant integration issues/changes, etc.
The context is the NCIRE(VA-UCSF)/DUKE library Versus the Zurich (Matthais) Library.

Changes:

  - Included zurich changes to BlockDiag(...) method in matrix classes.
  - Include Zurich logic changes in SpinOpCmp.cc
  - Changed (our) code to include the int32_t declarations, and to make the required header file available to windows users.  Currently the header (stdint.h) comes with gcc (e.g. 4.x), but does not come with visual studio (as of version 9, aka visual studio 2008).

  - Kept in <stdlib.h>, <math.h>, etc. for windows compatibility.
  - Omitted extra (and hopefully unnecessary) 'extern' declarations.
  - A number of header files in the Zurich code contained methods declared as Class::method().  The extra 'Class::' specification is not needed, and upset the compiler on the MAC OSX platform and so they were omitted.
  - In SuperOp.h/.cc: 
    - [1] changed declarations of the form 'void operator*=' to  'SuperOp & operator*='. both forms seem to give the same result in C++, but the latter form is currently the preferred form.  Also, only the latter form gives the proper result when exporting this interface to python.  
    - [2] Kept in my rounding issue changes to make sure the sqrt of an int was the right int (e.g. sqrt(9) = 3).  
    - [3] Incorporated Zurich's bug fixes to d_commutator() and to CheckLOp().

  - Added new method declarations outside of a class, in cases where there method was declared as a friend within the class.  Otherwise, on some platforms, these methods would not be visible outside the class.
  - Uncommented 'ask_Dante()', etc, and omitted the declarations for WF_DANTE, CP_DANTE, and PT_DANTE.
  - Changed float to double, in the IO of h_matrix (i.e. the read and write routines).
  - Changed variable names between our two code bases in a few classes. e.g. ss <--> SS.
  - Kept in our windows changes for compatibility, e.g. with sprintf_s, _hypot, localtime_s, _j0, etc.
```
#ifdef _MSC_VER
    sprintf_s(...)
#else
    sprintf(...)
#endif
```

  - In IntRank2.cc, commented out method that could cause infinite recursion, but not called by any other classes.
  - In Level1/coord.h, added Rmx( .., .., ..) declaration outside of class to augment friend declaration.
  - Omitted changes to Spin_T class to make certain functions into member functions, as it was not necessary. e.g. spin_T_error() <--> Spin_T::spin_T_error().
  - Removed lines from Basics\Gutils.cc that have comments '//clear out any linefeeds' in agreement with zurich's code.  Found these lines were not needed.
  - Kept in a new definition for Kex, with the signature Kex(int, int, double) in sys_dynamic.
  - Changed File* to ifstream in GamIO/FrameMaker.cc
  - RelaxBWRexch.cc/.h, Omitted the Zurich changes of converting friend functions into class member functions as not needed, and also these functions did not make sense as part of the class.
  - Removed RelaxAux.h/.c from the build and Visual Studio project as this class no longer contained any functioning code.
  - Removed some buggy code from GenOp (from svn diff -r 95 GenOp.cc):
```
   if(!WBR) { *this = -Op1; return; }   // If No Op, result is -Op1
-    {
-    *this = -Op1;
-    if(Op1.OpName.length())
-     name("Negated " + Op1.OpName);
-    return;
-    }
```

  - FrameMaker.cc, kept in my windows enhancements sprintf-->sprintf_s, and my modifications to change File* to ifstream in FMFind().  Removed the double casts that I had previously added - as they no longer seem to be required.
  - In ML5Tag.cc/.h: moved definition of isBigEndian() into header, made it a const function, and call it using the this->isBigEndian() convention.

 




