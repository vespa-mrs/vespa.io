# GAMMA/PyGamma Version Management
GAMMA and PyGamma necessarily share the same version number, although they
follow very different release strategies. This document describes how we
manage versioning and releasing GAMMA and PyGamma.

## The VERSION File
All parts of GAMMA/PyGamma (Makefiles, Python code, etc.)
get their version number from one source -- the file
[browser:trunk/VERSION gamma/VERSION].

## PyGamma Drives the Versioning...
The Vespa project is really only interested in PyGamma since that's what
Vespa needs to run. PyGamma is GAMMA plus a wrapper and an installer, so
it's possible for PyGamma to change while GAMMA remains the same. (This was
the case for the 4.2.1 release.)  In this case, the GAMMA version number
changes even though nothing has changed about GAMMA.


## ...But GAMMA Drives PyGamma
Despite the fact that PyGamma drives the versioning, we can still use version
numbers to mark significant changes in GAMMA. PyGamma can't exist without
GAMMA, so any significant change to GAMMA would result in a new version of
PyGamma anyway.

This combination allows us to release new PyGamma versions without waiting
for a change to GAMMA, while ensuring that changes to GAMMA are reflected
in PyGamma.


## GAMMA Releases
Currently and for the foreseeable future,
the only way to get GAMMA is via SVN. That being the case, anyone who gets
GAMMA and has questions about it can always report the SVN version to us. We
don't really have GAMMA releases. Changes are applied continuously to trunk.

## PyGamma Releases
PyGamma releases are more formal since we provide prebuilt binaries for them.

PyGamma gets its version number from GAMMA (specifically, from the file
`gamma/VERSION`). When we release a new version of PyGamma, we're also
"releasing" a new version of GAMMA, since the two share their version file.

When we release a new version of PyGamma, all of the prebuilt binaries
we provide have to be rebuilt _even if GAMMA hasn't changed_.
Rebuilding the binaries is necessary because they embed the GAMMA version number.

## How to Release a New Version of PyGamma
1. Update `gamma/VERSION` and `gamma/NEWS`. Update `VERSION` _before_ you
 build since the version number gets embedded in the build output.
1. Build a wheel for each of [PyGammaHowToBuildWheelsForWindows Windows], 
 [PyGammaHowToBuildWheelsForOsx OS X], and [PyGammaHowToBuildWheelsForLinux Linux].
1. Commit the VERSION file and NEWS files.
1. Create an SVN tag for the release with a command like this:
```
 svn copy  https://scion.duhs.duke.edu/svn/gamma/trunk           \
           https://scion.duhs.duke.edu/svn/gamma/tags/TAG_NAME   \
           -m "TAG COMMENT GOES HERE."
```
 For example:
```
 svn copy  https://scion.duhs.duke.edu/svn/gamma/trunk           \
           https://scion.duhs.duke.edu/svn/gamma/tags/4_2_1      \
           -m "Tagging for 4.2.1 release."
```
1. Let PyPI know that the package has changed --
```
 python setup.py register 
```
1. [PyGammaHowToUploadWheels Upload the wheel files].
1. You might want to announce the new version on the Vespa email list.