# Performance
The Python code's performance is already better than I expected it to be.
It's about 2 - 5 times slower than the Fortran. Further improving performance is 
definitely possible, but I already picked the low-hanging fruit.

## The Low-Hanging Fruit
Some early versions of the Python code contained a rote port of the Fortran, like this --

```
#!python
for i in range(n):
    zworkv[i] = zworks[i] - (beta * zworkv[i])
```

All of those loops have been transformed into the equivalent (and much faster)
code that takes advantage of numpy arrays, like this --

```
#!python
zworkv[:n] = zworks[:n] - (beta * zworkv[:n])
```

## Algorithmic Improvements
I don't understand the math in this code, so I might be missing some 
obvious opportunities for improvement. The only numpy/scipy functions I can 
apply are ones that are a 1:1 map with the Fortran code. If there's a way to
eliminate a block of slow Python code by manipulating a matrix with numpy/scipy 
calls, I won't see it.

There's even a suggestion to this effect in `zlansvdw.py`. It says --

   THIS SHOULD POSSIBLY BE REPLACED BY A CALL TO THE FAST
   DIVIDE-AND-CONQUER BIDIAGONAL SVD IN LAPACK 3 OR BY TRANSFORMING B
   TO TRIDIAGONAL GOLUB-KAHAN FORM AND USING DHILLONS "HOLY GRAIL"
   CODE.

That's probably a great suggestion! I don't understand it enough to follow up
on it, so that will have to be for someone else to do.

## Cython
This code is purely CPU bound, and Cython excels at boosting the performance of
that kind of code. I would be surprised if Cython couldn't improve the performance of this code
quite a bit.

### Cython and Vespa
Cython comes with its own shortcomings from the perspective of integrating
this code with Vespa. A Cython-ed HLSVDPRO would still carry two of the big
pieces of baggage that this port was supposed to eliminate in the first place.

First, we would still have to build binaries for all six supported platforms 
(32- and 64-bit, three operating systems). Second, we would have to maintain
documentation for the build tool (Cython instead of GFortran) and process.

In addition, there's not much point in Cython-ing this code while there is
still a dependency on the binary due to [HlsvdproPortDbdsqr dbdsqr()].

That said, Cython is still interesting to think about. Assuming the `dbdsqr()`
problem gets solved somehow, using Cython might not be a bad idea.

The need to build binaries for all six platforms is mitigated by the fact that
a pure Python version of this code will work anywhere, it would just be slow
compared to a Cython-ed version. That opens the possibility of building 
Cython binaries for a select few platforms (e.g. 32-bit only) and leaving the
others stuck with the slower-but-functional pure Python version.

Also, I think maintaining a Cython build process would be more appealing than 
maintaining the current GFortran build process for the following reasons --
 * [analysis:wiki:HlsvdBuilding The current build setup] requires installing
 GFortran and installing (and possibly building) FFTW. One Windows one must 
 also install GnuWin32. By comparison, installing just Cython is a good bit
 easier.
 * It's implied in the bullet point above, but worth stating explicitly that
 the Python version of HLSVDPRO uses numpy's FFT and therefore doesn't require FFTW. The same would apply to a Cython-ed version.
 * Given Vespa's enormous Python emphasis, investing time in Cython seems more 
 likely to pay dividends elsewhere than investing time in GFortran.
 * Cython is already required to build 
 [analysis:wiki:PyWaveletsOsxBuilding PyWavelets for OS X].
