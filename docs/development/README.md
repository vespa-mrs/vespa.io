---
sort: 3
---

# Development 

## Overview

Vespa is a free software suite composed of four magnetic resonance spectroscopy (MRS) applications called _Simulation_, _Pulse_, _DataSim_ and _Analysis_. These powerful tools are for magnetic resonance (MR) spectral simulation, MR RF pulse design, simulated MRS data creation and spectral processing and analysis of MR data.

Vespa's _DataSim_ application is new; the other three applications in the suite are rewritten versions of three existing MRS software tools  [IDL-GAVA/Gamma](http://cds.ismrm.org/ismrm-2003/0852.pdf), IDL-Vespa, and [MatPulse](http://www.mmrrcc.upenn.edu/downloads/matpulse.html). Vespa enhances and extends their capabilities and provides a free, integrated, open source, and open development platform. 

Vespa's applications run separately, yet can communicate via a shared database of objects and results. One example of inter-application sharing is that _Simulation_ can make use of an radio frequency pulse designed in _Pulse_ to create a more realistic MR simulation. The output of _Simulation_ can in turn be used as improved prior information in _Analysis_ for a more robust spectral fit of experimentally generated data. _Simulation_ output can also be used in _DataSim_ to create user defined MRS data sets with varying amounts of added noise that can be used to test algorithms in _Analysis_.

## All Topics

{% include list.liquid %}
