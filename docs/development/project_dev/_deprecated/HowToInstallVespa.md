# How To Install Vespa for Python 3.x
These are our most straightforward Vespa install instructions. Note - these are for Vespa version 1.0.x and later, which runs only in Python 3.7 at this point.

The following instructions are based on using the conda 'miniconda' installation to install the dependencies that Vespa requires. We are only installing the packages we need for simplicity. You could install these packages yourself using other means, but this HowTo uses conda.  Here we go. 
You'll need to use the command line for most of these instructions. Be careful of typos.

## Step 1 - Install Python
_Vespa uses 64-bit Python 3.7. We recommend using an automated Python distribution called Miniconda. These 'Simple Install' instructions assume that you used Miniconda to install 64-bit Python as described below._

Install the 64-bit Miniconda3 package for your system from here:
http://conda.pydata.org/miniconda.html

As of September 2020, this will install conda with a base Python of version 3.8, but Vespa requires Python 3.7. So, fire up the conda base command window and create your first environment. This is simple (see below) and it is good to do your actual work in Python outside of the base environment.

Create an environment called python37 (or whatever you want to name it) by typing:
```
conda create --name python37 python=3.7
```
conda will think for a bit, then list the files it will install and ask you to confirm. Type 'y' and return. Conda will then download packages and install them.

The last step here is to activate the new python37 environment by typing:
```
conda activate python37 
```

## Step 2 - Install Vespa's Dependencies, Round 1
Run this command --
```
conda install numpy scipy matplotlib wxPython configobj
```

Then run this command --
```
conda install -c conda-forge lmfit pydicom pypubsub
```

Then run this command --
```
pip install packaging pygamma vespa-suite
```

## Step 3 - Finish the Vespa Install
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
[join the Vespa Forum on MRS Hub](https://forum.mrshub.org/c/mrs-software/vespa/11).
We'll see you there.


Enjoy,[[BR]]
-- The Vespa Team


# (deprecated) How To Install Vespa for Python 2.7These instructions are for Vespa version 0.11.x or earlier. These versions will be removed from PyPI as some point in the future. We recommend you transition to Vespa 1.0.x or later which only runs on Python 3.x


You can follow either of our two guides to install Vespa.

We suggest [SimpleInstall the simpler install guide] if you're 
new to Python and/or you're not comfortable
finding packages for your platform.

Feel free follow our [AdvancedInstall guide for advanced users] if you're experienced with Python.


*OS X users*, we are aware (and maybe you are too) that Python comes
preinstalled as part of OS X. The general consensus is that the preinstalled
Python belongs to OS X
and you shouldn't use it in case you change it in some way that breaks
OS X (and vice versa). We recommend that you install
another Python instead of using the preinstalled, system Python. This is
covered in the installation guides we've provided.