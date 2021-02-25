# Pulse Concatenation
This should be a "Create Concatenation" transformation.

* *Note: All segments require identical dwell and slew rate.*

Why have an adjustable slider for slew in Matpulse???

Specify gap between two pulses (There are at least 2 ways to specify this).
"Run" button adds the waveform.

The number of points in each pulse should not matter as long as the dwell time is the same.

When you save this project it will create a new UUID, and it should lock the two (or more) source pulse projects. 

  * Export: The source pulse projects should be exported with this new pulse project.
  * Import: The source pulse projects should be imported first. If that succeeds, then import the final resultant pulse project (although this should be an obvious part of the importation process. i.e. if one part fails the whole thing fails).


''Jerry to Review: He said this one was tricky and not "optimally developed"'

** NOTE2: I asked Jerry if we need to "keep track" of what refocused gradiant values (e.g. area and duration) are used by excitation profiles, and he said that the person building the concatenated pulse needs to worry (and not us as code designers)... and that there are tricks people play in terms of reducing the time between pulses by having the pre and post pulse gradients cancel each other out, or use the same gradient for refocusing as is used for the new pulse, but just add a small time delay. We'll see...

## See, in Matpulse...
  * STRING\MSLSM.M
  * STRING\MSLCALCC.M