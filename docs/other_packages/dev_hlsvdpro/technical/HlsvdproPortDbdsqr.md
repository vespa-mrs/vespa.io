# DBDSQR()
Why does this one LAPACK function get a whole Wiki page? Because it blocks our
complete independence from our custom binary.

Of all of the BLAS and LAPACK functions called by HLSVDPRO, `dbdsqr()` is the only
one that I can't get to from scipy/numpy, and it's complicated enough that 
I don't want to port it myself. To date I've resorted to calling the binary 
version of `dbdsqr()` in our HLSVDPRO library. 

As long as our Python code calls HLSVDPRO even for just one LAPACK function, we're
stuck with schlepping around a binary and all of the baggage that goes with it.
(That includes GFortran installed on three platforms, binaries for 32- and 64-bit, 
documentation on how to build it, etc.)

(Side note: I can call `dbdsqr()` via scipy 0.11.0 on
my Mac, but not on Linux nor on Windows, and even its availability under OS X
might be the result of a compiler whim. For details, 
see [this scipy mailing list discussion](http://mail.scipy.org/pipermail/scipy-user/2012-December/thread.html#33826).
If that link breaks, Google for "Calling LAPACK function dbdsqr" and ignore the
conversation on the numpy list.)


## Possible Fix 1 - Use Something Else
`DBDSQR()` is a LAPACK routine described as follows -- 

   DBDSQR computes the singular values and, optionally, the right and/or
   left singular vectors from the singular value decomposition (SVD) of
   a real N-by-N (upper or lower) bidiagonal matrix B using the implicit
   zero-shift QR algorithm.
   (from [dbdsqr.f](http://www.netlib.org/lapack/double/dbdsqr.f))

If some clever person could find scipy/numpy function(s) that solve the same
problem in a different way, we could get rid of `dbdsqr()`.

## Possible Fix 2 - Expose it via Scipy
The scipy folks would like all of BLAS and LAPACK to be available via scipy. The
only reason it isn't yet is because the work hasn't been done to make it 
happen. If we submit a patch to make it available, then it should appear in some
future version of scipy.

This would require learning a bit about 
[using f2py to wrap LAPACK](http://www.scipy.org/Cookbook/F2Py) which doesn't
look so bad. The awkward part is that `dbdsqr()` calls several other LAPACK
functions and some of them aren't in scipy either, so you'd also have to generate wrappers for them, too.

## Possible Fix 3 - Port `dbdsqr()` to Python
This is technically possible, but probably the most work and the one that 
would result in the worst performance. It's not a short function; it's about
600 lines long even ignoring the big block comment at the top.

## Possible Fix 4 (OS X Only) - Call LAPACK Directly
Python's `ctypes` makes it possible to call arbitrary binaries. OS X ships
with LAPACK in the Accelerate framework which our code could theoretically
load and call. 

Since OS X is the only platform that ships with a predictable LAPACK implementation,
this solution won't work on other platforms.
