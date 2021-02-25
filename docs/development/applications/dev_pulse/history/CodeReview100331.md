## general
 * In general the code looks quite good.
 * Glad to see that your comments reference the source of the algorithms 
   you're using.
 * Several of functions contain magic numbers. There seem to be two 
   categories. The first can easily be replaced by enum-style constants. 
   filetopython_cp.py contains two good examples; `bandwidth_convention` and
   `band_type` should both be compared to predefined constants instead of raw
   ints.
   
 The second kind of magic number is more difficult; I don't know enough to
 assess what can/should be done. Let's take `linear_setup.linear_setup()` as 
 an example. 
 It contains this line:
```
 while abs(f) > .00001 and n < 100:
```

 From where do the numbers .00001 and 100 originate? It'd be nice to know. 
 The problem is that there are tons of numbers hardcoded in these files, and 
 it'd be impossible to comment every one. At some point you just have to say 
 "That's how the math is done". I don't know how to make these judgement 
 calls because I don't know the math & science, so it might be obvious to 
 everyone but me.

 * PLease use `FIXME` instead of just `FIX` in comments
 * There are a lot of inline comments which PEP 8 recommends to "use 
   sparingly". Yours are well chosen and helpful which IMO is more important 
   than their location, so I'm not worried too much about whether or not 
   they're inline. Nevertheless, their use is mildly discouraged.
 * PEP 8 also recommends an 80 column line width limit. Sometimes I break this
   but generally respect it.
 * Take it easy with the import aliasing. This is a bit obscure:
```
   import scipy.signal as sps
```
   Me, I probably wouldn't alias it at all, or if I did it would be like so:
```
   import scipy.signal as signal
```
   But there's a module in the Python standard  lib called `signal` so my 
   choice would be worse than obscure, it'd be downright misleading. I can't 
   think of a good abbreviated alias for this module.


## fir_least_squares.py 
 * In `firls()`, params should all be lower case. Ditto for variables used in
   the code. All upper case is reserved for constants, CamelCaps is reserved 
   for classes. This is probably annoying for you since you have both R and r
   used as variables and I suppose there's some good mathematical reason for 
   that, but it ain't Pythonic. 
 * In `firls()`, since the param f is a list of tuples, a brief example in the
   comments would be nice to show what kind of tuples are expected.

## linear_filter.py 
 * Don't use '`from xxx import *`'. See our coding standards for reasons 
   why; search the coding standards page for "from some_package import *".
 * In `linear_filter()`, condense the docstrings into one. 

## linear_setup.py 
 * In `linear_setup()`, there's a number of instance of this:
    ```
       if foo == True:
    ```
   Typically, Python code just says this:
    ```
       if foo:
    ```

     When I see an explicit comparison to True or False, it makes me wonder what 
     values the variable might have. There's a good example in this file:
    ```
        if is_single_band == True:         # Single band pulse
            fr = [0, fp, fs, 1]
            mag = [magn, magn, 0, 0]
            wts = [wt1, wt2]
        elif is_single_band == False:         # Dual band pulse
    ```
     I could infer from the explicit checks that `is_single_band` is a tri-state
     variable, perhaps with the 3rd value being None. In this case you chose a
     good, clear name that indicates it is a boolean so I wouldn't get too 
     distracted thinking about whether or not it is tri-state. But this would 
     be clearer:
    ```
        if is_single_band:         
            fr = [0, fp, fs, 1]
            mag = [magn, magn, 0, 0]
            wts = [wt1, wt2]
        else:
            # Dual band pulse
            etc.
    ```
 * At the end of the function you can just say this:
    ```
       return (fr, mag, wts, corrctf)
    ```


## min_max_filter.py 

 * in `max_min_filter()`, condense the docstrings
 * On line 246, there's this:
    ```
     min = magn[0::2]    
    ```

     That overwrites the Python builtin function `min()`! See here for a example
     of the consequences:
    ```
     >>> min( [1, 2, 3] )
     1
     >>> 
     >>> min = 42
     >>> min( [1, 2, 3] )
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     TypeError: 'int' object is not callable
     >>> 
    ```


## mrs_rfpulse.py 
 * In the `PulseParams` class, thank you for all the comments in `__init__()`.
 * LIne 101, change this:
    ```
            if wave_profiles != None:  
    ```
 to this:
    ```
            if wave_profiles:
    ```
 * Line 104, is `self_waveform_x_axis` a typo for `self.waveform_x_axis`?
	
 * You can discard `write_to_xml()` and `read_from_xml()` if you want. 

## transition_band.py 
 * Don't alias imports to capital letters. There's nothing technically wrong
 with doing so, but it is entirely unconventional.


