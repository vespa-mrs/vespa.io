# Create Sinc-Gaussian Transformation
_Here are a few quick notes to guide the creation of the sinc-gaussian transformation._

The calculational code, for creating sinc-gaussian pulses as they are created in matpulse, is located in the file: 
  * vespa/common/pulse_funcs/analytic_pulse.py

The function to use is:
  * def sinc_gaussian(nop, cycles, filter_type, filter_percent, angle)

*nop* is the number of points.

For the GUI, one could use either the Gaussian transformation and add a few variables, or use the hyperbolic-secant and take away a few variables.