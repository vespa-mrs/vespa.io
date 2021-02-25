# How To Upgrade Vespa
This guide is for users upgrading from one version of Vespa to another.

If you're upgrading from a version < 0.9.1 to a version >= 0.9.1, you're
moving from 32-bit to 64-bit Vespa which is a big change. In that case, ignore the
instructions below. Instead, please read our
[overview of the change](/wiki:AboutUpgradeFrom32To64/) and then 
proceed to the [HowToInstallVespa installation instructions].

If you are upgrading from a version < 0.10.0 you need to make sure that wxPython has been upgraded to version 4.0.4 or higher, and matplotlib 2.2.3 

## Check Your Python
Download [export:/trunk/get_python_info.py get_python_info.py] and
run it with this command --
```
python get_python_info.py 2
```
If your Python installation has all the necessary 64-bit dependencies you should see a message stating, "Everything looks good! You are ready to proceed with the Vespa upgrade." ... on to the next step!


*Note.* As of Vespa version 0.10.0 you may need to upgrade to newer versions of wxpython and matplotlib packages, and install lmfit and pypubsub packages. In Anaconda (or miniconda) you can do this at an Anaconda command prompt with these commands --
```
conda install wxpython==4.0.4 matplotlib==2.2.3

pip install lmfit pypubsub
```


## Upgrade Vespa
Run this command --
```
pip install vespa-suite --upgrade
```

## Questions?
If you have any questions, feel free to ask them on 
[the Vespa mailing list](https://groups.yahoo.com/neo/groups/vespa-mrs/info). 
