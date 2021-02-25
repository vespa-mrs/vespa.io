# PyGAMMA and Python Strings
## Summary
 * Python strings passed to PyGAMMA must be 8 bit, not Unicode.
 * The safe way to ensure that a string is 8 bit is to call 
 `my_string.encode("utf-8")`.
 * You can convert a string to 8 bit by calling `str(my_string)`, but
 on some strings it will raise an exception.


## The Problem
Python 2.x has two string types -- Unicode and what I'll call "8 bit" strings.
In general, one can ignore the difference until one has to deal with the
world outside of Python.

Calling PyGAMMA is one of those "world outside" cases where the difference 
matters. PyGAMMA
doesn't like Unicode strings. (There's a 
[#PyGAMMASWIGTechnicalDetails detailed explanation] below.) 
If you pass a Unicode string to PyGAMMA, you're likely to get a 
NotImplementedError.

```
#!python
>>> import pygamma
>>> isotope = pygamma.Isotope("1H")  # This works, but...
>>> isotope = pygamma.Isotope(u"1H")  # ...this does not
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/pygamma/pygamma.py", line 133, in __init__
    this = _pygamma.new_Isotope(*args)
NotImplementedError: Wrong number of arguments for overloaded function 'new_Isotope'.
  Possible C/C++ prototypes are:
    Isotope()
    Isotope(Isotope const &)
    Isotope(std::string const &)

>>>
```


## Solution 1 (Recommended) - `my_string.encode("utf-8")`
The safest solution is to explicitly state the encoding when converting
one's Unicode strings to 8-bit. There are lots of encodings to choose from
but for most people *UTF-8 is the best choice*.

Calling `.encode()` is a little more cumbersome than calling `str()`, but 
guaranteed to succeed where `str()` fails as in the example below. 
(The string `u"Bj\xf6rn"` is Python's Unicode representation of 
"Bjorn" which is a fairly common first name in Sweden.)


```
#!python
>>> my_name = u"Bj\xf6rn"
>>> my_name.encode("utf-8")   # This works!
'Bj\xc3\xb6rn'
>>> str(my_name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character u'\xf6' in position 2: ordinal not in range(128)
```



## Solution 2 (Not Recommended) - `str(my_string)`

Another way to ensure that a string is 8 bit is to call Python's builtin 
function `str()`. This leaves 8 bit strings unchanged and converts Unicode
strings to 8 bit, as in the example below. 

```
#!python
>>> type("foo")
<type 'str'>
>>> type(u"foo")
<type 'unicode'>
>>> type(str(u"foo"))
<type 'str'>
```

However, *`str()` raises an exception when called on some strings*. 
That's because when a Unicode string is converted to 8 bit, it must
be _encoded_ via an encoding scheme capable of representing Unicode
as an 8 bit stream. In the call to `str()`, the encoding is implicit.
It uses whatever sys.getdefaultencoding() returns, and on most systems
that's "ascii".

That means that a call to `str(my_string)` is equivalent to this:
```
#!python
my_string.encode(sys.getdefaultencoding())
```

On most systems, that's equal to this:

```
#!python
my_string.encode("ascii")
```

Therefore, the string you're converting had better be limited to the
128 characters in the ASCII repetoire or you'll get an exception --

```
#!python
>>> str(u"Bj\xf6rn")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character u'\xf6' in position 2: ordinal not in range(128)
```


## Strings from Vespa
Vespa guarantees that all strings passed to user pulse sequence code
(sequence and binning) have been converted to UTF-8 so they're safe for
use with PyGAMMA.


## PyGAMMA/SWIG Technical Details
PyGAMMA is a C++ library wrapped with SWIG, and SWIG's documentation says: 
  At this time, SWIG provides limited support for Unicode. Some languages 
  provide typemaps for `wchar_t`, but bear in mind these might not be 
  portable... This is a delicate topic that is poorly understood by many 
  programmers and not implemented in a consistent manner across languages. 

When one calls a PyGAMMA function that receives a string as a parameter,
the C++ runtime tries to find a function signature that matches the 
arguments passed. Let's return to the example from above.

```
#!python
>>> import pygamma
>>> isotope = pygamma.Isotope("1H")  # This works, but...
>>> isotope = pygamma.Isotope(u"1H")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/pygamma/pygamma.py", line 133, in __init__
    this = _pygamma.new_Isotope(*args)
NotImplementedError: Wrong number of arguments for overloaded function 'new_Isotope'.
  Possible C/C++ prototypes are:
    Isotope()
    Isotope(Isotope const &)
    Isotope(std::string const &)

>>>
```

`Isotope()` wants a `std::string const &` passed to it, but Python's Unicode
type doesn't map to that. Therefore the C++ runtime is unable to find a
matching function and raises a NotImplementedError.


## Historical Note
The Python 2.5 documentation calls 8 bit strings "normal" strings. 
This was probably written when Python 2.0 came out and was 
appropriate then because Python 1.x had only 8 bit strings. Unicode strings 
were new in Python 2.0 so of course they seemed "not normal". 

As Python 2.x
matured, everyone realized that Unicode was the way to go. More and more 
libraries started returning Unicode strings by default. Nowadays, Unicode 
strings are just as "normal" as 8 bit ones to most Python programmers.

Python 3.x has only Unicode strings, so in the eventually-to-be-default
version of the language, Unicode strings are the norm.

