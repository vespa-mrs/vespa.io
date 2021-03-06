# What Can Vespa Do for Me?
Listed below are some of the ways to use Vespa, both by taking advantage of the updated and extended capabilities of the individual packages, and working with the combined and integrated toolset. 

### Individual Packages
#### Simulation (in beta)
Simulation allows users to create sophisticated NMR simulations and provides the ability to incorporate subtle effects on spectra such as field inhomogeneities and chemical shift offset effects by allowing users to incorporate their own pygamma code in simulations. 

Additional uses for Simulation:

  * Create a metabolite basis sets for spectral fitting and analysis
  * Perform off-line optimization of parameters in an existing manufacturer pulse sequences. 
  * Test for sensitivity to chemical shift offset artifacts for given pulse(s), pulse sequence(s), and metabolite(s)
  * Maximize the signal for a specific metabolite and a given pulse sequence
  * Examine the effects of gradient waveforms on the spectra of metabolites
  * Enable off-line pulse sequence development - for new pulse sequences
  * Optimize signal editing for metabolites
  * Test the accuracy of published chemical shift and coupling values

#### RFPulse (in beta)
RFPulse allows users to design sophisticated RF pulses and provides an improved interface for the design of standard MR pulses such as SLR and Adiabatic (Hyperbolic Secant) pulses. Access to new functionality like generation of pulses via optimal control (forthcoming) will provide previously unavailable capabilities. 

Detailed usage for RFPulse:

  * Easily design Shinnar-LeRoux (SLR) and Hyperbolic-Secant pulses
  * Generates amplitude modulated RF pulses for a desired spectral response
  * Uses Bloch equation simulations for examination of pulse performance
  * Maintain the history (or provenance) of how the pulse was designed.

Planned in upcoming releases:

  * Deploy root reflection for generation of reduced voltage spin echo pulses, and self-refocused pulses
  * RFPulse will also include optimization routines to enable reduced voltage selective excitation, inversion, spin echo, and saturation pulses to be designed - as well as broadband (non-slice-selective) pulses with selected immunity to B1 inhomogeneity, and to resonance offset.
  * Generates re-mapped adiabatic "FOCI" pulses
  * Create a version of VERSE pulses using re-mapping
  * Allows the design of RF pulses in the presence of modulated gradients to reduce RF power and/or duration


#### Analysis (release forthcoming)
Analysis allows users to fit complicated NMR spectra using a variety of types of prior information. It also provides access to what was previously widely scattered and difficult to compare spectral analysis methods - including some that were previously unavailable, such as improved reference deconvolution methods.

Other Uses of Analysis for spectral fitting:
  * Test and compare a variety of time and frequency domain methods
  * Compare the utility of including a wide variety of prior information
  * Test and compare various lineshapes and baseline assumptions

### Integrated Toolset
As an integrated toolset, Vespa can be even more powerful that it's component parts. One typical use of the integrated package will be to iteratively design a RF pulse and test it's effect on the spectra of metabolites of interest. Details of the method for providing the pulses generated by RFpulse to the sequence design methods used by Simulation are under development, but a tutorial linked to below shows how to read a text file containing a list of real and imaginary values representing a pulse, into pygamma code for a simulation. Once you are satisfied with the resulting pulse and pulse sequence design, an experiment could be run and fit using the Analysis package and the Simulation results.

In this scenario, results generated by the Simulation package are used by the Analysis package for spectral fitting. This is one of the two major methods currently in use for providing basis function for fitting MRS data. The other method is to apply the pulse sequence to be used in the experiment to phantoms containing the metabolites of interest (provided that the eventual application will be to a sample containing the set of metabolites such as a biological sample) and to use the resulting functions as "basis functions" for the fitting procedure. Both methods have strengths and weaknesses, and both can produce basis functions that can be used by the Analysis package but for a number of reasons the authors are advocates of the method of generating basis functions via spectral simulation. 

The Vespa package is obviously and specifically designed to make use of spectral simulations, and the tutorials below focus on how to generate "basis functions" using the Simulation package.    