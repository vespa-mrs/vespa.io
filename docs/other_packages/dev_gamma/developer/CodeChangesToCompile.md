# Compiling Gamma
This page is for documenting changes made to Gamma code (circa July 2009) so it will compile in the following environments:
  * gcc 4.3.3 on ubuntu 9.04
  * gcc 4.0.1 on Mac 0SX
  * visual studio, windows 2008 express


## 1.  Compiling for Windows
Using Visual Studio 2008 express, got some windows specific issues to deal with (see (a) below), and some non-windows-specific (item (c)), and also it caught infinite loops that might not have been caught by gcc (item (b)).

### a. Added #ifdef _MSC_VER for some windows specific complaints
e.g. 

```
  #ifdef _MSC_VER
  // Need to confirm this has no effect on results.
  return _hypot(z.re, z.im); 
  #else
  return hypot(z.re, z.im);
  #endif  
  }
```

and

```
#ifdef _MSC_VER
	sprintf_s(buffer, 200, "%d", i); 
#else
	sprintf(buffer, "%d", i); 
#endif
```

### b. Infinite loop correction and disabling
Windows caught three cases where entry into a function would never exit and overflow the stack.

In one case I was able to correct the issue, as it was pretty clear what was happening.  In another case I could not find an obvious fix, but the code was not being used, so it was commented out.  In the third case I was not able to fix or comment out (2 aformentioned remedies), but it was in a directory called "Deprecated", so I added code that was windows specific (#ifdef _MSC_VER) that prints out a warning, and then exits.

i.e., in block_1D.cc
```
#ifdef _MSC_VER
	// *DCT* This call leads to infinite recursion and will not compile on windows.
	cout << "\nFATAL: Call to this deprecated funtion leads to infinite recursion.\n";
	assert(0);
#else
	BLK.row_vector::operator= (-BLK1);	// vector negation
  BLK.ParameterSet::operator= (BLK1);		// copy parameter set BLK1 into BLK
#endif
```

### c. Variable type changes
This was typically required for pow( , ) and sqrt().  pow() takes a floating point (or double) and then an int (or long) and sqrt() takes a float or double.  In many cases where floating point numbers were expected, it was being passed integer types.  

2 solutions.  

i. If it was a simple case of a numeric value, it was just cast as a double or float.

e.g. pow(10, 2) or  pow(long(10), 2) changed to pow(double(10), 1), etc.

ii. If it was a variable type, it was cast to a double or a float.

```

  const double SUPEROP_EPSILON = 0.000001;

  int LSp = mx.rows(); /* mx.rows(), an integer */

  int HSp = static_cast<int>(sqrt(static_cast<double>(LSp)) + SUPEROP_EPSILON); 
  
  Hbs = basis(HSp);    // Set Hilbert space basis to default

```

The 0.000001 was added to handle potential rounding issues before casting back to an int.

Reviewed the use of magic numbers (0.1, .000001) in HSdecomp.cc and SuperOp.cc (HSLib and LSLib), and then changed from .1 to 0.000001 to SUPEROP_EPSILON in SuperOp.cc.  Did something similar in HSdecomp.cc.

In a few special cases the result had to be cast as it's result was used in other calculations, or the required value of the input was not clear.

In the case listed below the input was being cast to a long, which might have side effects, so the long cast was kept and was in turn cast to a long double, and the result recast back to a double.

e.g. 
```

  // FIXME if needed **** i.e. Are two static_casts<>() really needed.
  for(int i=1; i<FMCP.steps; i++)   // Calculate extremum
      extremum += static_cast<double>(pow(static_cast<long double>(long(FMCP.CLM)),int(i-1))*FMCP.CLI);
  if(extremum<FMCP.dmin)            // Insure it isn't less than min
      extremum = FMCP.dmin;         // Insure it isn't less than min
         
```


## 2. Removed extraneous class specifiers from header files.
e.g.
```
Class Foobar
{
    // Foobar:: is extraneous here.

    Foobar::Foobar();
  
    Foobar::GetFoo();

    Foobar::SetFoo(std::string a);

    Foobar::~Foobar();
};
```
Changed to:
```
Class Foobar
{
    // Ah, better.

    Foobar();
  
    GetFoo();

    SetFoo(std::string a);

    ~Foobar();
};
```
## 3. Added header file <stdlib.h>, and <math.h> to some ".cc" files
If the .cc files used any of the following function, then it needs to include stdlib.h:

  * abs()
  * atof()
  * atoi()
  * exit()
  * system()

and math.h for:

  * pow()
  * sqrt()

## 4. Changed how friend functions were declared
In many classes there were friend functions defined in some secondary class, but not declared separately.  I believe the older compilers treated the friend definitions/declarations as function declarations, but not in gcc 4.3.3.  

It's not clear how many of these functions even have any business being friend functions of the classes in which they are included, but I did not try to investigate and simplify this issue. It's there to be tackled on a second round of inspection and coding.

### a.In many cases this was solved by adding a separate declaration - with the function signature - outside the class. Then just removing any duplication of default values for variables.

e.g. In header it might have,

```
/* foo.h */
class Foo
{
   Foo();
   int GetNextFoobar();

   friend double propagate_foo_bar(int foo, double bar = 1.0);
   ~Foo();
}
```
With associated function definitions in Foo.cc

This let to compiler errors that were fixed as follows in foo.h:

```
/* foo.h */

/* put default initializer in this declaration */
double propagate_foo_bar(int foo, double bar = 1.0);

class Foo
{
   Foo();
   int GetNextFoobar();

   /* removed default initializer from here */
   friend double propagate_foo_bar(int foo, double bar);
   ~Foo();
}
```

### b.In one case there was so much confusion because the function name was so overloaded, that I created a new class called Evolve.  The functions from this class were all defined as static and can be called using the Evolve::evolve() or Evolve::prop() style format.  This had other benefits, as it revealed linker issues on the Mac OSX that were not seen on gcc 4.3.3 on Linux.

## 5. Converted "File *" to "ifstream"
See GgnuPlot.cc for an example in function:
  * string GPFind(bool vocal)



