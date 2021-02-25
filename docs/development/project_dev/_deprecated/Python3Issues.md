# Python 3 Changes Of Which To Be Aware
Python 3 is the first Python release ever which introduced 
backwards-incompatible changes. There's a pretty complete list of those
changes here: 
http://docs.python.org/dev/3.0/whatsnew/3.0.html

This document is a summary of those most likely to affect us and for which 
we can prepare.

 * The division operator changes.
 
 Python 3 concludes a long-standing debate in the Python community by 
 changing the '/' operator to return a float even if its arguments are int.
 In other words, in Python 2, 3/2 == 1. In Python 3, 3/2 == 1.5.
   
 We can get "true" division now in Python 2 by adding this at the top of 
 a file:
   `from __future__ import division`

 Here's an example of the difference under Python 2.5:
```
#!python
    >>> 3/2
    1
    >>> from __future__ import division
    >>> 3/2
    1.5
    >>> 
```
 Our code involves lots of math, so this is a potentially big change for 
 us. However, we're well positioned to handle it if we take action now. 
 It's pretty simple -- we'll have to retest any modules affected by this 
 change, and I think that means most of them. We'll have a lot more 
 modules in the future than we have now, so making this change will
 only get more expensive as time goes on.
   
 For that reason, '''I recommend 
 that we immediately begin using "true" division in all our new code, and
 that we change our existing code to use "true" division as we get the
 opportunity to do so.'''
   
 Last but not least, note that in both Python 2 & 3, the // operator always 
 gives the truncating
 behavior. 3//2 == 1  and  11//3 == 3. (Note that the latter doesn't round
 up to 4.)
   

 * The different between Python ints and longs disappears. 
 
 In Python 2, ints are represented with C longs, so their minimum range 
 is +/- 2147483647. Python 2 longs are effectively unlimited. (If you create
 a number big enough, eventually your computer will run out of memory or
 Python will die, but I've created a number with > 78,000 digits and Python
 was fine with it.)
   
 In Python 3, longs go away and ints are effectively unlimited.
   

 * Absolute imports become the default.
 
 This change will only affect code inside packages, and I debated even
 mentioning it here. Suffice it to say that if we need to change our 
 import statements for Python 3, the changes will be minor, 
 straightforward, and easy to find (since import statements are almost
 always confined to the first pages of modules).

 * "Everything you thought you knew about binary data and Unicode has 
 changed."
    
 Fortunately for us we're not manipulating too much text, so the effect
 on us will be relatively minor. In addition, there's not much we can
 do now to future-proof our code. (It's hard to write code of much
 significance that's compatible with both Python 2 & 3.)
    
 * The builtin `file()` constructor is gone. The Python 2 documentation
 says, "When opening a file, it's preferable to use open() instead of
 invoking this constructor directly." Despite this, I often used the 
 `file()` constructor because it allowed me to read in a file in one line
 like so:

   `s = file("foo.txt", "rb").read()`
