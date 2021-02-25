# Benchmarks of PyGAMMA Using SWIG's -builtin Option
## Summary
[SWIG 2.0.4](http://sourceforge.net/news/?group_id=1645&id=300581) introduced a
new `-builtin` option that replaces pure Python class wrappers with Python
objects implemented in C++. According to SWIG's documentation, it "is
especially suitable for performance-critical libraries and applications that
call wrapped methods repeatedly" (1). It "provides a significant performance
improvement" (2). I performed benchmarks to see how SWIG's new built-in types
affected some typical PyGAMMA scripts.

The option does indeed provide benefits, although they're modest. On my
laptop, the performance gain was roughly 1 second per 100,000 PyGAMMA calls.
Since there's no downside to using this flag, we'll enable it in our builds
and recommend it, but keep expectations low.


## Methods
I benchmarked two scripts on my laptop which is a MacBook Pro with two
2.53Ghz Core i5 processors and 8G of 1067Mhz DDR3 RAM. It was running OS X
10.6.8. During the benchmarks I disconnected from the Internet and ran only
apps essential for benchmarking (terminal, text editor, Python).

PyGAMMA was compiled with gcc 4.2.1 using the current version
([browser:/trunk/platforms/OSX/Makefile?rev=377 r377]) of the Makefile with
two changes. First, I changed the optimization from O3 to O2 because with 
O3 linking takes about 10 minutes on my machine and I'm impatient. Also, 
I obviously modified the SWIG options to include -builtin option when 
benchmarking that. 

My Python is 32-bit Python 2.6.6 from Python.org.

I ran two scripts ([attachment:fid.py fid.py, attached to this page] from our GAMMA test
suite, and [contrib:wiki:602e7450-8227-48eb-8252-38f8597d9342 basing3dj.py from the basing3dj sample]) three times for each scenario in the table below and took an average of
the results. Averaging results wasn't necessary since the differences between
results were nearly non-existent, but I did so anyway.

`basing3dj.py` was chosen because it makes a lot of PyGAMMA calls, and the
`-builtin` option is supposed to make the Python/C++ transition more 
efficient. `fid.py` was chosen for the same reason and the exact opposite
quality. It makes very few PyGAMMA calls, and so shouldn't benefit from 
builtin types.

In order to count the number of PyGAMMA calls made by each script, I created a
module (not included here) that wrapped all the PyGAMMA calls made by
`basing3dj.py` and `fid.py`. This module merely counted the call and then
called the appropriate PyGAMMA function. I didn't use that wrapper during
benchmarking since it would have altered the runtimes, but it was useful for
counting calls into PyGAMMA.

Although the purpose of this test was benchmarking, I did compare the output
of the scripts using PyGAMMA with and without builtin types. The results were
the same.

## Results

### basing3dj.py
This script made 379,484 calls into PyGAMMA.

||-builtin?||Script||Metabolite||Runtime||
|| ||basing3dj.py||gsh_test.sys||7.90||
||YES||basing3dj.py||gsh_test.sys||4.80||
|| ||basing3dj.py||creatine.sys||126.67||
||YES||basing3dj.py||creatine.sys||121.12||

Using `-builtin` was 7.90 - 4.80 = 3.10 seconds faster for `gsh_test.sys` and
126.67 - 121.12 = 5.55 seconds faster for `creatine.sys`.


### fid.py
This script made 8 calls into PyGAMMA.

||-builtin?||Script||Metabolite||Runtime||
|| ||fid.py||phenylalanine.sys||3.94||
||YES||fid.py||phenylalanine.sys||3.95||
|| ||fid.py||phosphorylcholine2.sys||52.78||
||YES||fid.py||phosphorylcholine2.sys||52.78||

Using `-builtin` was .01 seconds slower for `phenylalanine.sys` and no
different for `phosphorylcholine2.sys`.


## Discussion of Results
The script which made a lot of calls into PyGAMMA (`basing3dj.py`) ran faster
when PyGAMMA was compiled with the `-builtin` option, while the script which
was computationally intense but made few calls into PyGAMMA (`fid.py`) didn't
benefit at all. This bears out the assertions that SWIG's `-builtin` option
(a) improves traffic flow across the Python/C++ border and (b) has no
discernible effect otherwise.

If we divide the time that `basing3dj.py` gained by using `-builtin` (3.10 and
5.55 seconds) by the number of calls into PyGAMMA (379,484), we find that the
improvement for each function call is ~8-14 microseconds. This implies that
builtin types won't make much of a difference unless a script makes a
lot of PyGAMMA calls.

To look at it another way, it's interesting to see how many PyGAMMA calls it
will take to see 1 second of improvement. At a gain of 8 microseconds per
call, it will take ~125,000 PyGAMMA calls. At a gain of 14 microseconds per
call, it will take ~71,000 PyGAMMA calls to gain 1 second.



## References
1. [SWIG 2.0.4 release notes](http://sourceforge.net/news/?group_id=1645&id=300581)
1. [Documentation for -builtin](http://swig.org/Doc2.0/Python.html#Python_builtin_types)
 