# Remapping

The intention of this tool is to keep the same tip angle (or total rotation) and/or shorten the pulse, while reducing the Maximum Radio Frequency Amplitude, and keeping track of the maximum Gradient and slew rate.

## Fields/Variables:
*Machine Name (optional)*: "Using 7T SMIS INSTR": Should be the name the user gives to this machine.

*Gmax*: Gradient max. Set to the machine setting for gradient max: However, users may want the ability to impose a lower limit. Jerry even allowed users to use a higher value than that allowed for the machine and made the field be yellow (*) if it was higher than the value in the machine settings. This value affects the "New Dwell Time".

*Slew (a.k.a. Gradient Slew Rate)*: Set initially to the value assigned in the machine settings. Jerry allowed users to experiment by changing this lower or to make it higher (field would turn yellow (*) if higher).

(*) Karl, Jerry and I discussed how to do this with the database in RFPulse (if desired). Perhaps set a non-compliant flag in the sqlite if the output is not compliant with the machine settings.

*RFm (a.k.a. Max RF Voltage)*: Set to the maximum allowed RF voltage based on the machine settings. This should/could depend on what coil is installed in the MR machine.

*Previous Grad*: Previous Gradient. Designed for a slice thickness. (gradient ==> slice).

*Previous Dwell*: In Matpulse this has a slider, but could leave out this control and make this a static field. It is the dwell time of the previous result.

*New Dwell Time*: This interacts with Gradient Max. Why the slider? Jerry implied that New Dwell Time affects Gmax, just as Gmax affects new dwell (NOTE: Will need to look at code to be sure)

*Resync Enabled*: Check box. If checked, will make sure pulse ends where gradient is still "full on".

*Backup Enabled*: Check box. If checked, it adjusts last few steps of RF pulse and gradient (to comply ??) with Maximum slew rate.

*Continuous Gradient OR Last-step backup*: Radio Box, choose one or the other. _Jerry to check what this is for._. Update on this; Jerry will see if this still works and if we need it still. If we keep this:
  1. Jerry may need to change how we specify the refocusing gradient, i.e. in absolute terms (milliTesla/meter * milliseconds) rather than in fractions of the original gradient.
  1. Jerry may want to add refocusing for remapped pulses.

*Reset Inputs*: Put user interface back to initial settings.


## See, in Matpulse ...
  * REMAP\MRLCALCC.M
  * REMAP\MRLMMAP.M (Primary remapping program)
