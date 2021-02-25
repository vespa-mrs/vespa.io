# VeSPA- General Project FAQ Page
Questions and answers specific to the VeSPA project and sometimes a bit more ...
----
## Index
*[#HowdoIdownloadVespa How do I download Vespa?]*

*[#HowdoIinstallVespa How do I install Vespa?]*

*[#WheredoIfindApplicationspecificFAQs Where do I find Application specific FAQs?]*

*[#SetupsaysIhaven'tgotthedependenciesinstalled(scipy,numpy,etc.),butIdo! Setup says I haven't got the dependencies installed (scipy, numpy, etc.), but I do!]*

*[#InstallProblem1-IssuewithwidgetsorwxPython Install Problem 1 - Issue with widgets or wxPython]*

*[#HowtoRunApplicationsfromCommandLineinLinux How to Run Applications from Command Line in Linux]*

----
## Questions and Answers
### How do I download Vespa?You can download Vespa from the [Downloads](/wiki:Downloads/) page.

### How do I install Vespa?Complete instructions for installing Vespa are on the [Installation](/wiki:Installation/) page.

### Where do I find Application specific FAQs?Each application has its own wiki that contains a extensive information and links. Some are still under construction but will be included when they are released in beta. FAQs for each can be found here:  [simulation:FAQ Simulation FAQs], [rfpulse:FAQ RFPulse FAQs], Analysis FAQs

### Setup says I haven't got the dependencies installed (scipy, numpy, etc.), but I do![This was in response to a Windows user question] - One reason for this is that you may have more than one Python version installed, and when you install a Python package for one of our dependencies, it is installed to only one Python version at a time. In other words, if you have Python 2.5, 2.6 and 2.7 on your computer and you install matplotlib, it is installed for just one of those Pythons. It isn't installed "globally". If you want matplotlib to be available to all 3 versions of Python, you have to install it 3 times, once for each Python.

Under Windows, when you install a Python package from an installer (an EXE that you double click), it can see that you have multiple Pythons and it guesses which Python under which it should install itself. It gives you the option to change this guess during the installation, but it's easy to overlook. So, for example, you may installed matplotlib and scipy to a different Python than the one you're trying to use with Vespa.

Vespa uses the first Python it finds in your path. If you open a command prompt and type 'set path', it will show you the current path, and that will tell you which Python comes first. Another way to find out which Python is first in your path is with this command:

```
   python -c "import sys; print sys.executable"
```

That should print something like "c:\python26\python.exe".

You can test whether or not Python can import a package with a command like this:

```
   python -c "import matplotlib"
```

If matplotlib is installed, that will return silently. If it's not installed, you'll get a loud & clear import error like this:

```
   python -c "import this_does_not_exist"
   Traceback (most recent call last):
     File "<string>", line 1, in <module>
   ImportError: No module named this_does_not_exist
```

Those commands should give you the tools you need to figure out what is installed where. However, if the Vespa installer says that matplotlib isn't installed, it definitely is not for that version of Python. The Vespa installer just tries the same test suggested above: import something and see whether or not it fails.


### Install Problem 1 - Issue with widgets or wxPythonAt this moment (March 2013), we recommend that you use wxpython version 2.8.x (more specifically 2.8.11.x or later). We develop Vespa using 2.8.12.1 under Windows, for example. There are changes under wxpython 2.9.x for which we have not tested/modified Vespa to account for. Part of this is time on our part, and part of it is that wx 2.9 is still sort of a moving target with the changes they make.  So we've decided to stick with wx 2.8.x versions for the time being.

Try uninstalling wxpython 2.9 and installing wxpython 2.8.12.1 (or so) to see if that fixes these problems.

More information (useless or otherwise) - We would prefer to require wxPython 2.8.11.0 because that's the first version that includes a version of floatspin.py that contains the patches we submitted. However, as of December 2012, the most current version of EPD (7.3) is still on wxPython 2.8.10.1 which is not sufficiently recent. Until EPD provides a more recent wxPython, we can't require 2.8.11.0.

Here is a link to some more general comments on the versions of dependency modules required for Vespa.

[Vespa Dependencies version information](http://scion.duhs.duke.edu/vespa/project/wiki/Dependencies)

### How to Run Applications from Command Line in Linux
Vespa is installed in site-packages, or dist-packages under some Linux distros. There's a Vespa utility that can help you find them if you don't mind running a little Python. Enter 'python' at a bash prompt and then enter the following, hitting enter after each of the two lines --

```
import vespa.common.util.misc as util_misc
util_misc.get_vespa_install_directory()
```

That will print out something like this --
```
>/usr/local/lib/python2.6/dist-packages/vespa
```

That's the main Vespa path. The individual apps are under that directory under the names simulation, analysis, priorset and rfpulse. To invoke each app, start [app_name]/src/main.py. For example, to start Simulation --

```
>python /usr/local/lib/python2.6/dist-packages/vespa/simulation/src/main.py
```

If you're interested in learning more about this, there's a Vespa install utility called create_desktop_shortcuts.py that creates the Desktop shortcuts for Linux as well as OS X and Windows. You can see that online here:
[http://scion.duhs.duke.edu/vespa/project/browser/trunk/create_desktop_shortcuts.py]
