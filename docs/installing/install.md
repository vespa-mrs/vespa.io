---
sort: 1
---

# New Vespa Installation

## Installation Steps

Vespa is a Python package. It requires a Python environment be installed with certain dependencies (all easily obtained) and then Vespa can be automatically installed from the PyPI web site. For historical reasons, the package on PyPI is called Vespa-Suite. 

Vespa is an actively developed project with ongoing releases. Once you have it installed, it is simple to [Upgrade](upgrade.md). 

_Note. Vespa has been tested mainly under Python 3.7 due to our conversion from Python 2 to Python 3. Work is under way to evaluate other Python 3.x versions._

The following instructions are based on using the 'Miniconda' installation, part of the Conda package management sytem, to install the dependencies that Vespa requires. We are only installing the packages we need for simplicity. You could install these packages yourself using other means, but these instructions use conda. 

You'll need to use the command line for most of these instructions. Be careful of typos.

### Step 1 - Install Python (using Miniconda)

Vespa has been tested under Python 3.7. These instructions assume that you used Miniconda to install 64-bit Python as described below.

Download [the 64-bit Miniconda3 package](https://docs.conda.io/en/latest/miniconda.html) for your system. Note - we recommend installing miniconda 'for yourself' vs 'all users' as this installs the 'miniconda3' subdirectory in your home directory. We assume for some hard coded paths below that this is the case.

As of September 2020, this will install conda with a base Python of version 3.8 or 3.8, but Vespa has only been tested under Python 3.7. Not to worry, Miniconda allow you to create virtual environments with any version of Python 3, and this is what we will use to install/run the Vespa package. So, fire up the conda base command window and create your first environment. This is simple (see below) and it is good to do your actual work in a Python environment outside of the base environment.

Start an Anaconda (aka 'miniconda') command prompt (on Win10) by clicking the Start button, scrolling down the Programs file list to Anaconda, and selecting "Anaconda Prompt".

In the Anaconda prompt, create a new environment within your miniconda installation called 'python37' (or whatever you want to name it) by typing:  

`>conda create --name python37 python=3.7` 

conda will think for a bit, then list the files it will install and ask you to confirm. Type 'y' and return. Conda will then download packages and install them.

The last step here is to activate the new python37 environment by typing: 

`>conda activate python37` 

This switches you from whatever virtual conda environment you are currently in, into the 'python37' (or whatever name you chose) environment you just created. All the additional software installation steps will now be applied to that environment.

### Step 2 - Install Vespa Dependencies

2.1 At the command line, run this command:
 
`>conda install numpy scipy configobj packaging`  (if these do not install, try from conda-forge, as in 2.3)` 

2.2 Then run this command:

`>conda install matplotlib==3.3.4 wxpython==4.0.4`  (if these do not install, try from conda-forge, as in 2.3)

2.3 Then run this command:

`>conda install -c conda-forge lmfit pydicom pypubsub nibabel nifti-mrs pymapvbvd`

### Step 3 - Now Install the Vespa Package 

At the command line, run this command:
 
`>pip install  pygamma nifti-mrs vespa-suite`


### Step 4 - Doublecheck Vepsa Dependencies 

At the command line, run this command:
 
`>python -m vespa.check_dependencies `

_**Note. For Linux Ubuntu 20.04 (minimal install) check_dependencies.py found that the fftw3 package was not installed. As this was a Linux dependency, not a Python module, I installed it manually using apt-get at the command line.**_

### Step 5 (optional) - Create Shortcuts on Desktop to Run Vespa  

At the command line, run this command: 

`>python -m vespa.create_shortcuts`

_**Note. Automated Windows shortcut creation may no longer work under Win10 (Thanks, Microsoft!). So, see below if you want to manually set up Shortcuts on the Windows Desktop for running the Vespa apps.**_ 

And, You're Done! Double click on one of the shortcuts to start using Vespa!

Don't forget to [join the Vespa Forum on MRS Hub](<https://forum.mrshub.org/c/mrs-software/vespa/11>). We'll see you there.

Enjoy,
 
-- The Vespa Team

## Creating Windows Shortcuts

The Vespa installation has had problems with shortcuts since Win 10 came out. This post will walk you through setting up shortcuts manually.

So, this assumes that you have installed Python 3.7.x using miniconda. The command used below allows any conda environment that you have created in your miniconda directory to be used, so it’s OK if you have several set up other than 3.7.x

1. Right click on your desktop, and create a New Shortcut.

1. In the dialog that pops up, browse for any Python (*.py) file (to get the corresponding icon). You could browse for the Vespa Analysis main.py script now if you want, as you will need this path later.

1. Enter a name for your Shortcut like “Vespa Analysis”, hit enter. You now have a shortcut that you can modify …

1. Copy the following line (below) into a word process and modify it to match the locations of your Miniconda and Vespa installations on your computer. Detailed instructions are listed below. Use a word processor so it is easier to read/type. *_Be very careful to get the directory names and all the quote symbols correct!_* 

    ```
    %windir%\System32\cmd.exe /k ““D:\Users\bsoher\miniconda3\Scripts\activate.bat” “D:\Users\bsoher\miniconda3\envs\python37” && python “D:\Users\bsoher\miniconda3\envs\python37\Lib\site-packages\vespa\analysis\main.py” && exit”
    ```
    
    This tells the Shortcut to do 4 things, in order: 

    - create a Windows cmd.exe window
    - use a minconda script to activate your Python 3.7 conda environment in the cmd window
    - run the Vespa Analysis main.py script
    - when Analysis quits, exit the cmd window 

    Let’s parse these steps and tell you what you need to change for it to work on your computer:

    `%windir%\System32\cmd.exe /k`

    change nothing

    `"“D:\Users\bsoher\miniconda3\Scripts\activate.bat”`

    change path to where your miniconda install lives (note two 'double quotes' at the start of the line)

    `“D:\Users\bsoher\miniconda3\envs\python37”`

    change path to select the conda environment for Python 3.7

    `python “D:\Users\bsoher\miniconda3\envs\python37\Lib\site-packages\vespa\analysis\main.py”`

    change path to where Vespa is installed, usually under “Lib\site-packages\vespa” in your Python 3.7 directory

1. Copy the edited command from your text editor into the Shortcut you created. Right click its icon, click Properties. On “Shortcut” tab, delete all text in the Target line, and paste new command text into Target. Click OK and dialog should close. With luck, you can now click on the Shortcut icon and Vespa Analysis will run.

1. Create new Shortcuts for the other Vespa applications. Create New Shortcuts, or copy/paste this first one, and change the command in each Target box to the Python script that runs Simulation, Pulse, or DataSim by changing the word 'analysis' to either 'simulation', 'pulse', or 'datasim', respectively.

1. (optional) Your shortcut typically has the default icon applied to it. If you want to use the Vespa icons instead, we have included them in the installed Vespa package for you to apply manually.  Just FYI, the icons you see Vespa using are embedded in the code, so nothing you do to these external *.ico files can mess up the applications
    1. Right click your shortcut, select Properties
    1. On the 'Shortcut' tab, click on the 'Change Icon...' button.
    1. Vespa icons are located in the `~\miniconda2\envs\python27\Lib\site-packages\vespa\icons` directory
    1. Use the Browse button to select the icon for the Application you are setting up.
    1. Close the Properties dialog by clicking OK twice and it should appear.


## Questions?  

If you have any questions, feel free to ask them on [the Vespa Forum on MRS Hub](<https://forum.mrshub.org/c/mrs-software/vespa/11>). 

If you want to report a bug, please email us directly at - vespa.bugs@gmail.com.


## Other Useful Notes

1. For OS X and Linux users, we are aware (and maybe you are too) that Python comes preinstalled as part of OS X. The general consensus is that the preinstalled Python belongs to OS X and you shouldn't use it in case you change it in some way that breaks OS X (and vice versa). We recommend that you install another Python instead of using the preinstalled, system Python. This is covered in the installation guide above.
2. If you need to use a Python version later than 3.7, at this point we would suggest Python 3.9 with matplotlib version 3.6.2, and wxpython version 4.2.0. This is our current dev environment on which we are testing Vespa.  Newer versions of the other dependencies may or may not have problems, but we have definitely seen issues in the Vespa plotting GUI for environments using wxpython 4.1 and matplotlib > 3.3.  
