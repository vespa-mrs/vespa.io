# Pre- and Post-Install Utilities
This document describes
[source:/trunk/vespa/check_dependencies.py Vespa's dependency checker],
the [source:/trunk/vespa/requirements.txt requirements.txt file] that it uses,
and the pre-install utility.

These utilities are primarily intended for end users, but they can also
be useful to Vespa developers when troubleshooting a user's Vespa installation.

## The Pre-Install Utility
The pre-install utility was written to address one of the most common problems
for people installing Vespa. Users would often have multiple Pythons installed
and somehow install Vespa's dependencies to one Python and Vespa to another,
with the result that Vespa would report to the user that its dependencies
were not installed.

The pre-install utility ensures that a desirable Python is first in the
user's PATH during installation. (See the code for details -- it's
well-documented.) As long as users follow the admonition to run all the
install commands in the terminal window where the pre-install utility ran,
they should get their dependencies and Vespa installed to the correct Python
100% of the time.

[source:/trunk/vespa/create_shortcuts.py Vespa's shortcut creator] creates
shortcuts that contain absolute paths the Python executable (rather than
just `python`), so once Vespa is installed it's insulated from PATH changes.

## The Post-Install Utility (Dependency Checker)
Once Vespa's installation is complete, the dependency checker can ensure that
things look the way they're supposed to.

The dependency checker relies on `requirements.txt`. That's a valid
[pip requirements file](https://pip.pypa.io/en/stable/user_guide/#requirements-files),
although due to our complicated dependencies we can't actually use it as such.

I wrote it in the hopes that we would be able to install all of Vespa's
dependencies like so --
```
pip install -r requirements.txt
```

I learned that we can't, due to various quirks. (`numpy` & `scipy` aren't pip-installable
on Windows, PyWavelets isn't pip-installable on OS X and Linux, wxPython isn't
pip-installable anywhere, etc.) We can hope that someday all our dreams
will come true, but in the meantime we're stuck with a grimy reality that could
use a bath.

Nevertheless, `requirements.txt` is a good place to describe Vespa's dependencies
for two reasons. First of all, it positions Vespa well for a future where
we _can_ use it the way it was meant to be used. Second, it leverages the predefined
[requirements.txt syntax](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format)
and the [PyPI module for parsing that syntax](https://pypi.python.org/pypi/packaging).








