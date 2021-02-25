# Welcome to Vespa Priorset
Vespa-Priorset is an application written in the Python programming language that allows users to interactively create and save simulated MR spectroscopic data. It's part of 
[project:wiki the free, open source Vespa suite]. Vespa-Priorset allows users to: 
  1. Select a Vespa-Simulation Experiment from the Vespa database to serve as the underlying basis set for the simulated priorset.
  1. Select which metabolites to include in the simulated priorset.
  1. Set individual metabolite areas and T2 decays.
  1. Set global spectral resolution, T2* decay, B0 shift, and zero order phase.
  1. Include random noise at the simulated time domain FID level to achieve a desired SNR level.
  1. Create arbitrary 'baseline' signal contributions with independent area, ppm and line width values.
  1. Observe graphically the results of setting up the priorset ‘on the fly’.
  1. Save a Priorset workflow into a human readable XML format that can be opened later and re-used. 
  1. Export simulated priorsets into Vespa readable VIFF and other formats.
  1. Export Monte Carlo priorsets with fixed metabolite levels but different sets of added noise.

## Documentation and Resources
 * [project:export:/trunk/vespa/docs/priorset_user_manual.pdf The Priorset user manual (PDF)]
 * [wiki:FAQ] - Frequently Asked Questions
 * [wiki:Acknowledgements] - Contributors and inspirations!

