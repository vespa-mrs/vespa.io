# Upgrading to Version 0.1.6
Vespa version 0.1.6 adds a dependency on a Python package called
`multiprocessing`. That's included in Python 2.6 and above, but not in 2.5. If
your version of Python doesn't provide multiprocessing, you'll need to add it.

The easiest way to figure out whether or not `multiprocessing` is
already installed is to try to install Vespa. If `multiprocessing`
is missing, you'll get a message like this -- 

```
Sorry, the installation can't begin because the following dependencies are unmet:
 - multiprocessing: the required version is >= 0.0.0; it is not installed.
```

The install will stop there. There's no harm done; just install `multiprocessing`
and then re-run the Vespa install.


## Installing `multiprocessing`
*Windows* users should [download this multiprocessing executable](http://pypi.python.org/packages/2.5/m/multiprocessing/multiprocessing-2.6.2.1.win32-py2.5.exe) and
double click on it to install.


*Linux* users, check to see if your package manager provides
`multiprocessing`. If not, follow the instructions for OS X.

*OS X* users, [download this multiprocessing tarball](http://pypi.python.org/packages/source/m/multiprocessing/multiprocessing-2.6.2.1.tar.gz) and
follow the [OsxInstallCommandLine instructions for installing a package from the command line].
