# Unported Code
I ported most of the Fortran code, but not all of it. There are a few cases
where the port is incomplete or suboptimal.

## Singular Vector Calculation in zlansvdw.py
Near the end of `zlansvdw.py` (after the loop that calls `zlanbrow()` has 
ended), there's a block of code marked with the comment 
"Calculate singular vectors if requested". Inside that block, there's a section
that only executes if jobv == 'Y'. In our code, that's always hardcoded to 
'N' so I didn't port that section.

## Classical/Modified Gram-Schmidt Reorthogonalization
In `zlanbprow.f` the constant `MGS` (I think it means 
"[use] Modified Gram-Schmidt") is hardcoded to 1. The code contains
a couple of cases where it calls `zreorth()` instead of `zreorth2()` 
depending on the value of `MGS`. Since `MGS` never changes in our code and 
I don't have a way to confidently test the branches that aren't taken, 
I didn't port those branches. 

They wouldn't be hard to re-enable if you're interested, since I already ported
both `zreorth()` and `zreorth2()`.

## Poor Ports of BLAS, LAPACK and Other Functions
There are (at least) two functions that I ported from Fortran where my version
is almost certainly not as robust as the originals. Specifically, my implementations 
of `dlapy2()` and `zsafescal()` are correct but don't guard against 
under/overflow the way the Fortran code does.

## Timing Code
I didn't port the [HlsvdproPortFortranTimingCode timing code] since Python's built-in profiler gives me almost exactly the same information with far less effort.