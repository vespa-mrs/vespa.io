# Bugs
## Python
### Occasional OverflowThere's a problem that shows up very infrequently in the Python code. I'm not 
sure if it represents a bug in my port or a weakness of the algorithm. (I suspect
the former.) I see it only with
the test dataset `laser_2010102901.xml`. The algorithm completes, but 
overflows in `vanmon()` --

```
$ ./test.py original/dist/laser_2010102901.xml 
/Users/me/w/duke/src/duke-mr/hlsvdpro/hlsvdpro.py:304: RuntimeWarning: overflow encountered in cdouble_scalars
  temp *= root
/Users/me/w/duke/src/duke-mr/hlsvdpro/hlsvdpro.py:304: RuntimeWarning: invalid value encountered in cdouble_scalars
  temp *= root
RMSE = 456.13, normalized RMSE = 11.32%
```

This occurs in approximately 3% of runs. I don't see it with any other data
sets.

Why does this error occur sometimes and not others? The algorithm
[HlsvdproPortRandomness uses random numbers], and some of those numbers work
better than others.

### Hidden Bugs
The test data I used is all of a certain flavor, but this algorithm is expected to handle
a variety of data. It's certainly possible that running it against different data would expose bugs in the code that aren't exposed by the test data I used.

## Fortran
### Compiling with Optimization
I've seen suggestions that `dlamch.f` (part of LAPACK) should not be compiled
with optimization. I rebuilt my test version of HLSVDPRO with optimization 
disabled and immediately 
[saw my old friend](http://scion.duhs.duke.edu/vespa/analysis/ticket/49).

Optimization can cause some flaky problems, but my guess is that what's 
happening here is a bug in PROPACK being exposed by changes that optimization 
makes. Furthermore, I think there's a good chance that the bug is an array
index bug (described below).


### Array Indices
I suspect that the Fortran code contains bugs related to 
[HlsvdproPortFortranMemoryAllocation indices into the work and zwork arrays].

