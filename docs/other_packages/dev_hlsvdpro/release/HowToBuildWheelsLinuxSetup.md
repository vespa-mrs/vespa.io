# How to Set Up Linux For Building an HLSVDPRO Wheel
This document describes how to set up a Linux environment to be able to build an HLSVDPRO wheel that you can distribute. You only have to do it once per machine, not every time you build a wheel.

These instructions are for HLSVDPro version 2.x creation. 

Please follow the instructions on this page [Building CentOS 7](/wiki:HlsvdproHowToSetUpCentOs/) to create a linux distro to create HLSVDPRO wheels. 

This specific linux distro is used because we are attempting to create 'manylinux2014' flavor wheels for distribution and installation.  See [PEP599](https://www.python.org/dev/peps/pep-0599/) here for details.

Caveat - This is still sort of a half-assed attempt at PEP599 compliance because we are not using any of the docker resources that comply to the library versions etc. that are required.  Just did not have the time to figure this out this time around. So I'm just going to go with a clean install of CentOS7 in VirtualBox and hope that the library versions are similar.  BJS Oct 2020

----

# Deprecated Linux Instructions for version 1.x
HLSVDPRO version 1.x used CentOS 5.x to create a 'manylinux1' flavor wheel for installation. It also used CTYPES to access the Fortran code and other differences from HLSVDPRO version 2.x.  For provenance, we maintain the instructions below for setting up Linux to create the version 1.x library.  

## (deprecated) Install CentOS 5.11
We use CentOS 5.11 to build Linux wheels. If you have set up a CentOS 5.11
environment for building PyGamma wheels, that's a perfect base to 
build on. 

If not, start by [following the instructions for building CentOS](/wiki:HlsvdproHowToSetUpCentOs/). 

Once you have CentOS installed, continue with the instructions below.

## (deprecated) Install GFortran
```
sudo yum install gcc-gfortran.x86_64
```

## (deprecated) Download and Build libfftw3
1. [Download the libfftw3 source code](http://www.fftw.org/download.html) and untar. 
 I was able to use the latest version (3.3.4 as of this writing).
1. Build --
```
 sudo ./configure --enable-shared --disable-static
 sudo make
```
1. Install --
```
 sudo make install
```
1. Make Linux aware of the shiny new library in /usr/local/lib --
```
 sudo /sbin/ldconfig /usr/local/lib
```

At this point you're ready to build HLSVDPRO.

## Other Things You Might Want
You don't need `matplotlib`, but should you want to install it,
you'll definitely
[benefit from these instructions](http://stackoverflow.com/a/28073304).
