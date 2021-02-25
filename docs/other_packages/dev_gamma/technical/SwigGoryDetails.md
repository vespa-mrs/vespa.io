# Gory details of Swig Issues
Quote from Swig documentation:
''"Given the tricky nature of C++ memory management, it is impossible for proxy classes to automatically handle every possible
memory management problem. However, proxies do provide a mechanism for manual control that can be used (if necessary) to
address some of the more tricky memory management problems."''

*Lets dig deeper into the two issues mentioned...*

### First, Python has garbage collection and C++ does not
We created PyGAMMA by applying SWIG to GAMMA. No special treatment was applied for handling reference counting, and C++ does not do reference counting by default. 

Python has reference counting on each object, so in pure Python code, when an object is being considered for garbage collection, the tree of ownership is scanned for any objects that are still in use. If anything in the tree is still being pointed too, it will not be garbage collected.

In C++ - which is optimized for speed - there is no garbage collection. Users need to manage all their own memory: i.e. Allocation, deletion and keeping track so that nothing is lost.

In SWIG, the interface between the two, their is some support to manage object ownership. It creates proxy classes that point to the underlying C++ object and keeps track of the python object that owns that proxy (i.e. what Python variable has ownership of that proxy). However, it does not keep track of the hierarchy of ownership within C++. So, if BigObject owns SubObject, Swig will keep track of the ownership of the proxy class for BigObject, but not for SubObject. This can cause non-pythonic behavior to be observed in some situations. 

In Python, you expect the reference count to be incremented on the 'SubObject', ACQ.table(sigma0), when you have a new Python object, mx, pointing to it:
```

>>> ACQ = pygamma.acquire1D()

>>> mx = ACQ.table(sigma0)

```

However, this is not - by default - how it's handled in the SWIG wrapped C++ code. Why? In C++ the function, ACQ.table(...), returns a reference to a table that is still part of ACQ. Swig handles this as it would a pointer. So mx is a proxy class with a pointer to the internal object inside of ACQ.  However, mx does not get ownership of this object, as it is still considered owned by ACQ. So if this code segment is part of a function, then when the function returns ACQ - and the table to which mx points - will all be deleted (garbage collected).

In C++, however, the situation is a little different (see below).

### Second, Python has pointer semantics and C++ has copy semantics
As a preamble to this section, keep in mind that Python does not have the distinctions between pointer, reference, and Object. In C++ we'd have to think about whether we wanted a pointer, a reference, or a copy (a new object), and have to handle all the memory management issues that ensue. Some knowledge of C++ would help for understanding this section.

Assume that BigObject has a method called sub_obj() that returns a reference to SubObject, declared like this:
```
class BigObject
{
    // ...    
    SubObject & sub_obj() const;
};
```

So when you write this (in C++):

- Code snippet 1 -
```
BigObject Big = new BigObject();
SubObject Asub = Big.sub_obj();
```

The assignment, Asub = Big.sub_obj(), is actually creating a copy of the subObject that is in BigObject.

Note, that if we actually just wanted a reference (similar to a pointer), in C++ we could write:
```
BigObject Big = new BigObject();
SubObject & Asub = Big.sub_obj();
```

If we create a Python code snippet that is analogous to code snippet (1) - using the Swigged version of the C++ code - then we'd have:
```
>>> Big = BigObject()
>>> Asub = Big.sub_obj()
```

In this case, Asub is actually a proxy containing a pointer to the instance of SubObject that is a part of BigObject. This is very different than how it worked in C++, and these differences is behavior cause some confusion for both the C++ and python developer.  

When we garbage collect _Big_ we would also garbage collect the SubObject, and this could lead to problems - depending on how it is used in your code. 


*Note: In the Swig Documentation (version 1.39) it states:*

  * "Don't return references to objects allocated as local variables on the stack. SWIG doesn't make a copy of the objects so this will probably cause your program to crash."
