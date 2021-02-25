# What I Gleaned at SciPy 2009
## Philip
I focused on learning about two things while at the conference: packages that could help us talk to other languages (C, C++, Fortran) and packages that could help us speed up code.

### Cython
Cython falls into both categories. For wrapping code, Cython could challenge ctypes and SWIG for some uses. I don't want to get into a compare/contrast of Cython, ctypes and SWIG here, but that would be a useful document to write at some point.

Cython can also provide a small code speedup with little investment.

 - Brian: I came away with the thought that Cython would be a good way to improve bottlenecks in our algorithm code, and that if we were smart about it, we could do a pure-python AND a Cython variant depending on whether a user had a compiler or not. 

 - Brian: which brings us to the DISTUTILS question. All my questions about how to distribute Cython solutions or what would happen on platform A versus B were deferred to answers along the lines of "that is dealt with in DISTUTILS". So we may need to do some soul searching through that package if we're going to provide Cython solutions and still want to estimate the "cost" of maintaining our distribution.

I don't remember hearing anyone mention SWIG.

 - Brian:  at the same time, they were not too disparaging of SWIG either ... also they never really got to the examples of how to wrap existing code. Examples exist in the Cython website tutorials, but they seem to be for C functions, not C++

At a BoF meeting, I learned that most of the main developers on Cython are distracted with other things for the foreseeable future (12 months or so). They won't be AWOL but we should not expect many changes to Cython except for bug fixes. Dag speculated that the next source of dedicated effort will most likely come from a Google Summer of Code student.

### fwrap
I also learned about fwrap, a Fortran-to-Python convertor. I spoke to the lead developer (Kurt Smith) at a BoF session and he told me something interesting. Fortran has had an unusual growth pattern. Most languages add features as they age making them more difficult to parse. That's not the case with Fortran. 

F77 has roots in the wild & wooly days of computing. The specification had holes and compiler writers filled them as they saw fit. F90 tightened up the language and added features to make it easier for Fortran to talk to other languages. As a result, it's easier to parse F90 code than F77, and his project has focused mostly on the former. He said that fwrap cannot yet challenge f2c for handling edge cases in F77 code. fwrap isn't exactly flush with developers, and so it might never outdo f2c for F77 code.

