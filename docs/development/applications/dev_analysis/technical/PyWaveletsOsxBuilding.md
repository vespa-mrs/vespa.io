# Building Our PyWavelets for OS X Package
This page is technical documentation for Vespa developers who want to build 
our [PyWaveletsOsx PyWavelets for OS X] package. 

In 2012 when we first built our own PyWavelets distribution for OS X, building this 
package was a bit complicated. Now in 2016, thanks to Python's new wheel format,
it's a snap.

## The Build Process
You first need to satisfy PyWavelets' build dependencies -- Python, of course, 
as well as `numpy` (I think) and `Cython`. You'll also need the Python packages
`setuptools` and `wheel` in order to build wheels. All of these come with Anaconda.

To build a wheel, download the PyWavelets source code, untar it, and then 
enter this command --
```
python setup.py bdist_wheel
```

Python will build PyWavelets for you and place a correctly-named wheel in the `dist` directory.

