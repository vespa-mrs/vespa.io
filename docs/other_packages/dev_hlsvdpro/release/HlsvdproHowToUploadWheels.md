# How To Upload HLSVDPro Wheels
This document describes how to upload HLSVDPro wheels to PyPI.

*Note. Once you load a version to PyPI, the same version can NOT be reloaded. So be careful.*

Just FYI - One workaround is to upload 'release candidate' versions, e.g. if you upload 1.2.15rc1 initially you can still upload 1.2.15 later.  

## Introduction
As of this writing, uploading wheels requires some help from 3rd party
packages. See the "One-time Setup Steps" section below if you have not already
set these packages up, yet.

If you find these steps to be too much trouble, remember that you can always
upload the wheel files to scion instead. That would create a small
inconvenience for the user.

If the HLSVDPro wheels are on PyPI, the user can type
`pip install hlsvdpro` and pip will find and install the right version of
HLSVDPro for the user's system.

## Credit
Some of the information in this document comes from here:
https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/

## Assumptions
This document assumes the following --
 * You have already built the HLSVDPro wheels
 * You have an account on the test PyPI
 * You have an account on the production (real) PyPI
 * You have followed the one-time setup steps in this document (see below)

## Uploading Wheels
Upload to the test PyPI if you want --
```
twine upload --repository testpypi dist/*
```

You can find this upload at [https://test.pypi.org/project/hlsvdpro/] 

To use this test version to upgrade your version of HLSVDPro, type:
```
pip install --index-url https://test.pypi.org/simple hlsvdpro==2.0.0rc3
```


*When you feel ready, upload to the production PyPI --*
```
twine upload dist/*
```

You can find this upload at [https://pypi.python.org/pypi/hlsvdpro] 

It's perfectly OK to upload just one file, e.g. --
```
twine upload dist/hlsvdpro-2.0.0-py37-none-win_amd64.whl
```

If `twine` isn't in your `PATH`, try using `python -m twine` instead of
just `twine`.

## Changing Metadata
If you change any of the metadata in `setup.py` (e.g. the description,
maintainer email, etc.), you'll need to re-run the `setup.py register` step
for that information to appear on PyPI.

The metadata is stored in the `HLSVDPro.egg-info` directory that's a
sibling of `setup.py`. In my experience it gets overwritten when one
runs the  `setup.py register` step. If you're feeling paranoid, you 
might want to delete that directory by hand after a metadata change.

If this does not work, then doing a full twine upload will also update any
metadata. You can use a throw-away version number like 0.9.dev10 to test
this on TestPyPI.

## One-time Setup Steps
These are steps that only need to be done once, not every time you
upload a wheel.

### Install twine
Because Python tools are not where they need to be yet, we need to rely
on a 3rd party package called twine. Install it like so --

```
pip install twine
```

### Create the PyPI Config File
Create the file `.pypirc` in your home directory and populate it with the
text below, replacing the stuff in <angle brackets>.

```
[distutils]
index-servers=
    pypi
    testpypi

[testpypi]
repository = https://test.pypi.org/legacy
username = <your test user name goes here>

[pypi]
repository = https://upload.pypi.org/legacy
username = <your production user name goes here>
```

You can also include your password in that file, but that means your password
will be stored in plain text on your hard drive. I cannot recommend this.

If you don't put your password in .pypirc, you'll be prompted for it when
you run `setup.py register` or use `twine` to upload wheels.

### Register the Project
Register on the test PyPI first --
```
python setup.py register -r test
```

If that goes well, you can register on the production (real) PyPI --
```
python setup.py register
}}}