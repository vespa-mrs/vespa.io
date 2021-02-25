# Coding Standards - General Comments
```
#!rst

#### ========Coding Standards
#### ========

About
-----
Coding standards are one part of a development protocol. Other parts include
unit testing and code reviews. This document covers only coding standards.


Why?
--------------------------

Following a coding standard is like handwashing in a hospital:
both require discipline. Following the
protocol takes more time than ignoring it, and it's pretty difficult to
associate a particular negative incident (disease transmission or a software
bug) with a particular instance of failing to follow the protocol. 
Nevertheless, every incidence of corner-cutting increases the
probability of a bad outcome somewhere down the line.

Development protocols attempt to avoid bad outcomes by reining in software
complexity. Entropy kills projects, and the Second Law of Thermodynamics is as
true in the software world as it is in the natural world. Perhaps you've heard
the maxim that the first 90% of a project takes 90% of the time and the last
10% takes the other 90% of the time. That doesn't have to be true, but it
often is. On some projects, that last 10% of development is like a game of
whack-a-mole. Smack a bug here, another pops up there.

In fact, if a project is messy enough the last 10% never gets completed. All
effort gets sucked into fixing bugs and inadvertently creating new ones.
Eventually one faces the choice of shipping something that's only 90% complete
or not shipping at all.

Those are some really bad outcomes. They can be avoided, but only by deliberate
action. **The only thing you get without effort is entropy.**

That said, here's the most obvious pressures on this project that call for
software development rigor.

- This project is being written by a team of 4+ people who are across the 
  country from one another.

- Only one of them is strong in the project's primary language (Python).

- This project will subsume GAVA, Vespa and Matpulse. Software complexity
  usually grows exponentially in relation to size, so this project's complexity
  will exceed not only the individual projects but also the *sum* of the
  individual projects. That's a lot to manage!

- A larger project needs a long lifespan to justify the effort put into it,
  and a longer lifespan increases the odds that (a) someone totally new will
  join the project and need to understand the code and (b) the code will need 
  to be modified and/or expanded in the future.

- The more people involved, the greater the odds that others will read, use
  and modify code that you write.

- The end result needs to be clean enough to encourage outsiders to
  contribute.


Words of Wisdom from the Masters
--------------------------------

  "Controlling complexity is the essence of computer programming."
  
  -- Brian Kernighan

  "Let us change our traditional attitude to the construction of programs: 
  Instead of imagining that our main task is to instruct a computer what to 
  do, let us concentrate rather on explaining to human beings what we want a 
  computer to do."
  
  -- Donald Knuth

  "Readability counts." 
  
  -- Tim Peters in PEP 20.

This last quote is about design (aircraft design, actually) rather than code, 
but it is one of my favorites.

  "It seems that perfection is reached not when there is nothing left to add, 
  but when there is nothing left to take away". 
    
  -- Antoine de Saint Exupery


It's Not About You
--------------------

The guidelines below are intended to help you write code that's easier 
for others to work with. They're not about making *your* life easy.
If you think about it, that makes sense: there's a lot more of them
than there are you. 

Be kind to them! They, in turn, will be kind to you.

And you never know, five years down the road it might be you 
who has to read that long-forgotten code. You'll be glad, then, that
you considered the reader when you wrote it.

```

```
#!rst

In General
----------

- `Magic numbers <http://en.wikipedia.org/wiki/Magic_number_(programming)#Unnamed_numerical_constants>`_ 
  are unacceptable.
  
- As a generalization of the above, 
  `DRY <http://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_ is a 
  valuable concept.

- Comment your Subversion commits.

- Avoid abbreviations in variable, function, file and class names. There's
  usually more than one "obvious" way to abbreviate a word or phrase, so if 
  you're not
  the author of the code (or sometimes even if you *are* the author of the
  code) it's hard to remember what abbreviation was used.

  For instance, if you're looking at a variable representing "metabolite 
  description", the author could name it metabolite_desc or metabolite_descr 
  or mdescription or m_desc or mdescr or md. Python requires a bit more 
  care in this area than compiled languages (like C) since compilers complain
  about undeclared variables whereas Python will happily accept something like 
  this:
```

```
#!python
    
    # Code added by person A
    mdesc = [1, 2, 3]

    # ...several pages of code here...

    # Code added by person B months later -- see the bug?
    if erase_previous_data:
        mdsc = None

```

```
#!rst
  There's also the benefit that longer variable names help to document the code.
  The name `mdesc` could mean "mule desecration" for all I know, whereas
  `metabolite_description` carries meaning.

  Yes, using unabbreviated variable names makes it harder to respect PEP 8's
  recommendation of limiting lines to a maximum of 79 characters.

  Standard abbreviations are acceptable, like *fft* for Fast Fourier
  Transform, or *ppm* for parts per million. Obviously, "standard" is a weasel
  word that doesn't really say what's OK and what's not. There's no hard and
  fast rule; we'll have to judge on a case-by-case basis.

  Here's some questions to ask when you're trying to decide whether or not an 
  abbreviation is OK --
  
  - Does the abbreviation appear more commonly than the expanded form?
  - Is my audience (i.e. those reading the code) likely to be familiar with 
    the abbreviation?
  - Will I save a lot of typing by abbreviating?
    
- Don't be shy about using parentheses to clarify operator precedence. e.g.

  This works:
```

```
#!python  
     z = something * PI - something_else / FUDGE_FACTOR
```
```
#!rst
  This works and makes your intent clear:
```
```
#!python
     z = (something * PI) - (something_else / FUDGE_FACTOR)
```

```
#!rst
- Don't put redundant information in names. For instance, in a Person class it
  is unnecessary to call the attributes ``person_name``, ``person_address``, 
  etc. Simply  use ``name`` and ``address`` instead. Similarly, 
  if a file is part of the Analysis
  project, there's no reason to name the file ``analysis_utilities.py``. Just
  ``utilities.py`` will suffice. 
  
  As a bonus, the simpler name will still make
  sense if the project's name 
  changes or is merged with another project.

- All of our source code should be straight ASCII. Be careful about copying &
  pasting text from MS Word that contains curly quotes or em/en dashes.

  If you're ever confronted with a choice as to what non-ASCII encoding to 
  use, choose utf-8.

- Always use / as the path separator. Microsoft operating systems accept both 
  \\ and / (since DOS 2.0 `according to this discussion
  <http://bytes.com/groups/python/23123-when-did-windows-start-accepting-forward-slash-path-separator>`_).
  It's only the DOS command 
  line that hiccups on /. By contrast, backslash as a
  path separator only works under Windows and is an escape character in Python
  strings.

- If you come across (or write) some code that is or may be broken, fix it. If
  the fix isn't obvious or you don't have time, add a comment containing the
  string FIXME (no space!) in the comments and a brief explanation of what you
  think is wrong. e.g.
```
```
#!python    
        if film == HOLY_GRAIL:
           bring_out_your_dead()
        elif film == LIFE_OF_BRIAN:
           look_on_bright_side()
        elif film == HOLLYWOOD_BOWL:
            albatross()
        # FIXME - need an else statement; how to handle unexpected cases?
```


# C and C++

C++ coding standards in detail:  CppCodingStandards


# Python

 
```
#!rst

Python 
------

- `Duck typing <http://en.wikipedia.org/wiki/Duck_typing>`_ is an important 
  and valuable concept in Python that can feel strange if
  you're used to statically typed languages.
    
- The corollary -- if you find yourself using ``type()`` or 
  ``isinstance()``, that's usually a sign of unPythonic code. 


- Our project will require a minimum Python version of 2.5, so any language
  features (like the ternary operator) or libraries (like sqlite or ctypes) that
  are in 2.5 are fair game.

- If you're new to Python, use an editor with decent code highlighting so that
  it tells you when you're using a Python keyword as a variable name.

- `PEP 8 <http://www.python.org/dev/peps/pep-0008/>`_
  is worth following. The main
  things to remember are CamelCase for class names and lower_with_underscores
  for variable names. Filenames should be all lower case since the filesystems
  on some of our target operating systems are not case-sensitive.

  Note that PEP 8 observes, "The naming conventions of Python's library are a
  bit of a mess...". It's true! The standard library is unfortunately not always
  a good example to follow.

  `PEP 20 <http://www.python.org/dev/peps/pep-0020/>`_ is also worth a 
  read as it's really short.
  
- Never use the idiom ``from some_package import *``. It has a couple of
  disadvantages. For one, it clutters up your local namespace and can even lead
  to one module stepping on another's variables.

  The other huge disadvantage is that it makes one's code difficult to read. 
  If the code
  imports * from, say, five modules and then calls a function ``foo()``, 
  the person reading the code has to guess if the function is local, and
  if not, then which one of the five imported modules contains it.

  This is also true to a lesser extent for ``from some_package import xyz`` where
  xyz is a function. If I see a call to ``xyz()`` in the code, I have to look 
  around
  to see whether it is a local function or an imported one. By contrast, when I
  see ``some_package.xyz()`` in the code, I know exactly where that function comes
  from.

  If you find that you're importing some package with an inconveniently long
  name, make use of Python's as keyword:
```
```
#!python
   import xml.etree.ElementTree as ElementTree
```
```
#!rst
  Be mindful of creating obscure abbreviations, however:
```
```
#!python  
   import some_complicated_math_library.curves.splines as sp
```
```
#!rst  

- Python booleans are True and False, not 1 and 0. Be aware of this when you're
  porting code from languages that don't have a native Boolean type.
  Some examples include IDL, C, Fortran and possibly Matlab. They usually 
  use 1 and 0 to represent
  true and false. (C++ has a native boolean type.)

  Note that it's OK to treat 1 and 0 as booleans in expressions, just don't 
  *assign* them as booleans.

  For instance, if a variable (received from a C function for instance) has 
  a value of 1 or 0 it is perfectly acceptable to do this:
```
```
#!python
    if some_c_library.function_that_returns_one_or_zero():
       do_something()
```
```
#!rst
  It would be unPythonic, however, to do this:
```
```
#!python
    def on_foo_checkbox_clicked():
       self.foo_is_on = 1  # should be True, not 1
```
```
#!rst
  As a specific application of duck typing, it's usually unPythonic to 
  explicitly test for True and
  False. Note that all of these evaluate to False:
```
```
#!python
        bool(None)
        bool("")    # empty string
        bool([ ])   # empty list
        bool(( ))   # empty tuple
        bool({ })   # empty dict
        bool(0)
```
```
#!rst
  All of these evaluate to True:
```
```
#!python
        bool(n) where n is a non-zero number
        bool(s) where s is a non-empty string
        bool(z) where z is a non-empty iterable (tuple or list)
        bool(m) where m is a non-empty mapping (dict)
        bool(o) where o is an object other than None 
```
```
#!rst
  Historical note: the values True and False weren't added to Python until
  sometime in the 2.x series (2.2 I think) so you might see some Python code --
  esp. Python library code which must remain compatible with very old 
  versions -- using 1 and 0 instead of True and False.

- To prepare for Python 3.0, we need to `explicitly use "true" 
  division <http://www.python.org/doc/2.2.3/whatsnew/node7.html>`_.

  In order to do so, we need to add this to every module that uses division:
```
```
#!python  
    from __future__ import division
```
```
#!rst  
  And then we need to review the use of division in those modules 
  to ensure we're not breaking them.

  We can either pay this cost now, or pay it later when we want to move to
  Python 3 and there's a lot more code to review and fix.


- Python 2.2 introduced improved classes; these are called (rather 
  unfortunately) "new"-style classes. Old-style classes are gone completely 
  in Python 3. Our classes should always be new-style classes. To create a 
  new-style class, inherit from object. e.g. this:
```
```
#!python
    class TransformThingy(object):
```
```
#!rst
  not this:
```
```
#!python
    class TransformThingy():
```
```
#!rst

- Python has the identity operator "is". It means "are these objects the same
  object" rather than "are they equivalent". The only time you'll probably need
  to use it is when comparing something to None.
```
```
#!python
       if foo is None:
           do_something()
```
```
#!rst

  Since we prefer to perform simple boolean tests, the need to check explicitly
  for None (as opposed to False) might indicate a problem somewhere upstream, as
  this would be better:
```
```
#!python
      if not foo:
         do_something()
```
```
#!rst

  Sometimes an explicit test for None is unavoidable, however.

  In short, the admonition against "is" is similar to that against 
  ``isinstance()``, although less strong. If you find yourself using it, it's 
  often a sign of a design flaw.


- Don't underestimate what you can learn from testing concepts in the Python
  interpreter. For instance, if you can't remember the rules
  for taking a slice of a string from the end, try it out in the Python
  interpreter:
```
```
#!python
        $ python
        Python 2.5.1 (r251:54863, Nov 17 2007, 21:19:53) 
        [GCC 4.0.1 (Apple Computer, Inc. build 5367)] on darwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>> "abcde"[:-2]
        'abc'
        >>> 

}}}