## Swig and Garbage Collection - BigClass Example
This is a simple Python example to show the type of situation where the swigged C++ problem comes up.

This code works fine in pure python, but has issues if using swigged version of objects.

```

class SubClass(object):
    def __init__(self):
        self.x = 0

    def do_something(self):
        print "x = %s" %(self.x, )

class BigClass(object):
    def __init__(self):
        self._sub = SubClass()

    def sub(self):
        return self._sub


def afunction():
    big = BigClass()
    Asub = big.sub()

    # Give SubClass a real value
    Asub.do_something()
    Asub.x = 42
    Asub.do_something()

    return Asub

asub = afunction()

# This works fine in pure Python.
# Bad things happen here if using Swigged versions 
# of BigClass and SubClass

asub.do_something() 

}}}