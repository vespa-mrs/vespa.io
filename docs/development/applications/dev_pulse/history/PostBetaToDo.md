# Post Beta To Do Items for Pulse
  * Finish Root Reflection transform
  * Implement additional transformations at UI, DB, and at math and logic level. Probably will still need to do Optimal Control and Root Reflection. Jerry's suggested order for other transformations: 
    - REMAPPING
    - OPTIMAL_CONTROL
  * then...
    - SAMPLE_EFFECTS
    - PULSE_CONCATENATION
  * Note: When implementing 'concatenate pulses': copy over the "imported" pulses, and FREEZE them, and keep for provenance.
  * Continue to Update Pulse wiki to be more USER friendly (see Simulation wiki).
  * Add more science tests (regression tests).
  * Add more unit tests (decide on a unit testing framework).
  * Implement the Import or 3rd party pulses from Varian, Siemens, and Matpulse. See notes on [3rd party Importation](/wiki:NotesOn3rdPartyImport/).
  * Finish coding for other Bandwidth_Conventions.
  * Add new algorithm to rescaling, i.e. maximum phase shift from average (see note in resacale.py). Also, return flag as to what kind of rotation was performed (total or net).
  * Talk to Jerry about how to calculate corrections (fudges) in min_max_setup.py dynamically and not statically (and implement).
  * Implement dwell_time on interpolation page, and allow users to reduce number of points.
  * Reconsider if we want to allow a user to recover a saved (to db) set to machine settings after repopulating from a new template. e.g. Siemens (saved), etc., and hitting run, but before saving.
  * Add import/export of results to these formats: e.g. Bruker, Philips, GE.
  * Save UI settings, for plotting, for each tab in every pulse project (perhaps to the database).

  * (BJS) Write wiki doc on use of Transformation Base class
  * (DCT) Add scientific integrity (fidelity) tests to pulse_funcs code.
  * (KY)  See if possible to make interpolation work within root reflection.
  * (KY)  Write wiki doc on use of Pulse_functs as generic python code for use outside of Vespa

  * Have interpolation be more full-features. Allow users to specify # of points, fractional scaling factors, or new dwell_time.
  * Implement iterative solution of Hyperbolic-secant so get the exact bandwidth not an approximate bandwidth.



