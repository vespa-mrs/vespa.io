# Performance of Optimal Control: RFPulse vs Matpulse
BJS - leaving this page for historical reference

Optimal control is a highly compute intensive application.

## Experiment 1
Initial condition:
An SLR pulse created with the default parameters, except using 128 points.

Target of OCNS optimization: 
Default parameters, other than 93 degree tip, and 1.5 kHz bandwidth, and 1000 iterations.

Matlab: 54.46 seconds
RFPulse: 5 minutes (300 seconds)

*Matpulse was 5.5 times faster than RFPulse*


## Experiment 2
Initial conditions:
SLR pulse created with the default parameters, except using 128 points.
i.e. 90 degree, excite, 1 kHz, etc.

Target of OCNS optimization:
Spin-Echo, 180 degree tip, and 800 iterations


RFPulse: 5 Minutes
Matpulse: 60.722

*Matpulse was 5 times faster than RFpulse.*