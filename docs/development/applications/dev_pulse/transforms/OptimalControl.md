# Optimal Control (Non-Selective)
_Version 1: Broadband B1-Immune Pulse Design_

This tab takes any pulse type and shape as an input. 
Some papers on Optimal Control (OC) have even used random pulses (noise) to start things off.
However, in some cases it helps to start with a pulse that is close to what you want.

In this tab you specify a certain number of points Npoints and a bandwidth, and Optimal Control will try to get uniform tipping over that bandwidth. It does this by minimizing the average residuals for these Npoints - distributed evenly across the bandwidth - and for the B1 immunity range (e.g. -20% to 20%).

When using optimal control, we are optimizing the pulse by getting the best fit to the Bloch profile.

## Usage
The uses for Non-Slice-Selective pulses generated from optimal control.
  * Useful for high field (>=3T)
  * Designed for 3D MRI sequences
  * Provide Immunity to B1 inhomogeneities and resonance offset
  * Can be applied using conventional coils
  * Applicable to high resolution NMR Spectroscopy (Skinner/Glaser).
  * One can generate a large range of tip angles.

## Potential Issues/Questions
  * How to Implement the "Stop" button

## Fields/Variables
**A** - Items considered by Jerry to be "Advanced" or that can be placed on the "advanced" options page.

*Load Button*: Jerry used this to "pull-in" new initial data to work with. So if you want to start over again with a new initial pulse, this would be what you would use.

*Dwell, Length, Pulse Points*: These values are calculated from the input pulse. i.e. the dwell time, the Length in milliseconds, and the total number of points. They are used only for reference.

*Pulse (Optimization) Type*: This is the pulse type you are trying to make. Choices are Excite, Saturation, Inversion, and Spin-Echo. What you select from the drop down affects what is displayed as choices from the "phase type", i.e. which of these choices {Coalesced, Non-Coalesced, Linear Factor} is available. Defaults to Excite.

*Phase-Type*: The choices that are displayed depend on what Pulse Type selected.
  * For EXCITE we have two choices:
    * *Coalesced*: The phase of all magnetization in the transverse plane is the same.
    * *Linear (Factor)*: Implies that there is a linear distribution of phases in the transverse plane, i.e. that could be refocused using a gradient. NOTE: Linear is a type of Non-Coalesced pulse (the other types are Min and Max phase).
      * *Factor (numerical value)*: This is thought of as the fraction of the area under the gradient waveform - applied during the pulse - that needs to be applied in the opposite direction to achieve refocusing. Mathematically it is the numerical 'factor' in the expression: profile*e**(-i*2*pi*f*tau*factor) required to obtain refocusing. Default is 0.5. Real number.
  * For all the others we don't have a choice.  i.e.
    * SATURATION ==> Non-Coalesced
    * INVERSION  ==> Coalesced
    * SPIN_ECHO  ==> Coalesced

*Tip Angle*: The target tip angle for this optimization. Defaults to 90 (degrees). Real number.

*Bandwidth (kHz)*: Jerry called this "Excitation (kHz)", but preferred the name Bandwidth. Simply the bandwidth of the pulse. Defaults to 1.5. Real number.

*Initiate*/*Control*: These choices are mutually exclusive. They affect what value is used for the "Step Size Multiplier", in the subsequent runs of Optimization. So if you are in the middle of an optimization, the step size multiplier being used under the hood may not be the same as what was initially specified for this value.  If you stop the optimation, this determines if you should continue using the internal value, or re-*initiate* the value with what is specified in this input box. Even if you load a new pulse, if you use *continue* it will start the optimization with the internal value not (necessarily) the displayed value. Defaults to "Initiate".
  * *Initiate* - When hit "CALC" use the displayed value for the Step Size Multiplier.
  * *Continue* - When hit "CALC" use the internal value for the Step Size Multiplier.

*Step Size Multiplier (.1 to 1.0)*: This is a multiplier that is used to decide the step size to take along the minimization gradient to get to the next point (for checking residuals). Called "Initial Step Size" in Matpulse. The "(0.1 to 1.0)" indicates the typical-usage, or suggested, range. After discussing with Jerry we decided on changing the name to Step Size Multiplier to indicate the fact that this number may not change as you get close to converging but the actual step size will get smaller. So it is actually used as a multiplier for the fitting process and not as the actual step size.  How this might change during the fit is determined by choice of {Average, Fix Size, or Compute}. Defaults is 0.5. Real number.

*Average*/*Fix Size*/*Compute*: Mutually exclusive choices. Perhaps we can call this group something like "Step Size Modification". This defaults to Average (and this is also Jerry's preferred choice).
  * *Average*: The new step size multiplier will depend on the percent success of last 100 steps (what percent led to and increase or a decrease in the residual errors).
  * *Fix Size*: the step size multiplier will not be changed.
  * *A* *Compute*: Jerry's observation is that this did not work very well.

*Excitation Band Points*: the number of points to fit. The points will be spread uniformly (???) along the bandwidth in the profile.  Default to 41. Integer.

*B1 Immunity Range*: This, along with the "Steps" field, determine the specific profiles that will be fit for this optimization. Starting at a -B1immunity with steps size of 2*B1immunity/(Steps -1), all the way up to +B1immunity.  For example if Steps=5 and B1 Immunity Range is 20 then OC will use 5 profiles at -20, -10, 0, 10, and 20. OC will minimize the average residuals over these profiles (for the number of Excitation Band Points specified).  Default value for B1 Immunity Range is 20. Real Number.

*Steps*: Determines the number of profiles to use in the minimization. This and B1 Immunity Range determine the specific profiles used (See B1 Immunity Range). Default value is 5. Integer.

*Limit B1 Maximum to*: Used as a cutoff value for the maximum B1 field.  If the pulse output from the current iteration has fields above the max, the pulse will be "topped" at this value. The alternative would be to put a fitting penalty on values above the max, but this apparently works as well, perhaps by not giving any advantage to going higher that the max.  Default is 25 (microtesla). Real Number.

*A* *Limit SAR*: Check box. Used to indicate application of additional subroutines, that take the SAR Factor as an input.  Jerry suggested leaving this off for now or put in and "Advanced" sub-tab or pop-up panel. I believe (???) Jerry was not happy with the results this gave and perhaps someone else may have a better way of applying this. [note: SAR==>Power==>(rf)**2]. Default to not checked.

*A* *SAR Factor (0.1 to 1.0)*: Input to 'Limit SAR' subroutines. Not used if 'Limit SAR' is not checked. Range is 0.1 to 1.0. Default to 0.5. Real Number.

*Error Increase Tolerance*: The maximum allowed fractional residual increase (or something close).  Range is 1e-6 to 1e-3. Default if 1e-4. Real Number.  Is this for the last few 100 iterations or for a single iteration ???

__The Minimization routine may not stop - unless one of the following four criteria is selected - or the "Stop" button is hit. These items are NOT mutually exclusive.__

  1. *Max Iteration Number*: Check box and data input field. If selected it uses the Number specified to determine how many iterations should be executed before the optimization is finished. This is an absolute number, i.e. it is not in units of 100 iterations, etc. Default of check box is unchecked. Data input field default is 64. Integer.

  2. * Residual Error (%)*: Check box and data input field. Tells optimization to stop once the residual error is below a certain %. Default of check box is unchecked. Data input field default is 0.2 (percent). Real Number.

  3. *Differential Error (%):*: Check box and data input field. Tells optimization to stop if the error has not changed by more than the specified amount in the last 200 iterations. Default for check box is unchecked. Data input default is 1e-4 (percent). Real number.

  4. *A* *Halt if Error Increasing*: Check box. Indicates that the Optimization should be stopped if the error begins to increase. It looks at the last 200 (to 400?) iterations. Check box default is unchecked.


*Clear*: button. Doesn't really clear input, but rather closes the window. Is this what it is designed to do???

*Stop*: Pauses the optimization. One could load new data to optimize on, change some of the fitting variables, etc.

*Calc*: Begin (or restart) the optimization.

*A* *Enforce Symmetry*: If selected, this makes the real part of the __pulse__ symmetric and the imaginary part of the __pulse__ antisymmetric. Jerry only applies this to Spin-Echo pulses (so we might want to put that constraint on this), e.g. only make it available for spin-echo. This is not part of the current UI, but is currently read in by Op_Con_Adv function from a file. Boolean.


NOTE: At every 100 iterations this writes out the results, and also keeps in Memory (the Matlab/Matpulse workspace) the final results.


## See, in Matpulse...  * ZOPT/...
  * Import functions in OC_B1_Insen_Sel, OC_B1_Insen_NonSel, OC_Selective, SLR, Cplot and Auxilliary.
  * e.g. in OC_B1_Insen_Sel, 
    * ocsel_calc.m
    * Op_Con_Sel.m