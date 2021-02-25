# Swig Notes
## Details of Current Environment
  * Ubuntu 9.04
  * Swig 1.3.9
  * gcc 4.3.3
  * python 2.5 & 2.6 loaded (including the development options)
  * using for build and run python 2.6.2

## Issues (With C Code)
### Issue 1After swiging, compiling and linking received the following error when loading module into python:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example.py", line 25, in <module>
    _example = swig_import_helper()
  File "example.py", line 24, in swig_import_helper
    return _mod
UnboundLocalError: local variable '_mod' referenced before assignment
```

Solution to this problem (the first time I saw it) was using the following compiler option, "-fno-stack-protector"

gcc -fpic *-fno-stack-protector* -c example.c example_wrap.c -I/usr/include/python2.6 -I/usr/lib/python2.6 

*NOTE*: As of this writing (June 16, 2011) the flag, '-fno-stack-protector' is no longer required to have the build work, including on Ubuntu Linux 9.04, OSX, Solaris, Ubuntu 10.04, and CentOS 5.5. It does not seem a priority to figure our why, especially since we've rearanged the include order of swig ".i" files, changed other Makefile flags and there have also been OS and compiler bug fixes, etc.

### Issue 2
This same error comes back in an unusual circumstance.
  * I have a section of code that I thought would not be included in the swig build since it was separated off using the *#ifndef SWIG* directive.
  * I changed the name of a function so it is different in the regular code versus in the  #ifndef SWIG code.


** Do not do This **:

```
/* example.c */


#ifndef SWIG
#include <stdio.h>
#endif

/* Compute the greatest common divisor of positive integers */
/* changed name to bcd (biggest common denominator) */

int bcd(int x, int y) {
  int g;
  g = y;
  while (x > 0) {
    g = x;
    x = y % x;
    y = g;
  }
  return g;
}

#ifndef SWIG

int main(int arc, char * argv)
{
  /* still called gcd(...) here. */
  printf("%s%d%s", "\n\nThe greatest common denominator or 16 and 156 is ", gcd(16,156), ".\n\n");    

  return 0;
}

#endif

```

The name gcd(a, b) is not defined, but this code should not be included in the compile.  However, it may be included in the swig precompile, so the name gcd(a, b) is pulled in and reported missing.  At least that's my theory ... and getting rid of this code (in alignment with the documentation) fixed the issue.


## Working code for the above environment
example.c:
```
/* File : example.c */
#include <stdlib.h>
#include <math.h>

/* A global variable */
double Foo = 3.0;

double powpow(double a, int b)
{
    return pow(a, b);
}

/* Compute the greatest common divisor of positive integers */
int bcd(int x, int y) {
  int g;
  g = y;
  while (x > 0) {
    g = x;
    x = y % x;
    y = g;
  }
  return g;
}

int toggle()
{
  static int x = 0;
  int y = x%2;

  x += 1;

  return y; 
}
```

example.i:
```
/* File : example.i */
%module example

%{
// These are here so example_wrap.c will compile and link.
#include <stdlib.h>
#include <math.h>
double Foo;
double powpow(double a, int b);
int bcd(int x, int y);
%}

/* these are here so that python knows what to "build a bridge" too */
double Foo;
double powpow(double a, int b);
int bcd(int x, int y);
int toggle();

```

commands to swig, compile, and link:
```
swig -python example.i
gcc -fpic -fno-stack-protector -c example.c example_wrap.c -I/usr/include/python2.6 -I/usr/lib/python2.6 
ld -share example.o example_wrap.o -o _example.so
```

followed by testing:
```
dtodd@dtodd2-desktop:~/dev/test/swig3$ python
Python 2.6.2 (r262:71600, Jul 30 2009, 12:19:12) 
>>> 
>>> import example
>>> 
>>> example.bcd(8, 64)
8
>>> example.bcd(33, 22)
11
>>> example.toggle()
0
>>> example.toggle()
1
>>> example.toggle()
0
>>> example.cvar.Foo
3.0
>>> example.cvar.Foo = 5.53
>>> example.cvar.Foo
5.5300000000000002
>>> 
>>> example.cvar.Foo = 5.5
>>> example.cvar.Foo
5.5
>>> example.powpow(3,4)
81.0
>>> 
```

## Issues (With C++ Code)
After doing a link in C++, and then trying to load into python, I got the same "_mod" error.

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example.py", line 25, in <module>
    _example = swig_import_helper()
  File "example.py", line 24, in swig_import_helper
    return _mod
UnboundLocalError: local variable '_mod' referenced before assignment
```

After changing my code to target python 2.5, I got a slightly different error...

```
>>> import example5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example5.py", line 28, in <module>
    import _example5
ImportError: ./_example5.so: undefined symbol: __cxa_guard_acquire
```

So I added more diagnostic codes to the compile and link code and it appears that during the link process, not all the symbols were getting resolved:

e.g.
```
....
example5_wrap.o: In function `SWIG_UnpackDataName':
example5_wrap.cxx:(.text+0x4224): undefined reference to `strcmp'
example5_wrap.cxx:(.text+0x4242): undefined reference to `memset'
example5_wrap.o: In function `SWIG_PackVoidPtr':
example5_wrap.cxx:(.text+0x42c6): undefined reference to `strlen'
example5_wrap.cxx:(.text+0x42f7): undefined reference to `strcpy'
example5_wrap.o: In function `SWIG_Python_FixMethods':
example5_wrap.cxx:(.text+0x4340): undefined reference to `strstr'
example5_wrap.cxx:(.text+0x4399): undefined reference to `strlen'
example5_wrap.cxx:(.text+0x43c7): undefined reference to `strncmp'
example5_wrap.cxx:(.text+0x445e): undefined reference to `strlen'
example5_wrap.cxx:(.text+0x4477): undefined reference to `malloc'
example5_wrap.cxx:(.text+0x44d4): undefined reference to `strncpy'
example5_wrap.cxx:(.text+0x44f5): undefined reference to `memcpy'
example5_wrap.o: In function `init_example5':
example5_wrap.cxx:(.text+0x459b): undefined reference to `Py_InitModule4'
example5_wrap.cxx:(.text+0x45a9): undefined reference to `PyModule_GetDict'
example5_wrap.o:(.rodata+0x788): undefined reference to `PyObject_GenericGetAttr'
example5_wrap.o:(.eh_frame+0x12): undefined reference to `__gxx_personality_v0'
```

Apparently, using g++ instead of ld at link time solves the issue, but it is unclear to me at this time (08/07/09) why this is.  Still researching this.  But I got a hind from searching the we on various SWIG issues...

e.g. here is one such comment:

  Ok then, how does gcc/g++ work?

  Ok. Basically, you invoke the compiler by typing "gcc" or "g++", and make it do those special compiler things (or specifically, restrict it to only do part of it) by giving gcc or g++ an argument.

  A quick, but important note: You have to use "gcc" to build C programs and "g++" to build C++ programs. *The whole suite is called GCC, and there's even a slightly misleading note in some documentation saying that "gcc" should be able to build C++ programs by the file extension, but you need to use g++. Trust me on this.*



_My (DCT) find on this is that using gcc at compile time works, but we need to use g++ at link time._

I'll mock this up to more SWIG magic (for now).


### Here is a working C++ example:
// Header file:

```

/* basic_class.h */
#ifndef _BASIC_CLASS_H_20090806
#define _BASIC_CLASS_H_20090806

class BasicClass
{
public:
    BasicClass();
    BasicClass(int startCount);
    int CurrentCount();
    void Increment();
    ~BasicClass();

private:
    int m_Counter;
};

#endif

```


".cpp" file:


```

/* basic_class.cpp */

#include "basic_class.h"

BasicClass::BasicClass()
    : m_Counter(0)
{
}

BasicClass::BasicClass(int startCount)
    : m_Counter(startCount)
{
}

int BasicClass::CurrentCount()
{
    return m_Counter;
}

void BasicClass::Increment()
{
    m_Counter++;
}

BasicClass::~BasicClass()
{}

```

".i" file:

```

/* File : basic_class.i */
%module example5

%{
#include "basic_class.h"
%}

class BasicClass
{
public:
    BasicClass();
    BasicClass(int startCount);
    int CurrentCount();
    void Increment();
    ~BasicClass();
};

```


Using the following commands (note: these were designed to give a lot of output to see what's going on):


swig -c++ -copyctor -Fstandard -nocpperraswarn -v -Wall -python example5.i

gcc -shared -Wall -ansi -fuse-cxa-atexit -fno-stack-protector -c basic_class.cpp example5_wrap.cxx -I/usr/include/python2.6 -I/usr/lib/python2.6 

g++ --fatal-warnings --no-undefined --no-allow-shlib-undefined --unresolved-symbols=report-all --verbose -shared basic_class.o example5_wrap.o -o _example5.so


NOTE:  the name of the ".i" file is not that important as long as you use the right directives in the swig, gcc, and g++ command.  The final linker output (called _example5.so in this case) needs to be connected with the name of the module, as given in the directive "%module example5", in the ".i" file.  

This example can be loaded in python 2.6 as follows (To use python 2.5 just change the "python2.6" in the gcc command to "python2.5"):

```
dtodd@dtodd2-desktop:~/dev/test/swig5$ python
Python 2.6.2 (r262:71600, Jul 30 2009, 12:19:12) 
>>>
>>> import example5
>>>
>>> x = example5.BasicClass()       
>>> x.CurrentCount()
0
>>> x.Increment()
>>> x.CurrentCount()
1
>>> x.Increment()
>>> x.Increment()
>>> x.Increment()
>>> x.CurrentCount()
4
>>> y = example5.BasicClass(205)
>>> y.Increment()
>>> y.Increment()
>>> y.CurrentCount()
207
>>>  
```



