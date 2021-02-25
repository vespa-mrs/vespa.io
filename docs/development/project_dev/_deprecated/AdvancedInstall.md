# Advanced Install
These instructions for installing Vespa are for users who are
comfortable using the command line and finding and installing
Python packages.

## Step 1 - Install Python
Vespa will work with any 64-bit Python 2.7. Some possible sources for
Python are [Python.org](https://www.python.org) (of course!),
[Continuum Miniconda](http://conda.pydata.org/miniconda.html),
[Continuum Anaconda](https://www.continuum.io/downloads),
or, if you're on Linux, the Python from your package manager.

Vespa's dependencies are listed in the file
[source:/trunk/vespa/requirements.txt vespa/requirements.txt]. If you're
familiar with `pip`, please note that it's *not* possible to use this
requirements file with pip's `-r` option because not all of Vespa's
dependencies are pip-friendly.

*(Optional)* You may want to add your Python and Python\Scripts paths to your system path for convenience in launching Python or other scripts.

## Step 2 - Check Your Python
Download [export:/trunk/get_python_info.py get_python_info.py] and
run it with this command --
```
python get_python_info.py 1
```

It will tell you whether or not Vespa is compatible with your Python.

## Step 3 - Upgrade pip
Ensure you're running the latest version of pip. (Older versions of pip
have trouble with some of the steps in this guide.)

```
python -m pip install --upgrade pip
```

## Step 4 - Install Vespa's Easy Dependencies
These packages are easy to install with pip on all the platforms
Vespa supports --
```
pip install packaging pydicom==0.9.9 pygamma hlsvdpro lmfit pypubsub vespa-suite
```

## Step 5 - Install Numpy, Scipy, and Matplotlib
Under *OS X and Linux*, you can install Numpy, Scipy, and matplotlib via `pip` (on OS X) and the
package manager (on Linux).

On *Windows*, we suggest installing Numpy and Scipy from the
[wheels provided by Christoph Gohlke](http://www.lfd.uci.edu/~gohlke/pythonlibs/). Note. There is a link that describes how to install wheels on Christoph's site, but we also provide it here for your convenience [How to Install Wheels](https://pip.pypa.io/en/latest/user_guide/#installing-from-wheels)

Once Numpy and Scipy are installed, you can `pip install matplotlib==2.2.3` since as of version 0.10.0  Vespa requires this version.

## Step 6 - Install PyWavelets
Under *Windows*, you can install this with `pip install pywavelets==0.3.0`.

Under *Linux*, get it from your package manager.

Under *OS X*, use the
[PyWavelets 0.3.0 wheel that we provide](https://scion.duhs.duke.edu/vespa/analysis/wiki/PyWaveletsOsx).

## Step 7 - Install wxPython
Under *Linux*, get wxPython 4.0.4. It might be under a name like 'python-wxgtk'.

Under *Windows and OS X*, install wxPython 4.0.4 from one of the packages
provided on [wxPython.org](http://wxPython.org).

## Step 8 - Install FFTW3 (Linux Only)
*Linux* users, use your package manager to install the FFTW3 runtime
library. Look for it under a name like `libfftw3` or just `fftw`.


## Step 9 - Finish the Vespa Install
Run this command --
```
python -m vespa.check_dependencies
```

If that goes OK, run this command --
```
python -m vespa.create_shortcuts
```

## You're Done!
Double click on one of the shortcuts to start using Vespa!

Don't forget to
[join the Vespa mailing list](http://groups.yahoo.com/neo/groups/vespa-mrs/info).
We'll see you there.


Enjoy,[[BR]]
-- The Vespa Team