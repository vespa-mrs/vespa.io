# Fortran Memory Allocation
The Fortran code uses a number of real and complex arrays. Instead of
declaring these arrays individually, the authors chose
to allocate space for these arrays by declaring one big array of each type
(real and complex, called `work` and `zwork` respectively) and then subdividing 
them using indices. 

There must be a good reason for this because it's neither an easy nor obvious
choice, and it has a number of disadvantages. I feel 
like the authors went to a lot of trouble their lives harder than they needed to be.

I outline the disadvantages below not to chastise the original 
authors, but to illustrate some of the difficulties one will face in 
understanding the Fortran code.

If one wanted to begin to understand this code and make it easier to read
at the same time, a good place to start would be by replacing `work` and `zwork`
with smaller, individual arrays. Making use of the `allocate()` function 
(which might not have been in widespread use when this code was written) would
also allow one to hide some of these arrays inside functions.

## Disadvantage 1 - Difficult to Determine Correctness
The code that allocates the arrays does so at the outermost layer of the
code, so it has to know about the needs of all of the inner layers in order
to declare a sufficiently large array. As a result, we end up with this code 
in `hlsvdpro.f` to define `lwrk` and `lzwrk` which are the lengths of
`work` and `zwork` respectively --

```
#!fortran
lwrk    = Lrow+mcoL+13*kmax+8*kmax**2+32*Lrow+ndp*kmax
lzwrk   = Lrow+mcoL+32*Lrow+7*kmax+2+2*kmax**2+5*ndp
```

It's pretty difficult to determine where all of those terms came from, and 
whether or not they're correct.


## Disadvantage 2 - Difficult to Read
Since all the arrays are either in `work` or `zwork`, one has to look at the
array indices to determine what logical array is being referenced. The names
of the arrays themselves don't communicate anything and instead are just noise
hiding the signal. 

Instead of this (from `zlansvdw.f`) --
```
#!fortran
do i=1,j
   work(ibnd+i-1) = abs(rnorm*work(ibnd+i-1))
   work(ib1+lanmax+i-1) = work(ib1+lanmax+i-1)**2
end do
```

You could have this -- 
```
#!fortran
do i=1,j
  work_bnd(i) = abs(rnorm*work_bnd(i))
  work_b2(i)  = work_b2(i)**2
end do
```


## Disadvantage 3 - Forces Contiguous Allocation
Declaring multiple arrays as one big array tells the compiler to allocate a 
large, contiguous block of memory instead of several smaller blocks. It's 
always faster for the memory manager to find space for several blocks that 
occupy N bytes than to find one contiguous N-byte block.

I find it surprising that this wasn't a concern in Fortran code in which
all sorts of optimizations are blessed in the name of performance. 

Nowadays, computers have so much memory that it's a lot easier for the 
memory manager to find those contiguous blocks, so this probably isn't a
measurable performance hit anymore (if it ever was). However, it paves the
way for the next disadvantage...


## Disadvantage 4 - Masks Overrun Bugs
Like C, Fortran allows one to use invalid array indices. In other words, if
an array is declared like this -- 
```
#!fortran
real*8     sigma(50)
```

Fortran will happily allow one to access `sigma(51)`, `sigma(100)`, etc. 

There are two aids that can expose this kind of mistake. 

First of all, one can ask the compiler to add bounds checking to the code. 
I don't know how effective this is in the common case where an array is declared in one function
and then passed to a second function which declares it as `foo(*)`, but 
it's better than nothing.

Second of all, there's a chance that writing beyond the end of an array will
attempt to write into memory that doesn't belong to your process. That will
trigger a segfault which is a crystal clear sign that something is amiss.

In this code, due to the fact that the work arrays are created from one 
subdivided array, neither of these aids is likely to rescue the programmer from 
an overrun bug. That's because if I write beyond end of the array that's in 
one slice of my uber-work array, I'm just trashing the values in the neighboring
subarray. I'm not going beyond the bounds of my 
array as far as the compiler is concerned, and I'm still writing to my own
memory so I won't segfault.

One of these bugs exists (I think) in `zlansvdw.f`. The code in question looks
like this -- 

```
#!fortran
do i=1,n
	work(iq+(i-1)*(lanmax+1)) = one
end do
```

(FYI, this code is right before the "DIVIDE-AND-CONQUER BIDIAGONAL" comment.)

In this code, n is 2048 (when ndp == 4096) and lanmax is 50, so the loop above 
writes to a max index of `iq + (2048 * 51) = iq + 104448`. So far, so good. 

If we look at the code that defines `iq` and friends (in `zlansvdw.f` just 
below the comment `Set pointers into work array`), we see that the subarray
after `iq` starts at `lanmax**2`. In other words, only `50**2 = 2500` bytes are 
reserved for the subarray starting at `iq`, but the loop above writes far
past `iq+2500`.

It doesn't fail because the definition of `lwrk` in `hlsvdpro.f` is 
larger than necessary, but it is certainly writing to both subarray at iq and 
the subarray to the right of it. It's hard to tell if this code is intentionally
devious or just buggy.


## Disadvantage 5 - Masks Wrong Index Bugs
In `zlansvdw.f`, there's a piece of code just 
below the comment "`Set pointers into work array`" that looks like this --

```
#!fortran
lwrk = lwork-iwrk+1
```

This defines lwrk as the length of a subset of the real `work` array.

However, when `lwrk` finally gets used, it refers to the length of the complex `zwork` array.

If the subarrays were individually declared, each would have its own length
variable and this sort of bug could not occur.


## Disadvantage 6 - All Arrays are Global
Any function to which `work` and `zwork` are passed has access to all of the
subarrays in them. The function probably doesn't write or even read all of 
those arrays, but one has to look at the code to figure that out. 

If the subarrays were individually declared, every function that needs to
read or write an array would need that array passed to it, so the array would
appear in the parameters list. That aspect of the code would become self 
documenting instead of being entirely undocumented as it is now.

