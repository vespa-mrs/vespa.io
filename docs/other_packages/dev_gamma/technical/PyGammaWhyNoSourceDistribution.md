# Why There is No Source Distribution of PyGamma on PyPI
A  [source distribution](https://docs.python.org/2/distutils/sourcedist.html)
of a package is created with `python setup.py sdist`.
It creates a tarball (or zip file on Windows) that contains files that one
can download and unpack, and then run `python setup.py install`.

Source distributions make a lot of sense for pure Python packages, or for 
packages that can be compiled easily on their target platform(s). PyGamma is
a different animal. It's principally C++ code, and that code can only be 
compiled with our special build process. A source distribution wouldn't
do anyone any good.

We could provide the Python source + prebuilt binaries for each platform
as a source distribution. That's possible, but would require some care to 
create. 

If someone really wants to build and install from source, they can 
get the code from our public repository. 

