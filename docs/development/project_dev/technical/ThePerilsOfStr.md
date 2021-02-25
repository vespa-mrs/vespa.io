# The Perils of `str()`
## Summary
The built-in function `str()` is handy but doesn't play well with non-ASCII
strings. We can replace it with something better.

 * It's OK to call `str()` on non-strings.
 * It's not OK to call `str()` on strings because it might raise an exception.
 Use the string's `.encode()`
 method and pass `"utf-8"` as the parameter. e.g. `my_string.encode("utf-8")`
 * The built-in function `unicode(my_string)` is a bit less cumbersome than 
 calling `my_string.encode("utf-8")`, but `unicode()` doesn't exist in 
 Python 3 so all instances of it will eventually have to be replaced. We should
 keep our use to a minimum.
 * We can't avoid using `unicode()` entirely because that's the best way 
 to convert our custom objects (experiments, metabs, etc.) to strings. For example,
 if you need a string representation of an experiment, use 
 `unicode(the_experiment)`.


## Details
Python 2.x has two string types, Unicode and what I'll call "8 bit" strings.
Most modern Python libraries return Unicode. (See the historical note
below.) That includes the two sources of most of our strings -- `sqlite` 
and `wxPython`. Python makes it easy to mix the two types of strings and in
general we can ignore the difference.

However, there's two cases where we must use 8 bit strings, and how we convert
from Unicode to 8 bit is important. The two cases where we need 8 bit strings
are (1) when passing strings to PyGAMMA and (2) when writing to a stream 
(like a file or the console). You might think that it'd be a concern when 
writing to the database, but the sqlite module handles that for us.

To represent Unicode in 8 bit strings, one must _encode_ the string. 
For historical reasons there are lots of encodings but nowadays in this
part of the world, UTF-8 is the most popular and the only one we'll use.

In Python, one encodes a Unicode string with its `.encode()` method like so --
```
#!python
some_unicode_string.encode("utf-8")
```

The result is an 8 bit string. The `.decode()` method reverses the process.


It's less obvious, but the built-in function `str()` can also convert a
Unicode string into 8 bit. Normally we call `str()` on non-string objects
to make them strings, but one can call it on Unicode strings to convert
them to 8 bit. It's equivalent to this -- 
```
#!python
some_unicode_string.encode(sys.getdefaultencoding())
```

What's `sys.getdefaultencoding()`? It's the problem. In most Pythons it's
"ascii" which means the string you're converting had better be limited to the
128 characters in the ASCII repetoire or you'll get an exception --

```
#!python
>>> str(u"Bj\xf6rn")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character u'\xf6' in position 2: ordinal not in range(128)
```


The string `u"Bj\xf6rn"` is Python's Unicode representation of 
"Bjorn" which is a fairly common first name in Sweden.


So now you can probably see where `str()` leads to trouble. 
A Swedish user might name a metabolite that he got from his colleague
"aspartate from Bjorn". The code below (in which metabolite.name is a
Unicode object) is no problem -- 
```
#!python
metabolite.name.encode("utf-8")
'aspartate fr\xc3\xa5n Bj\xc3\xb6rn'
```

But this raises an exception -- 

```
#!python
str(metabolite.name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character u'\xe5' in position 12: ordinal not in range(128)
```

Because that code is equivalent to this (assuming the typical default 
encoding of ASCII) -- 
```
#!python
metabolite.name.encode("ascii")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character u'\xe5' in position 12: ordinal not in range(128)
```


So the code that we wrote that calls `str()` to convert strings from the 
GUI or the database into 8 bit representations in order to make those strings
safe for PyGAMMA or to display them in a text file would have broken as soon as 
someone passed non-ASCII to it. All of that code was replaced in r1652.


## What Does This Mean For Us?
When one calls `unicode()` on an object, Python first checks to see if the object
implements `__unicode__()`. If not, it calls the object's `__str__()` method.
If the object doesn't implement a custom `__str__()` method, standard object
inheritance implies a call to the `__str__()` method on Python's `object` 
class (from which all objects derive). That will print 
the reliable-but-boring representation you've surely seen before --
```
#!python
<vespa.common.mrs_metabolite.Metabolite object at 0x13f2350>
```

That's the short version of how `unicode()` is implemented.

Note that an object's `__unicode__()` method _must_ return a Unicode object.


When one calls `str()` on an object, Python ignores `__unicode__()` and calls 
only `__str__()`. _However_, objects may return Unicode objects from their
`__str__()` method. If an object's `__str__()` method returns a Unicode 
object, Python might (sometimes? always?) convert 
the string to 8 bit using the default encoding before `str()` returns.

When we `print` an object, Python calls `str()`. 

Therefore --

 * We want to be able to continue to use `print my_object`, so all
 of our objects need to implement `__str__()`.
 * If we return a Unicode object from the `__str__()` method, Python will 
 convert it to 8 bit using the default encoding. As discussed above, this
 breaks when the string is non-ASCII.
 * Therefore, we need to return an 8 bit string from `__str__()`, which,
 for us, implies UTF-8.
 * Sometimes we want a Unicode representation of our objects, so our
 objects also need to implement `__unicode__()`.
 * To keep ourselves sane, the `__unicode__()` method should be the 
 primary method for converting the object to a string. The `__str__()`
 method should implemented like so --
```
#!python
def __str__(self):
    return self.__unicode__().encode("utf-8")
```

This conversation goes into a little more detail on the subject 
of `__str__()` and `__unicode__()` --[[br]]
http://mail.python.org/pipermail/python-dev/2006-December/070237.html


## So What's So Great About UTF-8?
UTF-8 is fiendishly clever in that it is a superset of ASCII. That is, every
ASCII character has the same value in UTF-8. Yet UTF-8 can encode a huge 
chunk of Unicode -- "virtually all characters in common use" according to
Wikipedia. (Thus UTF-8 is a superset of ASCII
in the same way that North America is a superset of Poughkeepsie. ASCII
encodes 127 characters, UTF-8 over 1.1 million.)

This is useful to us because if we take an ASCII string and "convert" it
to UTF-8 by calling `my_string.encode("utf-8")`, we get the same string back.
We haven't ruined it. At the same time, it's a safe, standard way to encode 
any non-ASCII that might happen to drift our way. 



## Technical Notes
There's no harm in calling `.encode()` on a non-Unicode string.
Python returns the same string --
```
#!python
>>> assert("foo" == "foo".encode("utf-8"))
>>> assert(type("foo") == type("foo".encode("utf-8")))
```


One can make a string literal Unicode by prefacing it with 'u' as in the
example below.

```
#!python
>>> type("hello world")
<type 'str'>
>>> type(u"hello world")
<type 'unicode'>
>>> 
```

When an 8 bit string is added to a Unicode string, Python "promotes"
the former to Unicode. 

```
#!python
>>> type(u"hello" + "world")
<type 'unicode'>
```

Both Unicode and 8 bit strings derive from the class `basestring`. 
```
#!python
>>> isinstance("hello", str)
True
>>> isinstance("hello", basestring)
True
>>> isinstance("hello", unicode)
False
>>> isinstance(u"hello", unicode)
True
>>> isinstance(u"hello", basestring)
True
>>> isinstance(u"hello", str)
False
```


## Historical Note
The Python 2.5 documentation calls 8 bit strings "normal" strings. 
This was probably written when Python 2.0 came out and was 
appropriate then because Python 1.x had only 8 bit strings. Unicode strings 
were new in Python 2.0 so of course they seemed "not normal". 

As Python 2.x
matured, everyone realized that Unicode was the way to go. More and more 
libraries started returned Unicode strings by default. Nowadays, Unicode 
strings are just as "normal" as 8 bit ones to most Python programmers.
Python 3.x has only Unicode strings, so in the eventually-to-be-default
version of the language, Unicode strings are the norm.

