# Initial Work on GAMMA with Lapack/Atlas/Blas
  * *For up to date information on this subject see [GAMMA with Blas/Lapack](/wiki:GammaWithBlasLapack/)*


## Introduction
This section describes initial work done with ATLAS and LAPACK, and some suggestions on how to proceed.


Note: Since the initial writing of this section, Lapack has introduced a new library (11/15/10) that has native C calls that should simplify the work done below and possibly speed it up. That work was done in collaboration with Intel. 
For more information see these links:

  * http://www.netlib.org/lapack/
  * http://software.intel.com/en-us/articles/tools-for-math-processing/

NOTE:  This enhanced version of Lapack has since been [integrated into the GAMMA/PyGAMMA build](/wiki:GammaWithBlasLapack/).

## Gamma with LAPACK and Atlas Enhancements
Initial work was done to study the benefits of Adding LAPACK and Atlas to the Gamma code.  Basically how much speed enhancment would be gained by speeding up the linear algebra package.

### Initial Steps
These are the results using the Fortran version of Lapack with "c-wrappers".

One of the first things was that to make a major change to the Linear Algebra code would be outside of the scope of the current grant so a more focused approach was used. Specific routines were targeted that make up substantial portions of the computations for various simulations. I changed some code in:
```
n_matrix.multiply(...)
```
routine by adding in code that uses blas (cblas / Atlas) to compute the product of two matrixes.  The input matrix was copied into a suitable matrix to pass to this routine:
```
cblas_zgemm(...)
```
Testing indicated that the benefit of this approach on 2 independent computers, both with dual core "Pentium 6" chips, with 2-4 GBytes RAM and clock speeds in the 2.6 to 2.8 MHz range, was not obtained until the matrix sized reached 256 on a side.  

Additional works was done on this routine:
```
h_matrix.diag(...)
```
matrix diagonalization of a hermitian matrix.  This utilized CLAPACK (LAPACK with a C wrapper). This also used the strategy of copying the date to a suitable matrix (in this case row major ordering) and shipping off to the routine:
```
zheev_(...);
```
Testing of this routine also indicated that the minimum matrix size to gain benefit from this routine was 256x256.  This was the main reason we abandoned this approach as our molecules were of spin 7 and 8 (or matrix size 128x128 and 256x256), or less.


## What Next
A few thoughts on how to proceed.
  * Start with a detailed profiling of the code to see where it slows down for real problems.
  * Consider using the MAGMA project to speed up linear algebra using GPU's and mutlicore PC's: http://icl.cs.utk.edu/magma/index.html
  * There is also the parallel processing linear algebra project: http://icl.cs.utk.edu/plasma/index.html
