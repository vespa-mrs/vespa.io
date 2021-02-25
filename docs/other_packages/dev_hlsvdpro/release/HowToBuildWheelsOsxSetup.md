# How to Set Up OS X For Building an HLSVDPRO Wheel
This document describes how to set up your OS X environment to be able to build 
an HLSVDPRO wheel that you can distribute. You only have to do it once per 
machine, not every time you build a wheel.

# Instructions for HLSVDPRO version 2.x
I was using an older MacBook Pro with OSX Catalina installed. The default gcc did not have gfortran installed, so I installed gcc 6.5.0 with gfortran using Homebrew.

- Install Homebrew from https://brew.sh/ using the code below in a macOSX Terminal:

 `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

- Found a formula on Homebrew for gcc called gcc@6 for version 6.5.0. Picked this version for no particular reason other than it was newer that 4.x and not as cutting edge as 9.x (which eventually led to issues on my Win install, so I had to downgrade that, too).

 `https://formulae.brew.sh/formula/gcc@6'

- This formula required a few dependencies, gmp, isl, libmpc, mpfr, which (I think) it installed for me.

- Homebrew installs these packages in `/usr/local/Cellar`, you should check to be sure it is there.

- I created some symbolic links in easier-to-type subdirectories. Namely, I created `/usr/local/gcc6` and `/usr/local/gcc6/bin`

- To make a symbolic link on Mac on Terminal command line type `ln -s /path/to/original /path/to/link`. You can link single files OR whole directories.

- In /usr/local/gcc6 create a link to:

```
ln -s /usr/local/gcc6/bin/lib /usr/local/Cellar/gcc@6/6.5.0_5/lib/gcc/6
```

- In /usr/local/gcc6/bin create these links (may not need all, but WTF):

```
ln -s /usr/local/gcc6/bin/ar /usr/local/Cellar/gcc@6/6.5.0_5/bin/x86_64-apple-darwin19.4-gcc-ar-6
ln -s /usr/local/gcc6/bin/gcc /usr/local/Cellar/gcc@6/6.5.0_5/bin/x86_64-apple-darwin19.4-gcc-6
ln -s /usr/local/gcc6/bin/gfortran /usr/local/Cellar/gcc@6/6.5.0_5/bin/x86_64-apple-darwin19.4-gcc-gfortran-6
ln -s /usr/local/gcc6/bin/nm-6 /usr/local/Cellar/gcc@6/6.5.0_5/bin/x86_64-apple-darwin19.4-gcc-nm-6
ln -s /usr/local/gcc6/bin/ranlib /usr/local/Cellar/gcc@6/6.5.0_5/bin/x86_64-apple-darwin19.4-gcc-ranlib-6
```

- When done, I added a line to my `.bash_profile` file to be sure that the preferred gcc (gcc@6 in this case) was found before the system gcc.

```
# Add preferred gcc location to front of path. I have made links to the deep
# directory at a shallower depth for convenience
export PATH=/usr/local/gcc6/bin:/usr/local/gcc6/lib:$PATH
```

- It can be hard to force OSX to link statically, so I had to 'HIDE' the `libquadmath.dylib` and `libquadmath.0.dylib` files. I did this by creating a folder named 'bob' in `/usr/local/Cellar/gcc@6/6.5.0_5/lib/gcc/6` and moving those files into there.

- At this point I think I was ready to rock and roll.







----

# Deprecated Instructions for HLSVDPRO version 1.x
Enough code has changes between version 1.x and 2.x that I'm treating the process as a whole new architecture. Thus the new instructions above.  But, these below are also for provenance since we have not entirely retired version 1.x yet.

## (deprecated) Build FFTW3
[Get the FFTW3 source code](http://www.fftw.org/download.html), untar it, 
and then in the source directory (e.g.
`/usr/local/src/fftw-3.3.4`) execute these commands:
```
export MACOSX_DEPLOYMENT_TARGET=10.9
./configure --disable-shared --enable-static && make && sudo make install
```

## (deprecated) Install GFortran
Use the
[nice, OS X-aware GFortran installer](http://gcc.gnu.org/wiki/GFortranBinaries#MacOS).
I've used GFortran 5.2 and an earlier version (maybe 4.6?) with success.




