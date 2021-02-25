# Printing to the Console (`stdout`) from a Pulse Sequence

# Printing to the Console (`stdout`) from a Pulse Sequence
When debugging a pulse sequence's code (sequence and binning), it's useful
to be able to see the output of `print` statements. This document tells you
how to enable that.

## Where *Not* to Look
In the lower left of the pulse sequence editor's test tab there's 
[attachment:screenshot.png a "console" window] that starts with the 
message "Welcome to the Pulse Sequence Editor". 
*The output of Python `print` statements will not appear there.* 
That console only displays specific messages from the pulse sequence editor. 

## So Where is stdout?
When you run Simulation from a desktop shortcut, it executes Python in 
a shell that's either hidden or disappears as soon as the application
exits. (The behavior depends on which operating system you run.) A slight
alteration of the command in the desktop shortcut will allow you to 
see the command shell. 

Specific instructions for Windows, OS X and Linux are below.

## Windows XP
1. Right click on the Simulation desktop shortcut. Windows will display 
 a popup menu.
1. Select "Properties" on the popup menu. Windows will display a dialog
 containing the properties of the shortcut.
1. The "Target" contains the command you want to modify. Copy that to the
 clipboard and paste it into Notepad. It will look something like this:
    ```
     C:\python25\pythonw.exe "C:\Python25\Lib\site-packages\vespa\simulation\src\main.py"
    ```
1. Change `pythonw.exe` to `python.exe`
1. Save that file to `C:\simulation.bat`
1. Open a command prompt (under Start/All Programs/Accessories/Command Prompt)
1. Type `C:\simulation.bat` and hit enter. Windows will launch Simulation
 from the command prompt you started.
 
Messages sent to stdout will be visible in the command prompt.


## OS X
1. Start a command prompt (a.k.a "Terminal" in your `Applications/Utilities`
 folder).
1. Paste in this command and hit enter: `~/Desktop/Simulation.command`
 
Messages sent to stdout will be visible in the command prompt.


## Linux
1. The Desktop shortcut that launches Simulation is actually called 
 `Simulation.desktop` (full path: `~/Desktop/Simulation.desktop`). Open
 that file in a text editor.
1. Find this line:
    ```
     Terminal=false
    ```
1. Change it to this:
    ```
     Terminal=true
    ```
1. Save your changes.
1. Double click on the desktop shortcut to launch Simulation. 

Messages sent to stdout will be visible in the command prompt that launches
when you double click on the shortcut. Note that the command prompt will 
automatically close when you exit the application, so if you need to save
what's displayed there, don't forget to save it into a text document before
closing Simulation.
