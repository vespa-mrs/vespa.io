## How to Release a New Version of HLSVDPRO
1. Update the `VERSION` and `NEWS` files. 
1. [HowToBuildWheels Build wheels] for each platform.
1. Let PyPI know that the package has changed --
```
 python setup.py register 
```
1. [gamma:wiki:PyGammaHowToUploadWheels Upload the wheel files] using these
 instructions for PyGamma.
1. Commit the VERSION file and NEWS files.
1. Create an SVN tag for the release with a command like this:
```
 svn copy  https://scion.duhs.duke.edu/svn/hlsvdpro/trunk           \
           https://scion.duhs.duke.edu/svn/hlsvdpro/tags/TAG_NAME   \
           -m "TAG COMMENT GOES HERE."
```
 For example:
```
 svn copy  https://scion.duhs.duke.edu/svn/hlsvdpro/trunk           \
           https://scion.duhs.duke.edu/svn/hlsvdpro/tags/4_2_1      \
           -m "Tagging for 4.2.1 release."
```
1. You might want to announce the new version on a mailing list.
