# Porting HLSVD to Python
This document was written before the port. It's an outline of the pros
and cons of porting and also contains a preliminary plan of attack. 
It's here for historical interest.

## Some Observations
### Porting in General
When porting any code from one language to another, one always has to decide
how much idiomatic translation to apply.
A certain minimum is always imposed by the differences in languages. A bit
more is within easy grasp (the proverbial "low-hanging fruit") and is 
worth doing. Too much, however, is too much, as I think most will agree.
The problem is that the we sometimes don't realize how deep the water is
until we take a step and find it over our heads.


The most straightforward kind of port is a rote, line-by-line, context-free
port that doesn't take into account the strengths and weaknesses of the
languages. For instance, consider this Fortran loop:
```
do 160 i = 1,kfit
   amp(i) = scale * amp(i)
```

The straightforward translation into Python would be as a "`for`" loop, but it'd
be more Pythonic (and faster) to express it as a list comprehension.

This is a small example of a larger topic. How much should one consider idiom
when porting? That question has no easy answer, but it's important to consider
because it affects the advantages and disadvantages below.

Rote, idiom-free ports require the least skill and understanding of the 
source material.
However, the result is never pretty. Even if the source is beautifully
written, it won't look so beautiful expressed in another language.

What's more, a completely rote, mechanical port usually isn't possible. For
instance, Fortran typically uses lots of `goto` statements which Python
doesn't have. Look at the goto statements in the code below (from `imtql1()`
in `hlsvdpro.f`). It's simply not
possible to mechanically port this to a `goto`-less language.

```
   20    do 30 m=l,n
            if (m.eq.n) go to 40
            if (dabs(e(m)).le.machep*(dabs(d(m))+dabs(d(m+1)))) goto 40
   30    continue
 
   40    p = d(l)
         if (m.eq.l) go to 80
         if (j.eq.30) go to 130
         j = j + 1
```

If the unpleasant part of porting is coping with features that don't exist 
in the target language, the pleasant part is taking advantage of features
that only the target language has. An obvious feature in this case would be
OOP. 

Once one gets sufficiently far into replacing flow control and variable names, 
and taking advantage of new features like OOP, one begins to leave the 
realm of porting and enter the realm of rewrite. This well-intentioned 
journey can end in disaster if one isn't careful.


## The Advantages of Porting
This assumes a port to pure Python using numpy. 

  - Easier debugging. The more Pythonic the port is, the easier it will be
    to debug.
  - Accessible to a wider audience. If other people are interested in this
    library, the Python version is probably more accessible than the Fortran
    version. (In any other discipline, this argument would be very strong.
    But Fortran's popularity in the sciences undermines it a bit.)
  - No binaries to schlep around in SVN, backups, end-user packages, etc.
  - No more fussing with Fortran compilers
  - Proper error handling (raised exceptions)

## The Disadvantages of Porting
  - The cost in time. This is the most obvious -- it will take some time to
    port this code.
  - New bugs introduced by the process.
  - Slower. By how much? We don't know.
  - Difficulty. Most of the Fortran code is chopped up into reasonable 
    functions, but some of it is nevertheless long and opaque.


## Suggestions
Port it like an onion.

We've already discovered that it's pretty straightforward to call Fortran
code from Python. All of the functions in the HLSVD Fortran code
are visible to users of the binary library, so callers 
are not limited to calling just `hlsvd_()`. They can also call `lanczo_()`,
`vanmon_()`, etc. This means that we can call any Fortran function at 
any time.

This makes it possible to port HLSVD like an onion, one layer at a time.

The file [project:browser:/trunk/hlsvd/src/hlsvdpro.f hlsvdpro.f] contains the 
subroutine `hlsvdpw_python()` is one of two wrappers around the function 
`hlsvdpro()` which is where the work really starts. One could start by porting
`hlsvdpro()` to Python, but without porting any of the subroutines that
it calls (`lanczo()`, `vanmon()`, etc.) Those 
sub-subroutines are the second layer of the onion. 

Port the first layer to Python and use `ctypes` to call into that second
layer. Once you've got the first layer in Python and it behaves correctly,
then you can tackle the second layer.

Onion-ing breaks the problem up into manageable pieces. The pieces give you
places to stop and take a breather. Onion-ing also modularizes the code which
makes it easier to hunt down bugs and performance problems.
