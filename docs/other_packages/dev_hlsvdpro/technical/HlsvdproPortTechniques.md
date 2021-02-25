# Tips, Techniques and Things to Look Out For

 * In the Python code I repeated almost all of the Fortran code in comment 
 blocks with the Python immediately following the Fortran. For example --

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

 * A number of arrays in the Fortran code had single letter names, e.g. U and V.
   I changed these to three letter names, like uuu and vvv. This makes it a 
   lot easier to find them with grep or my text editor.

 * I changed some variable names completely (e.g. `lsinval` became 
   `singular_values`). I provide a name translation table at the top of each 
   module as needed.

 * When calling a function, Fortran passes variables by reference, and this Fortran code
 doesn't comment on which variables are modified by a function and which are 
 input-only. It's safe
 to assume in both the Fortran and Python code that if an array or matrix is 
 passed to a function, the function 
 modifies it. The exceptions to this are `lambda_` and `trlambda` which don't 
 change once computed.

 The Fortran functions usually don't modify scalars. One notable exception 
 is `zlansvdw()` which modifies `k`. It is passed in representing the number
 of singular values sought, but on `zlansvdw()`'s exit it represents the number of 
 singular values found.

 In Python it's not necessary to guess whether or not a function changes a 
 scalar parameter since those are effectively passed by value. In the case
 where a Fortran function modifies a scalar, the Python version of the 
 function returns the new value.

 * I had good success with debugging by print statement. It's a simple 
 technique, but pretty reliable. I added print statements to the code in the 
 same place in both the Fortran and the Python and then ran each with stdout
 redirected to a text file. Comparing the text files side by side allowed me
 to compare the progress of the two and see where the Python diverged from 
 the Fortran. 

 I left most of these print statements in the code (Fortran and Python) but
 commented out.

 * During its calculations, Python won't generate quite the same numbers as 
 the Fortran, even when it concludes with a good answer. This is most evident
 in scalars that summarize the contents of an array or matrix. The `zlanbprow()`
 variables `alpha` and `beta` are good examples, particularly the former.

 I'm not completely sure why this happens, but I have a few guesses. First,
 the code uses several constants derived from machine epsilon. On my Mac, 
 EPS in Python is 2.22044604925e-16. In Fortran it's half as big 
 (1.11022302462515654E-016). 

 Second, `zgetu0w()` uses a set of random numbers. Fortran uses the same 
 numbers every time, Python does not. 

 Third, there are probably subtle differences 
 between the floating point math in Python (C) and Fortran and the differences
 accumulate over time.

 For the record, I eliminated the first and second causes (by forcing the 
 Fortran EPS to be the same as Python's and by forcing Python to use the 
 same random numbers as Fortran) and their calculations still differed a bit.
