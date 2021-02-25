# GAMMA Overview
GAMMA is a computer package designed to facilitate construction of programs that simulate magnetic resonance phenomena in both solids and liquids. [PyGamma PyGAMMA] is a Python wrapper that makes much of GAMMA available via Python.

GAMMA is a library that provides data types commonly used to formulate MR problems, like spin systems, pulses, delays, Hamiltonians, and the like. By using this library to simulate magnetic resonance (MR) experiments, one can dramatically reduce the amount of work required to get a result.

Not only are GAMMA-based programs shorter, they tend to be clear and concise because source code can be written which closely mimics the mathematical or experimental formulation of the problem. 

## Under the Hood
GAMMA has implemented it's own matrix type, along with row vectors, column vectors and complex numbers, and has implemented a wide variety of calculations and manipulations of these types.  

In addition, GAMMA has created objects representing a host of MR related types.

The GAMMA source code is divided into the following modules --
```
Basics:            GAMMA constants, spin isotopes, parameter I/O.
Matrices:          GAMMA complex numbers, matrices, and vectors.
Input/Output:      Reading/Writing formatted data (MATLAB, FrameMaker, Felix, ...)
Hilbert Lib:       Making spin operators, Hamiltonians, pulse & delay propagators, etc.
Level 1:           Tensors, Wigner rotations, exponentials & Lorentzians, etc.
Liouville Lib: 	   Making superoperators, Liouvillians, steady-state density operators, ...
Level 2:           Transition Tables, Acquisitions, base decomposition, Bloch equations, ...
BWR Relaxation:    Isotropic relaxation ala Bloch, Wangness, and Redfield.
Rank 2 Interact.:  Dipolar, quadrupolar, CSA, Hyperfine, electron GAMMA, ...
Pulses:            Composite pulses, waveforms, pulse trains, broad-band decoupling.
Floquet Operators: Spin solids, MAS, DOR, ...
Multi-systems: 	   Interacting spin systems, exchange, ...
```

The Hilbert module includes functionality for construction of any spin operator, and any {ideal, rectangular, shaped} pulse. Base decompositons and Hilbert space analysis functions are also included. 

The Level 1 module also includes general spatial and spin tensors, Wigner rotation matrices and elements, and Clebsch-Gordon coefficients. Finally 3D coordinates are included as well as vectors of such coordinates. 

The Liouville module classes provided here are super_op, general superoperators, and sys_dynamic, isotropic dynamical spin systems. Functionality is included for construction of simulations programs acting in Liouville space and lay the foundations for dealing with relaxation and exchange problems. Acquisition functions and Liouville space analysis functions are also included. 


