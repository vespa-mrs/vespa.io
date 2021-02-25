# Static Linking
This document is for those who want to build a GAMMA and/or GAMMA
programs (using the `gamma` script) without runtime dependencies. One scenario
where this might be useful is when building a binary that's meant to run on 
a cluster. A statically linked binary means that you don't need to copy as 
many support libraries to the cluster slaves.

Static linking is a non-standard path so we don't recommend it if you're not
willing to battle linker options and error messages. This is not for the faint
of heart.

Also note that this document is pretty Linux-specific, although some if it could
perhaps be applied to OS X. (I haven't tried it.) 

This document summarizes some of 
[a Vespa mailing list conversation](http://tech.groups.yahoo.com/group/vespa-mrs/message/537).
You might want to read the whole thread for background information.


## Statically Linking GAMMA to BLAS
Note: [GammaWithBlasLapack GAMMA doesn't use BLAS by default]. Your choice of
library will affect the name you use to link to it, so the instructions below
are generic and must be customized to your installation. The examples below
assume you use OpenBLAS.

One can convince the linker to link the BLAS library statically while linking 
all other libraries dynamically by changing the `BLAS_LIBS` definition in 
the Makefile to this -- 

```
BLAS_LIBS = -L/usr/local/lib -Wl,-static -lopenblas -Wl,-Bdynamic -lgfortran 
```

The magic here is the `-Wl,-static` flag. The gcc option `-Wl` passes the 
following option directly to the linker. Using `-Wl,-static` tells the linker
to link all subsequently referenced libraries statically. (In this case, that's 
`libopenblas`.) The flag `-Wl,-Bdynamic` restores normal dynamic linking for
the remainder of the link steps. 

As one would expect, the resulting GAMMA binary does not depend on 
`libopenblas` --

```
$ ldd ../../linux-gnu/libgamma.so
	linux-vdso.so.1 =>  (0x00007fffe6721000)
	libgfortran.so.3 => /usr/lib/x86_64-linux-gnu/libgfortran.so.3 (0x00007f420fe5e000)
	libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f420fb5e000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f420f861000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f420f64b000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f420f28c000)
	libquadmath.so.0 => /usr/lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007f420f055000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f421094a000)
```

Theoretically, one could also statically link to `libgfortran` with these
options -- 
```
BLAS_LIBS = -L/usr/local/lib -Wl,-static -lopenblas -lgfortran -Wl,-Bdynamic 
```

However, on my test system (Linux Mint 13 x64) this gives an error that I don't
know how to resolve -- 

```
Making Shared Library libgamma.so From Object Files

/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/4.6/libgfortran.a(string_intrinsics.o): relocation R_X86_64_32S against `.bss.zero_length_string' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/4.6/libgfortran.a: could not read symbols: Bad value
collect2: ld returned 1 exit status
make: *** [../../linux-gnu/libgamma.so.4.3.2] Error 1
```

As I said, this exercise is not for the faint of heart!


## Statically Linking Your Programs to GAMMA
If you want the `gamma` script to statically link your programs to the GAMMA
static library, you'll have to edit that script. It normally resides in 
`/usr/local/bin/gamma`. 

The compile and link commands (one verbose and one silent; both are otherwise
exactly the same) are near the bottom of the `gamma` script. Replace this 
portion of the lines --

```
-lgamma
```

with this --

```
-Wl,-static -lgamma -Wl,-Bdynamic
```

GAMMA programs built with this script will no longer depend on the GAMMA 
library.
