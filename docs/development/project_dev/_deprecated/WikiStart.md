# Welcome to the Vespa Project (Versatile Simulation, Pulses and Analysis)
Vespa is a free software suite composed of four magnetic resonance spectroscopy (MRS) applications called _Simulation_, _RFPulse_, _Priorset_ and _Analysis_. These powerful tools are for magnetic resonance (MR) spectral simulation, MR RF pulse design, simulated MRS data creation and spectral processing and analysis of MR data.

Vespa's _Priorset_ application is new; the other three applications in the suite are rewritten versions of three existing MRS software tools  [IDL-GAVA/Gamma](http://cds.ismrm.org/ismrm-2003/0852.pdf), IDL-Vespa, and [MatPulse](http://www.mmrrcc.upenn.edu/downloads/matpulse.html). Vespa enhances and extends their capabilities and provides a free, integrated, open source, and open development platform. 

Vespa's applications run separately, yet can communicate via a shared database of objects and results. One example of inter-application sharing is that _Simulation_ can make use of an radio frequency pulse designed in _RFPulse_ to create a more realistic MR simulation. The output of _Simulation_ can in turn be used as improved prior information in _Analysis_ for a more robust spectral fit of experimentally generated data. _Simulation_ output can also be used in _Priorset_ to create user defined MRS data sets with varying amounts of added noise that can be used to test algorithms in _Analysis_.

## Get Vespa
 * [How to install Vespa](/wiki:HowToInstallVespa/)
 * [How to upgrade Vespa](/wiki:Upgrading/)

## Join the Vespa Mailing List
 * Browse or join [the mailing list](http://groups.yahoo.com/neo/groups/vespa-mrs/info)

## Learn About the Vespa Project
 * [Motivation for Vespa](/wiki:BriefHistory/)
 * [A detailed description of Vespa](/wiki:LongVersion/)
 * [What can Vespa do?](/wiki:WhatCanVespa_Do/)
 * [wiki:FAQ] - Frequently Asked Questions


## Vespa Application Wikis
 * [Simulation - MR spectral simulation and display](http://scion.duhs.duke.edu/vespa/simulation)
 * [Pulse - RF pulse design and display](http://scion.duhs.duke.edu/vespa/pulse)
 * [Priorset - user defined, simulated MRS data](http://scion.duhs.duke.edu/vespa/priorset)
 * [Analysis - MRS data processing and analysis](http://scion.duhs.duke.edu/vespa/analysis)

## Project Info
 * [TheDevelopers Personal profiles of the developers]
 * [About our open source license](/wiki:Licensing/)
 * [TechnicalDocumentation Technical documentation for developers]
 * [wiki:Acknowledgements]

Thanks to the *NIH* (*grant number 1R01EB008387-01A1*) which funded the maintenance and extension of these separate applications into a combined environment based entirely on the Python language.