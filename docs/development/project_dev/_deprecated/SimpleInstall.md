# Simple Install
These are our most straightforward Vespa install instructions. Note - these are for Vespa version 0.10.x and later.

You'll need to use the command line for most of these instructions.
If possible, we suggest that you copy and paste the commands in this guide
to reduce the possibility of typos.

## Step 1 - Install Python
_Vespa uses 64-bit Python 2.7. We recommend using an automated Python distribution called Miniconda. These 'Simple Install' instructions assume that you used Miniconda to install 64-bit Python as described below._

Install the 64-bit Python 2.7 for your system from here:
http://conda.pydata.org/miniconda.html

## Step 2 - Check Your Python (optional if you just installed miniconda Python 2.7)
Download this helper script [export:/trunk/get_python_info.py get_python_info.py] and
run it with this command --
```
python get_python_info.py 1
```

It will tell you whether or not Vespa is compatible with your Python installation.

## Step 3 - Install Vespa's Dependencies, Round 1
*OS X users*, run these two commands first --
```
conda install -c bjornfjohansson wxpython 
conda install python.app
```

Next, *everyone* should run this command --
```
conda install numpy scipy wxPython matplotlib configobj
```

Then run this command --
```
pip install packaging pygamma pydicom==0.9.9 hlsvdpro lmfit pypubsub vespa-suite
```

## Step 4 - Install Vespa's Dependencies, Round 2
If you use *Windows*, run this command --
```
pip install pywavelets==0.3.0
```

If you use *OS X or Linux*, run this command --
```
conda install -c https://conda.anaconda.org/dgursoy pywavelets=0.3.0
```

*Linux* users, also use your package manager to install the FFTW3 runtime
library. Look for it under a name like `libfftw3` or just `fftw`.

## Step 5 - Finish the Vespa Install
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