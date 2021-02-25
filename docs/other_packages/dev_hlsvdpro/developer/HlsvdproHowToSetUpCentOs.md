# CentOS 7 Setup
This document describes how I set up CentOS 7 to build Linux HLSVDPro wheels.
I used CentOS as a VirtualBox guest.

If you want to build 64-bit PyGamma wheels, you need 64-bit CentOS. As of 2019
we are no longer supporting 32-bit builds

## Support
CentOS 7 will be supported (albeit only with critical security updates) until 2024 according to the CentOS FAQ: https://wiki.centos.org/FAQ/General.

## Installation
I downloaded the ISO and created a new VirtualBox VM, mounted the ISO image to the CD, and then booted the machine. It started the installation wizard. I selected the minimal install option, but added on the Development, Debugging and SysAdmin tools to the min install. On the next setup menu page I set up a root and bsoher user name and passwd. 

When complete, I found that gcc and gcc-c++ were already installed (v 4.8.5). This seemed to include gfortran as part of gcc, so I was set to go for compiling HLSVDPRO.  [FYI - SWIG was installed but way earlier version (v 2.0.x), so for PyGAMMA I had to install/compile a newer version of SWIG.]

I used NAT to attach the network, but had to enable wired network in the Power drop menu (top right). 

(FYI, this step not implemented - don't know how to do - not sure if needed as compile still works) After the installation, I opted to disable SELinux. 

## Post-Install Configuration
NB. I've kept these next steps from the original (CentOS 5) instructions, but have annotated where they do/don't seem to be needed. 

On the first reboot after installation was complete, CentOS will update itself with the latest patches. (Not sure if this happened. Might have needed to have wifi network attached for this to auto-start).

First, add yourself to the `sudoers` file. Then, install VirtualBox guest additions to make the guest OS easier to use. 

### Adding Yourself to sudoers
1. `su -` switch user to root, use root passwd
1. `vim /etc/sudoers`  
1. At the end of the file, add this line:
 your_username      ALL=(ALL)    ALL
1. Save the file with `:wq!`
1. Type `exit` to exit the `su -` shell.

### Building VirtualBox Guest Additions
From the Virtual Box -> Devices menu, select Insert Guest Additions CD Image. The CD icon will appear and you will be asked if you want to AutoRun the install process.  Click yes, and wait a bit.  You should see things being 'built' and installed.

### Adding Packages
All these packages seem to already be installed: `xz zlib zlib-devel openssl-devel pcre-devel sqlite-devel` so I didn't have to do any other install steps here.

### What about Python?
CentOS 7 comes with Python 2.7, but it's always a bad idea to use/change the system Python installation. 

I used the Miniconda [installer](https://docs.conda.io/en/latest/miniconda.html). Based on some vague advice from Google I downloaded Miniconda2 since CentOS 7 system Python is 2.7.5.  

I then used the 'conda' command to set up local Python 2.7, 3.6, 3.7 and 3.8 environments called, creatively - python27, python36, python37 and python38. I installed twine and built a .pypirc file to simplify PyPI uploading (see [here](https://scion.duhs.duke.edu/projects/hlsvdpro/wiki/HlsvdproHowToUploadWheels) for info on Uploading Wheels)

### Download and Install pip
Pip comes with Miniconda and Python 3.7 environment as does setuptools and wheel, both of which we need.  May need to upgrade pip for it to work smoothly.



