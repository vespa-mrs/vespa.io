## Matlab to Python Conversion Notes

### Useful Links
Scipy: NumPy for Matlab Users:
  * http://www.scipy.org/NumPy_for_Matlab_Users

Mathesaurus: NumPy for Matlab Users:
  * http://mathesaurus.sourceforge.net/matlab-numpy.html

Matlab Alphabetical List of Functions:
  * http://www.mathworks.com/access/helpdesk/help/techdoc/ref/funcalpha.html

Another Numpy for Matlab Users:
  * http://svn.assembla.com/svn/robelin/scripting/python/docs/numpyMatlabUsers2.pdf

### Notes
```
Matlab --> Python

%  --> #
&& --> and
;  --> ''     // i.e. Empty space

elseif --> elif

a^b --> pow(a,b)

a.*b  -->  a*b  
```

  * ';' is used in matlab to not-echo the results of the preceding code. To add back echoing of command results, just remove the ';'.

  * For '.*', the orientation of the vectors must be the same to work the same as in matlab. Matlab does not seem to care if the vectors are oriented differently, but in python it makes a big difference.  '.*' in matlab does an element by element multiplication. In addition, when converting a.*b to python the 'a' and 'b' must be numpy arrays for a*b to work.

  * a:step:b  --> np.arange(a,b+step,step), e.g. a = -1.0, b = 2, step = .5  ==> [-1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]

