# How to Build HLSVDPRO Wheels
This document explains how to build Python wheels for HLSVDPRO for
Windows, Linux, and OS X. We only describe how to build 64-bit wheels.

You might also be interested in 
[HlsvdproLibraryDependencies why these wheels use so much static linking]
and how dependencies are resolved in general, although that 
information isn't necessary for building wheels.

## Environment Setup
Environment setup is a one-time step. If you've already done this, you can
skip to the compile step.

If not, we have instructions for --
 * HowToBuildWheelsWindowsSetup
 * HowToBuildWheelsOsxSetup
 * HowToBuildWheelsLinuxSetup

## Compile the Library
Once you have your environment set up, compiling is very similar on each
platform.

1. Open a command prompt and switch to the `hlsvdpro/hlsvdpro/src` directory.
1. Copy the platform-specific Makefile to `Makefile`, e.g.
```
 cp Makefile.win Makefile
```
1. Under OS X, execute this command --
```
 export MACOSX_DEPLOYMENT_TARGET=10.9
```
1. Under OS X, you also need to hide `libquadmath` if you haven't done so already. (See below)
1. Under Linux, if you're using GFortran < 4.3, you'll need to patch `hlsvdpro.f` with this command --
```
 patch < hlsvdpro_downgrade.patch
```
1. Enter `make dist`. (Under Windows, enter `mingw32-make dist` instead.)
 The Makefile will build HLSVDPRO and copy the binaries
 where they need to be for building the wheel.

## Build the Wheel
*Important:* To ensure you don't pick up junk from building a previous
wheel, delete the following directories each time before you build a wheel --
```
hlsvdpro/build
hlsvdpro/hlsvdpro.egg-info
```

Those directories are output from the wheel-building step.

Move into the directory that contains `setup.py`. (That's `cd ../..` if you
were just using your command prompt for the compile step.)

This package is a little strange by Python wheel standards, so the wheel
package needs some hints to get the name right. The `--universal` flag
tells wheel that this is compatible with Python 2 and 3. The
`--plat-name` specifies the platform with which the binary portion of the
wheel is compatible.

On Windows --
```
python setup.py bdist_wheel --universal --plat-name win_amd64

python setup.py bdist_wheel --python-tag py27 --plat-name win_amd64
```

On Linux --
```
python setup.py bdist_wheel --universal --plat-name manylinux1_x86_64
```

On OS X --
```
python setup.py bdist_wheel --universal --plat-name macosx_10_9_x86_64
```

Your wheel file(s) are in the `dist` directory.

## Build the Wheel - HLSVDPROPACK
*Important:* To ensure you don't pick up junk from building a previous
wheel, delete the following directories each time before you build a wheel --
```
hlsvdpropack/build
hlsvdpropack/hlsvdpro.egg-info
```

Those directories are output from the wheel-building step.

Move into the directory that contains `setup.py`. (That's `cd ../..` if you
were just using your command prompt for the compile step.)

This package is a little strange by Python wheel standards, so the wheel
package needs some hints to get the name right: 

The `--python-tag` flag tells wheel that this is compatible with some version of Python 2.x or 3.x. Be sure to use the version of Python under which the *.pyd library was compiled when creating the 'python-tag'. Example: py27, py37, py38, etc. 

The `--plat-name` specifies the platform with which the binary portion of the
wheel is compatible.

On Windows --
```
python setup.py bdist_wheel --python-tag py27 --plat-name win_amd64
```

On Linux --
```
python setup.py bdist_wheel --python-tag py37 --plat-name manylinux1_x86_64
```

On OS X --
```
python setup.py bdist_wheel --python-tag py38 --plat-name macosx_10_9_x86_64
```

Your wheel file(s) are in the `dist` directory.

## How (and Why) to Hide libquadmath on OS X
OS X hates to link
statically and will always link to dynamic version of libraries if it can find
them. To force HLSVDPRO to use the static version of libquadmath, we hide the
dynamic version from the linker.

The 64-bit version of `libquadmath` is
`/usr/local/gfortran/lib/libquadmath.0.dylib`.
Rename it from `libquadmath.0.dylib` to `libquadmath.0.dylib.hidden`.

I suggest that you undo this rename step after you finish building
HLSVDPRO, otherwise you will have a broken GFortran installation.

The OS X `make dist` build step contains a check that will
squawk at you if it looks like the HLSVDPRO dylib you build contains a
reference to  `libquadmath.0.dylib` (i.e. if the static linking
didn't go as planned).


## Wheel File name convention
From https://legacy.python.org/dev/peps/pep-0427/ 

The wheel filename is {distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl.

*distribution* - Distribution name, e.g. 'django', 'pyramid'.

*version* - Distribution version, e.g. 1.0.

*build tag* - Optional build number. Must start with a digit. A tie breaker if two wheels have the same version. Sort as the empty string if unspecified, else sort the initial digits as a number, and the remainder lexicographically.
language implementation and version tag
E.g. 'py27', 'py2', 'py3'.

*abi tag* - E.g. 'cp33m', 'abi3', 'none'.

*platform tag* - E.g. 'linux_x86_64', 'any'.

For example, distribution-1.0-1-py27-none-any.whl is the first build of a package called 'distribution', and is compatible with Python 2.7 (any Python 2.7 implementation), with no ABI (pure Python), on any CPU architecture.

The last three components of the filename before the extension are called "compatibility tags." The compatibility tags express the package's basic interpreter requirements and are detailed in PEP 425.