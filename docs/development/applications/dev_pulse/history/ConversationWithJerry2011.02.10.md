# Q&A on Gradients, Calculation-Resolution, create_pulse_base_tab, etc

  * *What is the relationship between F2 and G2 - Do you always have one with the other?*  You can have a G2 without an F2, but you cannot have an F2 without a G2. You get an F2 when you you are moving a pulse off isocenter (i.e. if getting slice images of the brain) and if the pulse is also remapped (i.e. we have a B2 and a G2). So in summary; when you have a G2 you _sometimes_ have an F2.

  * *Is B2, G2 just the remapped version of B1, G1?* This is mostly correct. However in B1/G1 case, the G1 can be changed without affecting the B1 to just get a wider or more narrow slice.  In the case of the remapped version (B2/G2), they are now tightly coupled so a change in B2 will need to have an appropriate change in G2 and vice-versa.  I.e. they are no longer independent.

  * *Do we have to have a gradient? Is there any assumed gradient?*  No and No.

  * *Are the time-points of G2 and F2 the same?* Yes.

  * *Are the time points of G2 the same as for the time domain pulse?*  Not necessarily, but they are generated that way in Matpulse, and we can do the same for the beta version of RFPulse, but we may want to either change this later or put in some tools to modify the time points for G2/F2 later.  The ultimate issue is that when you load the gradient onto the machine the gradient raster time is not necessarily the same as the dwell-time (and in general they are very different). So the gradient will need to be "downscaled" to a lower resolution point grid to load onto most machines.  

  * *Can we come up with a more descriptive name for calc. resolution?* Perhaps, "Frequency Resolution", as that is how it is used, in calculating the frequency domain properties using the Bloch equations and in the SLR calculations in the frequency domain transformation.  *NOTE ALSO:* There is a constraint that must be met for the calculations to work... something like this: Calculation-resolution must be greater than or equal to 4.0 times the number of time-points.  This should be coded into the UI as a hard limit.

  * *Are the parameters in panel_create_pulse.py the basic set for creating most new pulses?* I Briefly showed Jerry my UI for Creating new pulses... and he agreed that the input fields above the slr specific fields, i.e. those in auto_gui/panel_create_pulse.py, are the pulse parameters that all pulses should have or use.

