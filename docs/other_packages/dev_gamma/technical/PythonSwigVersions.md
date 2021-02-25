# Python and Swig Version Issues

You may run into build and test problems if you have multiple versions of Python or Swig installed on your computer, and your default version of Python or Swig is not the one you want to specify for your build. 

This is likely to be an issue if you are a power developer, or you are installing this in a server environment.

For example you may be the administrator of a system on which the default version of Linux is 2.4, but you want to install this for Python version 2.7. You may even have 2.7 as your user default. However, when installing the software you need to be root (or sudo/su), and root has 2.4 as the default version.

Here are two ways to manage this situation.
  1. Change one or both of these lines in the Makefile,
```
PYTHON = python
SWIG   = swig
```

  to point to the version of python/swig that you want to use for this build. e.g. Something like this,
```
PYTHON = /usr/bin/python
SWIG  = /usr/bin/swig
```
  or this
```
PYTHON = /nmrnet/gamma/python-i86pc-cc/bin/python
SWIG   = /nmrnet/gamma/python-i86pc-cc/bin/swig
```

  2. Alternatively you can override these defaults on the command line, 
```
make PYTHON='/opt/EPD/bin/python' SWIG='/opt/EPD/bin/swig' pysgdist
```
  and
```
make PYTHON='/opt/EPD/bin/python' SWIG='/opt/EPD/bin/swig' test
}}}