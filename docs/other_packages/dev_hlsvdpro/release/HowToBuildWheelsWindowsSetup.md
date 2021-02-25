# How to Set Up Windows For Building an HLSVDPRO Wheel
These instructions are for HLSVDPro version 2.0.0 and later. 

This document  describes how to set up your Windows environment to be able to build an HLSVDPRO wheel that you can distribute. You only have to do it once per machine, not every time you build a wheel.

As of HLSVDPro version 2.0.0 the algorithm is based on the T. Laudadio, N. Mastronardi, L. Vanhamme, P. Van Hecke and S. Van Huffel, J Magn Res, 157, p292-7, (2002) paper, which does not use an FFT, and thus no longer requires the FFTW dependency. Also we have updated the SVD algorithm to use PROPACK version 2.2. We use an f2py front end on the PROPACK SVD call, rather than the previous CTYPES front end for more flexibility. Finally, the actual steps of the HLSVDPro algorithm are organized in Python as calls to either the PROPACK SVD function or other functions in Scipy, rather than being fully encoded in FORTRAN as HLSVDPro version 1.x was.

## Install GCC/GFortran
*NB.* The installation recommended below had both already included, but some other installations may have to be done separately. 

For the most recent PROPACK v2.1 compile, I had to install an updated mingw-w64 compiler suite on Windows.  I installed 64 bit gcc version 7.3.0 as a trade off between the latest version and one that might be available across Windows, Linus and MacOS platforms, which this project supports. I downloaded from [here](https://sourceforge.net/projects/mingw-w64/) with the following steps.
- On this [page](https://sourceforge.net/projects/mingw-w64/files/) find the link halfway down the page to the MinGW-W64-install.exe file, and download it.
- Run this file and an installer dialog will pop up.
- Set the following settings in the pull-down menus
  - Version = 7.3.0
  - Architecture = x86_64
  - Threads = posix
  - Exception = seh
  - Build revision = 0
- Hit Next button (not installing yet)
- I recommend that in this next dialog you install in a folder without spaces in the name to make your life easier later in the Makefiles of life
- I installed into C:\compilers\mingw-w64\x86_64-7.3.0-posix-seh-rt_v5-rev0
  - all I changed here was C:\Program Files\ to C:\compilers\
- Hit Next and download/install will begin.

*NB.* Failure warning - I originally downloaded the TDM-gcc suite from https://jmeubank.github.io/tdm-gcc/ as listed previously in this documentation. However, they only had version 9.2.0 available at this time. I did get the Python 2.7 version of HLSVDPRO with PROPACK v2.1 to compile and work with this gfortran, but the Python 3.7 version compiled but threw a ImportError in Python about DLL initialization. Found one stackoverflow question where they had TDM too, and ended up installing a different mingw-w64 compiler. 


----

# Deprecated Instructions
These were the instructions for setting up Windows for the first version of HLSVDPro (version 1.0.0 to 1.0.1). That version of HLSVDPro was less modular that the current one. It focused on 'fitting' model of lorentzian lines to data and returning a set of amplitude, frequency, phase and damping values that described the fit for the first N model lines (where N is provided by the user). This algorithm used the PROPACK (version 1.x) SVD algorithm to calculate the first N singular values. It was also based on the method described in the W.W.F. Pijnappel, A. van den Boogaart, R. de Beer, D. van Ormondt, J. Magn. Reson. 97, 122 (1992) paper which used an FFT as part of its process. 

As of HLSVDPro version 2.x the algorithm is based on the T. Laudadio, N. Mastronardi, L. Vanhamme, P. Van Hecke and S. Van Huffel, J Magn Res, 157, p292-7, (2002) paper, which does not use an FFT. Also we have updated the SVD algorithm to use PROPACK version 2.2, and have put an f2py front end on that call, rather than the previous CTYPES front end.

### Install GCC
[This site](http://tdm-gcc.tdragon.net) offers a nice installer for GCC+GFortran.
Unfortunately, only the latest version of GCC+GFortran (5.1.0 as of this writing)
can be installed with their nice installer, and when I build HLSVDPRO with
that version, HLSVDPRO segfaults somewhere in its guts.

I reverted to GFortran 4.6.1 (the version with which I built HLSVDPRO the
very first time) and the segfault went away, so that's what I advise you to do
too. It's a little more work.

You can download the installer and the GFortran update from this Web page.
FIXME attach files. 

Run the GCC installer. It will install into `C:\MinGW64`.

### Install GFortran
Unzip `gcc-4.6.1-tdm64-1-fortran.zip`.

cd into the directory where you unzipped that, then run this command --
```
xcopy *.* c:\MinGW64  /E /F
```

That will copy everything in the Fortran package into the directory where you 
installed the compiler. 

If you want to see what that command will do without actually copying any files
(i.e. a dry run), add the `/L` parameter.

Add this to your PATH if the installer didn't do so
already --
```
c:\MinGW64\bin;
```

## Install the FFTW3 Runtime DLLs
Download [FFTW for Windows](http://www.fftw.org/install/windows.html).
The package will probably be called something like `fftw-3.3.4-dll64.zip`.
You only need one file from that package: `libfftw3-3.dll`. Copy that
file into the `hlsvdpro\src` directory. (It's a little strange to copy a DLL
into the source code directory, but if we put it in the `src\bin` directory
where it logically belongs, it will get wiped out every time one
runs `make clean`.)
