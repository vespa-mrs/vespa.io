# PyWavelets and Vespa
[PyWavelets](http://www.pybytes.com/pywavelets/) is a Python package that
performs discrete wavelet transform.
Vespa-Analysis can use it for baseline estimation during fitting.

Unlike most of Vespa's dependencies, PyWavelets is optional. In other words,
you're not required to install it before installing Vespa. If it's not 
installed, Vespa will still run, although Analysis won't allow you to use the 
wavelet filter for baseline estimation during fitting. Once PyWavelets is 
installed, Analysis will automatically find it and make it available to you.

PyWavelets is available as a pre-built binary for Python on Windows, Linux and OS X.
We provide details on where to get it for each platform below.

## Windows
PyWavelets' author provides 
[prebuilt Windows binaries on PyPI](https://pypi.python.org/pypi/PyWavelets/).

## Linux
As of this writing (early 2012), PyWavelets is available via the package
manager of most Linux distributions, including Ubuntu > 8.04, Fedora > 14 (or
possibly earlier), RHEL > 6, and OpenSUSE > 11.

Check your package manager for `pywt` or `PyWavelets`.

## OS X
We created [PyWaveletsOsx our own PyWavelets distribution for OS X]. 
3rd party package managers like `homebrew` might also provide PyWavelets.

