# The Vespa Data Directory
Vespa uses a data directory to store your preferences, database and other things. This directory is invisible under most circumstances and you shouldn't ever need to look at it. In case you do, here's how to find it. The location differs depending on your operating system and is user-specific.

 * Windows XP: `C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Vespa`
 * Windows >= Vista: `C:\Users\%USERNAME%\AppData\Local\Vespa`
 * Linux: `~/.Vespa`
 * OS X: `~/Library/Application Support/Vespa`
   
Under Linux and OS X, `~` stands for your home directory.

## Reset to Factory Settings
When a Vespa application starts, it detects any missing files or directories 
in the Vespa data directory and recreates them from scratch if necessary. 
That means that one can delete any individual files in the data dir or even 
the entire data directory itself and Vespa will deal with that gracefully.
(Provided you do the deleting while Vespa is not running.)

Of course, deleting the INI files will lose any preferences stored in them
(not a big deal). And deleting the database will destroy all experiments, 
pulse seqs, metabs, RF pulses, etc. that the user has created (possibly a 
very big deal), so use with caution.


## How to Get to the Data Directory under Windows (if AppData directory is hidden)
When using Windows with default settings, the directory that contains the
Vespa data directory is invisible from both the command line and Windows
Explorer. 

Here's a method for getting to that directory that anyone should comfortable
with.

1. For Windows XP, copy this to the clipboard:[[br]]
 `C:\Documents and Settings\%USERNAME%\Application Data\Local Settings\Vespa\`

1. For Windows >= Vista, copy this to the clipboard:[[br]]
 `C:\Users\%USERNAME%\AppData\Local`

1. Open "My Computer"

1. In the address bar where it says "My Computer", paste the directory you copied above. The  [attachment:screenshot.png attached screenshot] shows what I mean.

1. Hit enter.


