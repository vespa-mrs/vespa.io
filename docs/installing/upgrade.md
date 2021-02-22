---
sort: 2
---

# Overview

**_Note. As of Vespa version 1.0.0, Vespa is running under Python 3. If you have a Vespa version less than 1.0.0, that is running under Python 2.7 and can not be upgraded.  You should use the 'New Installation' instructions._**

The instructions below assume that you already have Vespa installed and that it is version 1.0.0 or higher. 


## Upgrade Vespa 

Run a command shell in the conda environment in which Vespa is installed.

Run this command:

`>pip install vespa-suite --upgrade`

This should install the most recent version of the Vespa package.  After it is done, please check your Python dependencies by running:

`>python -m vespa.check_dependencies `

If you are missing any packages, or the versions of packages you have installed are outside Vespa's dependencies, you will be given information about what changes are needed before you can run Vespa.


## Questions?  

If you have any questions, feel free to ask them on [the Vespa Forum on MRS Hub](<https://forum.mrshub.org/c/mrs-software/vespa/11>). 


