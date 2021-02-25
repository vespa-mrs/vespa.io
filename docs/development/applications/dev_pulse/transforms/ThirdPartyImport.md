# Third Party File (Pulse) Imports
For when a user of RFPulse wants to import a simple text file that contains R.F. pulse data.


We can make it support multiple formats of input data. The simplest (most common? or used by Matpulse) will be done first - which is a list of complex data points in the format: Amplitude <space> Phase (in degrees). We will program in the first format in the list below, but could support others - if requested by users:

  * Amplitude <space> Phase (in Degrees)  # used by Matpulse
  * [not in first implementation BJS] Amplitude <space> Phase (in Radians)
  * [not in first implementation BJS] real, imaginary # either with or without the comma.

We will assume the values in the pulse are in microTesla.

## Input Fields

*File Name and Path* - The file name and directory location.

*Comment Field* - Some user supplied information regarding what they know about this file and how it was created and where it came from, etc.

*Dwell Time* - The spacing between the points. In the representation of this pulse, we will create a histogram with one 'tower' or 'bar' for each point. So for two points there will be two 'towers' in the histogram, not one. 

Alternatively, we could allow the user to specify *Total Time*, so we might have two check boxes so a users can choose one or the other. Assuming we read in N points from the file, and the user supplies the total_time field, we would make the dwell_time equal to: dwell_time = total_time/N.

We will need to make sure the dwell time is consistent with the machine settings too, and perhaps adjust the total time a little to make this work out (e.g. as done in the Create SLR pulse).

*Pulse Max* - [not in first implementation - let users add a Scale transformation if they want this?? BJS] Scale factor for the overall intensity. Scale the maximum of the pulse to the "Pulse Max" value. We should probably scale the absolute value of the pulse (e.g. we might be scaling the negative portion to -PulseMax). We should not allow the user to exceed the B1 maximum for their machine settings. If the do we should pop up a Error Message that "This Pulse Violates your B1 Max value for your Machine settings". We could suggest the largest "Pulse Max" value that they can input for this to not violate this constraint.

*We will ignore all lines that begin with a ";" or a "#" or that only have white spaces (tabs or spaces).

