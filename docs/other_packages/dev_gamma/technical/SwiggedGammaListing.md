# Swigged GAMMA code
PyGAMMA's Python wrapper around GAMMA was created with [SWIG](http://www.swig.org/) (*S*implified *W*rapper and *I*nterface *G*enerator). We call the act of wrapping code "swigging" and we say that code that has been wrapped in this manner is "swigged". In other words, anything swigged is callable from Python.

Listed here (by directory) are the file prefixes of the .cc/.h files that were swigged. Any C++ file with an associated ".i" file has been swigged.

We believe that the majority of interesting physics code is swigged, but we may have missed something that you find important in your work. If you find that is the case, we have [ExtendingPygamma instructions on how to swig GAMMA files].

The functions that were made available to Python are all functions that are not listed as "friend" function in the .h files. With more work, many of these helper functions could also be swigged (In some cases, with minor reworking of the C++ code). See the link above if you're interested in helping this effort. 

Also, certain functions that handle I/O in C++ were not converted to Python as that's usually easier to handle in the native language.

*Basics* (Everything)
  * Gconstants  
  * Gutils
  * Isotope  
  * IsotopeData
  * ParamSet  
  * SinglePar
  * StringCut


*Bloch*
  * Bloch
  * BlochAcq
  * BlochSys
  * MagVec

*BWRRelax* (Everything)
  * relaxBWRexch
  * relaxDCSA
  * relaxExch
  * relaxNMR
  * relaxQCSA
  * relaxRand
  * relaxanalyze
  * relaxCSA
  * relaxDip
  * relaxJ
  * relaxProp
  * relaxQuad
  * relaxRF


*ESRLib*
  * No Files Swigged

*Floquet*
  * No Files Swigged

*GamIO*
   * No Files Swigged

*Gradients* (Everything that is not deprecated)
  * Gradients2
  * GrdAcquire
  * GrdEvolve
  * GrdPulses
  * sys_gradz

*HSLib* (Everything)
  * Basis
  * GenOp
  * GenOpRep
  * HSacquire
  * HSanalyze
  * HSauxil
  * HSdecomp
  * HSdetect
  * HSham
  * HSprop
  * PulseI
  * PulseShp
  * PulseS
  * SpinOpCmp
  * SpinOp
  * SpinOpRot
  * SpinOpSng
  * SpinSys
  * SpinSystem


*IntRank2*
  * No Files Swigged

*Level1* (Everything)
  * coord
  * coord_vec
  * Exponential
  * ExProcessM
  * Lorentzian
  * nmr_tensor
  * SpaceT
  * SphHarmic
  * SpinT
  * Wigner
  * WindowFct

*Level2* (Everything)
  * acquire1D
  * BaseDecomp
  * EAngles
  * MutExch
  * Quaternion
  * RelaxBas
  * TrnsTable1D

*LSLib* (Everything)
  * DensOp
  * LSacquire
  * LSanalyze
  * LSAux
  * LSprop
  * SuperOp
  * sys_dynamic


*Matrix*
  * col_vector
  * complex
  * matrix
  * row_vector

*MultiSys*
  * ExProcess
  * MultiAux
  * MultiExch
  * MultiHam
  * MultiHSLib
  * MultiIPul
  * MultiLib (partial)
  * MultiLOp
  * MultiSOp
  * MultiSys
  * MultiWBR
  * SpinMap

*Pulses* (Everything)
  * PulCHIRP
  * PulComposite
  * PulCycle
  * PulDANTE
  * PulGARP
  * PulGauss
  * PulMLEV
  * Pulse
  * PulSinc
  * PulSupCycle
  * PulTrain
  * PulTrainSCyc
  * PulWALTZ
  * PulWaveform


*Solids*
  * No Files Swigged