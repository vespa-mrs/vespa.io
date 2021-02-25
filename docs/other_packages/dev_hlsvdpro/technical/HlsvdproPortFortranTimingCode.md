# Fortran Timing Code
The Fortran code contains some code to measure the runtime of certain sections and count iterations. This code confused me a little at first, so I just wanted to point out that one can safely ignore it.

The timing code is scattered all across the code. It's not hard to identify from these clues --

 * A call to `second()`
 * The above plus fiddling with a variable that starts with '`t`', for example -- `tmvopx = tmvopx + (t3-t2)`
 * The above plus incrementing a variable beginning with n, for example -- `nopx = nopx+1`

The code in [browser:trunk/hlsvdpro/original/src/printstat.f printstat.f] makes use of these.

