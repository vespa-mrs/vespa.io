# Notes to Myself (or Someone Like Me)
These are notes that I wish I'd had when I started porting. If you want to 
improve the code or just understand it, these odds and ends will help.


## Code Structure Overview
The very high level code flow is this -- 

```
hlsvdpro() ==> lanczopw() ==> zlansvdw() ==> zlanbprow()
```

The entry point for the code I tested is `hlsvdpro()`. It calls `lanczopw()` 
and massages that function's output.

The function `lanczopw()` calls `zlansvdw()` in a loop until it receives a
satisfactory answer.

The function `zlansvdw()` is where Sima and Laudadio's code ends and Larsen's
code begins. It's useful to know that Larsen's code can be used independently
of the rest, although we don't use it that way.

`zlansvdw()` does a lot of work on its own and also calls `zlanbprow()` in a
loop.

## Fortran Code in the Python
In the Python code I repeated almost all of the Fortran code in comment 
blocks immediately before the corresponding Python code. For example --

```
#!python

#    alpha = B(k0,1)
#    call zcopy(n,V(1,k0),1,zwork(iv),1)
#    beta = rnorm
#    force_reorth = .true.

     alpha = bbb_a[k0 - 1]
     zworkv = vvv[:, k0].copy()
     beta = rnorm
     force_reorth = True
```


## Name Changes
A number of arrays in the Fortran code had single letter names, e.g. `U` and `V`.
I changed these to three letter names, like `uuu` and `vvv`. This makes it a 
lot easier to find them with grep or my text editor.

I changed some variable names completely (e.g. `lsinval` became 
`singular_values`). I provide a name translation table at the top of each 
module as needed.

In Fortran when I needed a counter variable (for a loop that prints
array values), I declared my own to avoid
stepping on any used by the program. I suffixed my variables with my initals
(PS), so `ips` and `jps` are my loop counters.

## Function Parameters
When calling a function, Fortran passes variables by reference, and this Fortran code
doesn't comment on which variables are modified by a function and which are 
input-only. From experience, I can say that it's safe
to assume in both the Fortran and Python code that if an array or matrix is 
passed to a function, the function 
modifies it. The exceptions to this are the matrices `lambda_` and `trlambda` 
which don't change once computed.

The Fortran functions usually don't modify scalars. One notable exception 
is `zlansvdw()` which modifies `k`. It is passed in representing the number
of singular values sought, but on `zlansvdw()` exit it represents the number of 
singular values found.

In Python it's not necessary to guess whether or not a function changes a 
scalar parameter since those are effectively passed by value. In the case
where a Fortran function modifies a scalar, the Python version of the 
function returns the new value.

## Debugging (Comparing Python Output to Fortran)
I had good success with debugging by print statement. It's a simple 
technique, but pretty reliable. I added print statements to the code in the 
same place in both the Fortran and the Python and then ran each with stdout
redirected to a text file. Comparing the text files side by side allowed me
to compare the progress of the two and see where the Python diverged from 
the Fortran. 

I left most of these print statements in the code (Fortran and Python) but
commented out.

During its calculations, Python won't generate quite the same numbers as 
the Fortran, even when it concludes with a good answer. This is most evident
in scalars that summarize the contents of an array or matrix. The `zlanbprow()`
variables `alpha` and `beta` are good examples, particularly the former.

I'm not completely sure why this happens, but I have a few guesses. First,
the code uses several constants derived from machine epsilon. On my Mac, 
EPS in Python is 2.22044604925e-16. In Fortran it's half as big 
(1.11022302462515654E-016). 

Second, `zgetu0w()` [HlsvdproPortRandomness uses a set of random numbers]. 
Fortran uses the same 
numbers every time, Python does not (although it can be made to do so, see
`_get_predictable_randoms()` in [browser:trunk/hlsvdpro/zget0w.py zget0w.py]).

Third, there are probably subtle differences 
between the floating point math in Python (C) and Fortran and the differences
accumulate over time.

For the record, I eliminated the first and second causes (by forcing the 
Fortran EPS to be the same as Python's and by forcing Python to use the 
same random numbers as Fortran) and their calculations still differed a bit.


## ctypes
If you need to use ctypes to call Fortran, you can often do it directly
but not always. Since C doesn't have a complex number type, any Fortran 
function that takes complex input needs a wrapper written in Fortran. 

The Python code must split the complex numbers into two arrays containing the
real and imaginary components as floats. The Fortran wrapper will take those
arrays and knit them back into complex numbers and then pass them to the 
target function. If the target function modifies the complex numbers, the
whole process has to be reversed after the target function completes so that
the changes are reflected back on the Python side. 

See [browser:trunk/hlsvdpro/original/src/zlanbprow.f zlanbprow.f] for an example.

## Style Considerations
My port was pretty rote both by design and necessity. For instance, there are
a lot of places in the code where I specify an array bound that's probably  
not necessary, e.g. (from `aprodw.py`) -- 

```
#!python
y[:n] = y1[:n]
```

In this case I _think_ both `y` and `y1` are always `n` items long, which means
the expression above can be stated more simply (and more expressively) in 
Python. The explicitly stated length is a result of this being a port from 
Fortran in which one must always specify array lengths.

I also wrote some pretty ugly code to get around the Fortran code's frequent
use of `goto` and Python's lack of it. The function `dcompute_int()` in 
[browser:trunk/hlsvdpro/zlanbprow.py zlanbprow.py] is probably the winner in 
this category.

In short, this code is *not* Pythonic. I encourage you to make it so!




