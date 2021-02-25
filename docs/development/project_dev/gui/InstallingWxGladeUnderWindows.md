# A Special Note for Using wxGlade under Windows
wxGlade can be installed from source or via a setup.exe. The latter is the default
option if one visits the sourceforge download page while using Windows. Once
you've installed from EXE, you can run wxGlade by double clicking on a
desktop icon that the installer creates for you.

*Don't use the EXE version.* This version has Python and wxPython "baked
in" and it uses old versions of them. Specifically, wxGlade 0.6.3 uses 
Python 2.3.5 and wxPython 2.8.3.0. Both of these fall short of our 
minimum versions (2.5.0 and 2.8.8 respectively). 

More to the point, if any of our custom controls use Python features not
present in 2.3.5, they'll silently fail to load. 

## Installing wxGlade from Source
To install wxGlade from source, first download the .zip file, unzip, and
run the following command at a command prompt:

```
python setup.py install 
```
 
For me, that created the directory `C:\Program Files\wxglade`, and I run
wxglade by starting a command prompt and typing the following:
```
python "c:\Program Files\wxglade\wxglade.py"
```

Since I'm lazy and don't want to type this, I created a batch file to
encapsulate this command. Here's the contents of `wxglade.bat` on my system:

```
python "c:\program files\wxglade\wxglade.py"  %1
```

The batch file (which is in my PATH) allows me to type this to open a wxGlade data file:

```
wxglade whatever.wxg
```


If you prefer a Desktop shortcut that you can double click, create one and 
set the target to this:

```
C:\Python25\python.exe "c:\program files\wxglade\wxglade.py"
```

That will start a DOS prompt which launches the wxGlade GUI. If you don't 
like seeing the DOS prompt and all of the startup messages (which are vital
for debugging problems with custom controls but uninteresting otherwise), 
change "python.exe" in the target above to "pythonw.exe".







