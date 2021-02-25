# Testing HLSVD
One of the traditional hallmarks of most computer programs is that they are
deterministic. For an input A, a deterministic program produces the output A'. 

The knowledge that a program maps A to A' enables us to test that changes 
to the code didn't break anything. This is the foundation on which 
automated testing is built.


The HLSVD algorithm and code we use (implemented principally by H. Barkhuijsen and W.W.F. Pijnappel) is deterministic. However, that determinism has limits. The algorithm and code are very sensitive to their environment. 

For instance, we compile the same code using GFortran under OS X, Linux and Windows. For some inputs the results are the same or similar across platforms, but for other inputs the results differ significantly. We see similar differences when we use f2c to convert the code to C and then compile with gcc on all platforms. Results for some inputs match, others don't. When we use updated LAPACK code (the LAPACK files that we've been using are from the early 1990s), once again we see some different results.

## This Is OK
For most code, giving different output for the same input would signify a 
problem. Not so for HLSVD. HLSVD attacks a problem that has one perfect 
answer and many adequate answers. The perfect answer is prohibitively 
expensive to compute but adequate answers are within reach, and those
adequate answers are what HLSVD provides. 

Since there are many adequate answers (some better than others), slight
differences in floating point calculations can send the algorithm towards
a different solution -- different, yet adequate, and therefore not incorrect.

## An Example
I ran HLSVD on OS X, Windows and Linux using input based on our sample data 
file press_cp5. For the purposes of this discussion, I'll pay attention only
to the amplitudes reported by HLSVD. 

The amplitudes were in almost perfect agreement under Linux and Windows.
The OS X results differed wildly in an element-by-element comparison. 
For example, under OS X, the 19th amplitude was ~435; under Linux and
Windows was ~0.5.

This looks like a disaster until one graphs the results
as below. The chart compares OS X's amplitudes (in blue) to those of 
Linux in yellow. (Windows is represented in red, but its amplitudes are so
close to those of Linux that Windows' red line is just buried beneath the 
yellow.) One can see that the results on all three platforms are not so 
different after all.

[[Image(amplitudes_raw.png)]]

In fact, by moving portions of the curves, we can see that the results
match pretty closely as in the graph below.

[[Image(amplitudes_phased.png)]]


## Practical Considerations for Testing
Without graphing each and every case where results differ, we can't say
whether or not it has behaved well. This is OK for a human who visually
inspects HLSVD's output. It's bad for anyone that wants to run automated
tests. Automated testing is difficult when the desired outcome isn't known.

Without resorting to fairly complicated tests, automated testing isn't 
going to be a reliable way for us to test HLSVD. 


## Attachments
Attached is the LibreOffice spreadsheet I used to make the charts.
