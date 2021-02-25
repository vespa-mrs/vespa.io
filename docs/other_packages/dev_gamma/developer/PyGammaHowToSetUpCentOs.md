# CentOS 7 Setup
This document describes how I set up CentOS 7 to build Linux PyGamma wheels.
I used CentOS as a VirtualBox guest.

If you want to build 64-bit PyGamma wheels, you need 64-bit CentOS. As of 2019
we are no longer supporting 32-bit buildss

## Support
CentOS 7 will be supported (albeit only with critical security updates) until 2024 according to the CentOS FAQ: https://wiki.centos.org/FAQ/General.

## Installation
I downloaded the ISO and created a new VirtualBox VM, mounted the ISO image to the CD, and then booted the machine. It started the installation wizard. I selected the minimal install option, but added on the Development, Debugging and SysAdmin tools to the min install. On the next setup menu page I set up a root and bsoher user name and passwd. 

When complete, I found that gcc and gcc-c++ were already installed (v 4.8.5), swig was installed but way earlier version (v 2.0.x). I used NAT to attache the network, but had to enable wired network in the Power drop menu (top right). 

After the installation, I opted to disable SELinux. (not sure how to do that yet ...)

## Post-Install Configuration
On the first reboot after installation was complete, CentOS will update itself
with the latest patches.

Next, you'll want to install VirtualBox guest additions to make the guest OS
easier to use. In order to do that, you first have to add yourself to the
`sudoers` file.

### Adding Yourself to sudoers
1. `su -`
1. `vim /etc/sudoers`
1. At the end of the file, add this line:
 your_username      ALL=(ALL)    ALL
1. Save the file with `:wq!`
1. Type `exit` to exit the `su -` shell.

### Building VirtualBox Guest Additions
From the Virtual Box -> Devices menu, select Insert Guest Additions CD Image. The CD icon will appear and you will be asked if you want to AutoRun the install process.  Click yes, and wait a bit.  You should see things being 'built' and installed.


### Adding Packages
All these packages seem to already be installed: `xz zlib zlib-devel openssl-devel pcre-devel sqlite-devel`

### Building Python
CentOS 7 comes with Python 2.7. To use a newer Python, I used the Miniconda installer script. Based on some vague advice from Google I downloded Miniconda2 since CentOS 7 system Python is 2.7.5.  I used the 'conda' command to set up a python 3.7 environment.

### Download and Install pip
Pip comes with Miniconda and Python 3.7 environment as does setuptools and wheel, both of which we need.

### Download and Build SWIG
1. Download and untar the SWIG source code. I was able to use the latest (4.0.1 as of this writing).
1. Build with `sudo ./configure && sudo make && sudo make install`



----
----
----


Deprecated Deprecated Deprecated Deprecated Deprecated Deprecated Deprecated Deprecated Deprecated 

The following instructions are included here for historical jocularity. Steps to set up
CentOS 7 as a VM are given above and should be used to create Python 3 wheels.

# CentOS 5.11 Setup
This document describes how I set up CentOS 5.11 to build Linux PyGamma wheels.
I used CentOS as a VirtualBox guest.

This document makes no distinction between 32- and 64-bit Linux. The
instructions are the same for each. If you want to build 32-bit PyGamma wheels,
you need 32-bit CentOS. If you want to build 64-bit PyGamma wheels,
you need 64-bit CentOS. It's probably possible to build
32-bit binaries on the 64-bit platform, but I haven't worked out how.

## Support
CentOS 5.x will be supported (albeit only with critical security updates) until 31 March, 2017 according to the CentOS FAQ: https://wiki.centos.org/FAQ/General.

## Installation
I downloaded the ISO and installed as one normally does under VirtualBox.
During the installation, I opted to disable SELinux.

## Post-Install Configuration
On the first reboot after installation was complete, CentOS will update itself
with the latest patches.

Next, you'll want to install VirtualBox guest additions to make the guest OS
easier to use. In order to do that, you first have to add yourself to the
`sudoers` file.

### Adding Yourself to sudoers
1. `su -`
1. `vim /etc/sudoers`
1. At the end of the file, add this line:
 your_username      ALL=(ALL)    ALL
1. Save the file with `:wq!`
1. Type `exit` to exit the `su -` shell.

### Building VirtualBox Guest Additions
First, install GCC --
```
sudo yum install gcc gcc-c++ 
```

Next --
1. Insert the Guest Additions CD. (The Guest Additions are an ISO file that you download 
  from VirtualBox.org. I think they're provided under a different license than the main 
  program which is why you have to download them separately.)
1. Start a terminal and `cd /media/VBOXADDITIONS_xxxx`. Note that the exact
 name of the `VBOXADDITIONS` directory changes with each each version of
 VirtualBox.
1. sudo ./VBoxLinuxAdditions.run
1. Eject the Guest Additions CD and reboot.

### Adding Packages
Install the things you'll need to build Python and swig, and to use pip --

```
sudo yum install xz zlib zlib-devel openssl-devel pcre-devel sqlite-devel
```

### Building Python
CentOS 5.11 comes with Python 2.4. To use a newer Python, download and untar
the source code for the Python you want to use and then build it. For the
Python 2.7.11 source that I used, I built with these steps --

```
sudo ./configure --enable-unicode=ucs4
sudo make altinstall
```

Using UCS4 (as opposed to the default UCS2) during the configure step is
important. See here for details:
https://www.python.org/dev/peps/pep-0513/#ucs-2-vs-ucs-4-builds

`make altinstall` tells Python to install itself in such a way that it doesn't
interfere with the default (system) Python.

Once my Python was built, I added a symlink to make it the default Python in my
shell --

```
sudo ln -s /usr/local/bin/python2.7 /usr/local/bin/python
```

At this point, if you start a new terminal and type `python`, you should
get Python 2.7.11.

### Download and Install pip
1. `wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py`
1. sudo python get-pip.py

This also installs setuptools and wheel, both of which we need.

### Fix pip
`pip` gets a little confused when installed in this context. Its 3 scripts
contain an incorrect shebang line. (See
[pip issue 1918](https://github.com/pypa/pip/issues/1918) for more details.)
Use `sudo vim` to edit these 3 scripts --
 * `/usr/local/bin/pip`
 * `/usr/local/bin/pip2`
 * `/usr/local/bin/pip2.7`

In each, change the first line from this --
```
#!/usr/bin/python
```
to this --
```
#!/usr/local/bin/python
```


### Download and Build SWIG
1. Download and untar the SWIG source code. I was able to use the
 latest (3.0.8 as of this writing).
1. Build with `sudo ./configure && sudo make && sudo make install`