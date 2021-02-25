# Implementation Details for Swigging gamma

## Swig code organization
Created a *pygamma.i* file in gamma/trunk/src that includes ".i" files from all the sub-directories that have swig conversions.  Each subfolder.i file (e.g. basics.i) contains a listing of all the files for which their are swig conversions.

pygamma.i is shown here:

```
%module pygamma

%include "Basics/basics.i"
%include "HSLib/hslib.i"
%include "LSLib/lslib.i"
%include "Level2/level2.i"
%include "Matrix/Matrix.i"
%include "Pulses/pulses.i"
```

hslib.i in the HSLib subdirectory looks like this:

```
%include "SpinSystem.i"
%include "SpinSys.i"
%include "GenOp.i"
%include "HSham.i"
%include "SpinOpCmp.i"
%include "HSauxil.i"
%include "PulseI.i"
%include "Basis.i"
%include "HSprop.i"
%include "SpinOp.i"
```

and the .i files have this basic look and feel:

```
/* SpinOp.h */
// Swig interface file.

%{
#include "HSLib/SpinOp.h"
%}

%include "std_string.i"

%rename(__add__)  complex::operator+;
%rename(__iadd__) complex::operator+=;
%rename(__isub__) complex::operator-=;
%rename(__neg__)  complex::operator- ();

%rename(__imul__) complex::operator*=;
%rename(__idiv__) complex::operator/=;

class spin_op 

{
public:

spin_op();

spin_op(const spin_op& SOp);
~spin_op();

//...

};

```

### A few notable features
1. The renaming of the overridden function to their python values,
```
%rename(__add__)  complex::operator+;
```
so that they work as expected in python.

2. The inclusion of the swig header for the stl libraries that are involved in the public functions so that stl classes can be "created" in python and used in these methods and also so that some obvious (or semi-obvious) translations can be made in the python to C++ boundary.
```
%include "std_string.i"
```
### Issues to be looked into a bit more
I observed an odd issue with code that worked in C++ but not in python.

The overloading of certain operators with this format worked in C++, but did not behave as expected in Python.
```
(a)
void operator +=
void operator *= 
```
When it was rewritten as:
```
(b)
object & operator +=
object & operator *=
```
it worked in both C++ and Python as users would expect.

As of this writing (11/10/09), this was implemented for SuperOp.h/.cc/.i (in LSLib), but there may be some places where this was not yet implemented.


## Makefile changes
For SWIG, we first need to create one or more new source wrapper files (e.g. .cxx file) from the ".i" files.
To do that, we issue a command like this:

```
swig -c++ -python pygamma.i
```

In our case, this is all that is required, since the pygamma.i file includes all the other ".i" files.

### Linux
In a Linux makefile this simple command translates into this:

```
PYSG_WRAP_SRC = $(addprefix $(BINDIR)/, pygamma_wrap.cxx)
PYSG_WRAP_SRC1 = $(addprefix $(BINDIR)/, pygamma.py)

PYSG_WRAP_SRCS = $(PYSG_WRAP_SRC) $(PYSG_WRAP_SRC1)
PYSG_WRAP_OBJS = $(addprefix $(BINDIR)/, pygamma_wrap.o)

# If add a new .i file, it needs to be added to gamma/trunk/make/Makemods
# You'll see examples there of how to do this.

OTHERDOTIFILES = $(addprefix $(SRCDIR)/, $(ALLIFILES))

$(PYSG_WRAP_SRC) : ${SRCDIR}/pygamma.i $(OTHERDOTIFILES)
	@echo
	swig -c++ -python -outdir $(BINDIR) -o $@ \
         -I../../src $<
```

There is a note in this block of "code" about "Makemods".  That is currently where all the source code listings are located.

The generated *_wrap.cxx code is then compiled using similar techniques as those used by the .cc files:

```
$(PYSG_WRAP_OBJS) : $(PYSG_WRAP_SRC)
	gcc -c $(PYSGCPPFLAGS) $(PYSG_WRAP_SRC)  \
         $(PYSINCFLAGS) -o $(PYSG_WRAP_OBJS)
```

This is then linked into the pygamma.so library as follows:
```
${BINDIR}/$(PYS_NAME): $(PYSG_OBJS) $(PYSG_WRAP_OBJS) $(PYSGAMMA_CHK) 
	@echo
	@echo "Making PYSGAMMA Shared $(PYS_NAME) From Pythonized and Swigged Object Files"
	@echo
	g++ ${PYS_LDFLAGS} -o ${BINDIR}/${PYS_NAME} $(PYSG_OBJS) $(PYSG_WRAP_OBJS) $(PYS_LDLIBS)
```


### Macintosh OSX
Similar techniques are used on the Macintosh OSX

### Windows
For windows, we add a pre-build command to create the SWIG wrapper source file from the .i file.

In the project properties panel:

Select the "Pre-build Events", listed under "Build Events", which is under "Configuration Properties".
```
+Configuration Properties
+Build Events
-->Pre-Build events
```

The command is listed in "command line" field
```
command line:  swig -c++ -python -outdir ..\..\i686-pc-msvc  -I..\..\src -o ..\..\i686-pc-msvc\pygamma_wrap.cxx pygamma.i 
```
The generated output file name (pygamma_wrap.cxx) is added as a required source for the project, and is thus compiled and linked in.

