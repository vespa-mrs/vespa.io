---
sort: 3
---

# DataSim Dev

## Overview

Vespa-DataSim is an application written in the Python programming language that allows users to interactively create and save simulated MR spectroscopic data. It's part of the free, open source Vespa package. Vespa-DataSim allows users to: 

1. Select a Vespa-Simulation Experiment from the Vespa database to serve as the underlying basis set for the simulated datasim.
1. Select which metabolites to include in the simulated datasim.
1. Set individual metabolite areas and T2 decays.
1. Set global spectral resolution, T2* decay, B0 shift, and zero order phase.
1. Include random noise at the simulated time domain FID level to achieve a desired SNR level.
1. Create arbitrary 'baseline' signal contributions with independent area, ppm and line width values.
1. Observe graphically the results of setting up the datasim ‘on the fly’.
1. Save a DataSim workflow into a human readable XML format that can be opened later and re-used. 
1. Export simulated datasims into Vespa readable VIFF and other formats.
1. Export Monte Carlo datasims with fixed metabolite levels but different sets of added noise.

## Topics

{% include list.liquid %}
