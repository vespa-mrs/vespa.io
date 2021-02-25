# Developer Setup
This explains what you need to set up Vespa if you want to make changes to
the code, GUI and/or database. It assumes you know a bit about Python, the
command line, how to use SVN, etc.

## Prerequisites
Prerequisites are described in the [installation instructions](/wiki:Installation/).
You can skip
the prerequisites if all you want to do is look at the code (or run the
dependency checker described below). But in order to _run_
Vespa, you need to satisfy all of the prerequisites.

In addition, you also need a Subversion client.

When working out your dependencies, you might find Vespa's dependency
checker useful --
```
python -m vespa.check_dependencies
```

If you've already installed Vespa the "normal" way on your machine, you need
to uninstall it before creating a development setup. (If you don't, you'll have
two copies of the Vespa code on your machine and both you and Python will get
very confused as to which set of code is executing.) To uninstall, follow
[SetupPy#UninstallingorUnwindingaBrokenInstall the uninstall instructions].
Removing the data directory is optional.


## Getting the Source Code from SVN
1. Decide where your source tree is going to live. For this example, I'm
    going to install in `/home/me/work`
1. Check out the Vespa source code. If you have read/write access:
```
    svn co https://scion.duhs.duke.edu/svn/vespa/trunk  /home/me/work/vespa
```
    For guest (read-only) access, which everyone has:
```
    svn co http://scion.duhs.duke.edu/guest_svn/vespa/trunk   /home/me/work/vespa
```

1. Find your Python's `site-packages` directory and add a plain text file
    called `vespa.pth` that contains the
    fully-qualified path to your `vespa/vespa` directory (which contains
    `__init__.py`, the directories for `analysis`, `simulation`, etc.).
    Here's the contents of `vespa.pth` for this example --
```
    /home/me/work/vespa/vespa
```
    This command should tell you where `site-packages` resides --
```
    python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"
```
    It might be called `dist-packages` under some Linux versions.
1. *Optional:* If you're using Analysis, you might want some sample data with which
    to work. For now, that's in a
    separate Subversion repository from vespa. Vespa doesn't care where these files live on your
    local hard drive, so you
    can put this directory anywhere you like. In this example, I'm going to
    leave it under `vespa`.
```
    svn co https://scion.duhs.duke.edu/svn/sample_data    /home/me/work/vespa/sample_data
```

You're ready to start hacking!

## Running Vespa Applications
To run any of the apps, type
```
   python /home/me/work/vespa/vespa/NAME_OF_APP/src/main.py
```
where NAME_OF_APP is one of `pulse`, `simulation`, `analysis`, or `priorset`.
Depending on which Python you're using, you might need to use `pythonw`
instead of `python`.

## Debug Settings in vespa.ini
Developers usually want to add some [IniFiles#DebugEntriesinvespa.ini useful debugging settings] to `vespa.ini`.

## User Interface Modifications (wxPython and wxGlade)
If you want to modify the GUI, you'll also need to install
[wxGlade](http://wxglade.sourceforge.net/).

### wxGlade on WindowsIf you're a Windows user, be sure to
[InstallingWxGladeUnderWindows read this note about installing wxGlade properly].

### All wxGlade UsersMake sure you
[WxGladeCustomControls read this note about configuring wxGlade]
to use our custom controls, regardless of what platform you are using.

Note that the technical documentation has a whole section on wx-related topics, including [WxTipsBugsAndQuirks tips, bugs and quirks].

## Database Modifications

Editing the database is described in ChangingTheDatabaseStructure.
