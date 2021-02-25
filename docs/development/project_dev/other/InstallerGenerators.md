# Installer Generators
by Philip

Update March 2010: there was a talk at PyCon 2010 on "Cross platform application development and distribution": 
http://us.pycon.org/2010/conference/schedule/event/38/

Here's round one of my research on tools with which to build a Windows
graphical installer for VeSPA. My research consisted of reading a lot of
discussions to expose myself to a decently-sized collection of opinions. One
phrase I read over and over again was "there's a learning curve".

A quick way to narrow the field is to discard the non-free products. The only
non-free product about which I read much was Install Shield which is
"expensive" and unpopular. I also saw a few references to Visual Studio
Installer, but it's not part of the free VS Express Editions.

Of the free products, there are three leading contenders, plus a dark horse
and one non-installer: WIX (Windows Installer XML), NSIS (Nullsoft Scriptable
Install System), Inno Setup, the dark horse InstallJammer and the
non-installer py2exe. Each is described in more detail below.

WIX and NSIS seem to be the most popular install generators. InstallJammer is
notable for being the only one to create cross-platform (Windows & *nix)
installers.

*Note:* Since writing this, I've learned that Python's `distutils` can 
create MSIs, so WIX's main advantage probably just went out the window. More 
research when I have time.

*Note 2:* If you do create an MSI with Python, be sure to test it on a fresh
Windows install to see if you run into 
[a problem like this one](http://code.google.com/p/pydicom/issues/detail?id=92).

http://docs.python.org/distutils/apiref.html#module-distutils.command.bdist_msi

### About MSIs
WIX is different from the rest of these tools because WIX creates a Windows
MSI. An MSI is a data file that one feeds to the MS installer. Sysadmins at
big companies love 'em because they're friendly to enterprise-type services
like Windows Active Directory deployment. Obviously, that's not our target
market.

I don't know anything about MSIs but my guess is that they're similar to a
package management system under *nix. For instance, I'll bet if I install
something through an MSI, it will automatically show up in the Windows Control
Panel Add/Remove Software list, whereas something installed by other means
won't (or won't without some special effort). And MSIs are probably smarter
about dealing with whatever security policies Windows has these days.

## WIX
[WIX](http://wix.sourceforge.net) is an open source project from Microsoft.
Microsoft's "open" offerings often aren't, but this one seems legit.

I've seen WIX described as a "thin wrapper" around the MSI format which is
reputedly complex and ill-documented. The moral of the story seems to be, "Be
prepared to learn a lot about MSIs."

This comment summed up a lot of the ones I read about WIX: "WIX sounded like a
great idea at first, but we found that it's like a lot of things from
Microsoft: easy to do the 80% that most people need, but you better pray
you're not in the camp that needs the other 20% because extending it adds
mind-numbing complexity to your WIX and build scripts."

WIX requires the .NET Framework 2.0 and its Service Pack 1 to run. I suspect
these things are common, but I don't know.

Here's a feature list for WIX: 
http://wix.sourceforge.net/faq.html

## NSIS
In contrast to WIX, [NSIS](http://nsis.sourceforge.net) creates install EXEs
that are just like any other Windows EXE. It offers more flexibility than WIX
but comes with the cost of learning the NSIS scripting language. I
didn't see anything that suggested the scripting language is easy or a treat
to use. One person called it "cumbersome".

NSIS grew out of WinAmp and has been around for a long time -- long enough to
have its manual translated to French and Polish and to offer commercial
support. NSIS users include Adobe, Google and Yahoo. It's got  a lot of users
and a Wiki with examples, bunches of plugins, etc.

Here's a complete feature list:
http://nsis.sourceforge.net/Docs/Chapter1.html#1.3

## Inno Setup
[Inno Setup](http://www.jrsoftware.org/isinfo.php) has been around for a while
too (since 1997). It's a bus factor 1 project, but it is open source and seems
popular enough to maybe get picked up by the community should anything happen
to Jordan Russell (the "JR" in jrsoftware.org).

The Web site and documentation, while thorough, offer less than the NSIS site,
Wiki and documentation.

Custom features must be written in Pascal (Inno Setup is written in Delphi).

## InstallJammer
[InstallJammer](http://installjammer.com/) is another bus factor 1 project.
It's also open source, but I'm not sure it has enough traction to survive in
the absence of its author.

I don't see a lot of people talking about it, but those that do say
nice things.

It's main claim to fame is that it is cross platform, although it does not yet
support OS X. While cross platform support is an interesting and unique
feature, I'm not sure that it benefits us that much.

## py2exe
[py2exe](http://www.py2exe.org/) isn't an installer _per se_, but it "converts
Python scripts into executable Windows programs, able to run without requiring
a Python installation."

It's open source, quite popular and has a solid community behind it.

One thing that gives me pause is the page that lists some packages which may
malfunction after being run through py2exe. The list could also be titled
"Modules that Analysis Uses", since just about all of them are on there
(cElementTree, ConfigObj, ctypes, MatPlotLib, SciPy, NumPy, and wxPython):
http://www.py2exe.org/index.cgi/WorkingWithVariousPackagesAndModules

I found a note that says not to use Python 2.6.2 when running py2exe due to http://bugs.python.org/issue4566

## Do We Need A Graphical Installer?
Now that we've examined solutions, let's examine the problem.

One of the big features provided by an install program is an
installation-specific toolbox. In our situation, we'll already have one
available in Python's distutils module. (That's assuming that the user has
read our prerequisites and at least installed Python. That assumption may or
may not be beyond our handholding limit; I'm open for discussion on the
topic.)

Python's distutils does a lot of work that we don't want to replicate (such as
finding the appropriate site-packages directory into which to copy .py files).
In addition, most or all of our dependencies will be Python-based, so the
easiest and most accurate way to check that they're present will be to attempt
to import the library from Python code (e.g. 'import wx').

Most of what we need from an install program, therefore, is already present
within Python, and using Python for a lot of installation-related tasks is not
only smart but necessary. What's more, if I need to do some custom scripting
at install time and I can do it in Python or in some install program's
homegrown scripting language, I'll choose Python every time.

That doesn't leave a lot for a graphical installer to do except (1) check that
Python is installed and (2) keep Windows users from being forced to
use a command shell to run `python setup.py install`. Since Windows users
typically have little exposure to the command line, the value of (2) is
considerable, but the cost might be too.


## Conclusion
### No to a Graphical Installer
I hope I'm not being naive, but I don't see that creating an installer buys us
much. Nothing I read about these packages left me excited about any of them,
and learning the intricacies of the MSI format or NSIS' scripting language
doesn't seem likely to pay dividends beyond this project.

If I had to choose among the installer generators, I'd say that NSIS is the
best choice. I'd check out WIX too since 95% of the work of our installer will
be pushed to distutils and therefore the WIX config should be pretty simple.
Hopefully our needs would fall in that "easy...80%" and as advised we should
"pray you're not in the camp that needs the other 20%".

### Tentative Yes to py2exe
I'm intrigued by py2exe because it looks a lot easier to use than any of the
other applications mentioned here. It seems worth trying out since it is a low
cost investment that obviates the need for preinstalling Python and 
allows Windows users to stay in their comfort zone.
