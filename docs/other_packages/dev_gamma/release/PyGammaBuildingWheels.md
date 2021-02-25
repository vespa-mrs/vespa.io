# Building Distributable PyGamma Wheels
As of version 4.3.3, PyGamma is distributed via [Python wheels](http://pythonwheels.com). This document explains how to build those wheels. It's principally for PyGamma's maintainers, although you might want to use it if you build a custom version of PyGamma and want to distribute it to colleagues.

As of this writing (January 2016), PyGamma only supports 64-bit Python 2.7. Building wheels for other platforms/Pythons is possible, but unsupported.

## Build Binaries
In order to build a wheel, you first need to [GammaBuildingLibrary build the PyGamma binaries]. Under *nix, make sure you build the `pysgdist` target (`make pysgdist`). Under Windows, building the provided solution is sufficient.

## Install the Wheel Package
In order to build wheels, your Python needs the `wheel` package. Installing that is simple:
```
pip install wheel
```

## Build the Wheel
Once the binaries have been built, you will have a new directory in your gamma source code tree at `gamma/pygamma/dist_staging`. Open a command prompt and `cd` to `gamma/pygamma` which is where `setup.py` lives and execute this command:
```
python setup.py bdist_wheel
```

Python will create an appropriately-named wheel file for you in `gamma/pygamma/dist`.

## Upload the  Wheel to PyPI
This section is TBD. 

## Virtual Machine Note
Wheels need to be constructed on the target distribution platform. In other words, if I'm building a wheel for OS X, I need to run `python setup.py bdist_wheel` on OS X. 

In most setups, this is blindingly obvious. However, if one is using virtual machines to build PyGamma (e.g. a Linux guest on an OS X host), take care to complete //all// of the steps above in the guest operating system.

One might be tempted to build the binaries on the guest platform and then run the `bdist_wheel` step on the host platform (or vice versa). If you do, you'll get a wheel file out of it, but the wheel name won't match the contents so it won't work for anyone.