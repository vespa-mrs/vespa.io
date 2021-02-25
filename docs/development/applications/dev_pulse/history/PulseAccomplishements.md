# Items Completed
BJS - left this in place for Historical reference

### 04/01/11 to 05/09/11
Targeted for these two milestones: Alpha Test then Beta Release

Items for Alpha Testing

  * (BJS) DONE - _VERIFY WITH DAVID, Better y-axis labeling re. Mz, Mx, Mxy (last only if REAL+IMAG plotted)._
  * (BJS) DONE - _reported some science bugs, Hook up sciency bits to the Root Reflect Tab GUI_
  * (BJS) DONE - _Finish GUI bits for Hyperbolic-Secant and Root Reflection (including pop-up warning of > 64 points)._
  * (BJS) DONE - _Needs work ... Add a User Manual version into docs_ 
  * (BJS) DONE - _Philip done it, actually, Design and implement View dialog for PulseProjects from Manage dialog_
  * (BJS) DONE - _Reinstate Help menu item for PDF user manual once the user manual exists_

  * (DCT) _Convert interpolate and rescale to python and implement._ - DONE
  * (DCT) _Finish design of rfpulse_project object (Just need Root reflection)_ - DONE
  * (DCT) _Design and implementation of Database for the above objects (Still need root reflection)_ - DONE
  * (DCT) _Remove global variables, referenced in pulse_func calls for SLR, etc, and clean up code in all the slr related routines._ - DONE
  * (DCT) Review SLR "FIXME"s with Jerry and see if any changes needed for Beta. 
    * (DCT) _Review how timepoints are handled in matlab vs rfpulse vs how they should be handled._ - DONE
    * (DCT) _Make this work (or raise an error) with an even number of points_ - DONE
  * (DCT) _Check and fix dwell/duration on HS tab._ - DONE
  * (DCT) _Check error messages (eg. duration of 300)_ - DONE

  * (KY) (DONE - Needs testing) _Export to Siemens (and Matpulse) file format._
  * (KY) DONE - _See how to implement weightings on firls() routine or disable least squares for beta._
  * (KY) (DONE - Needs editing) _Fill in Appendix B for each transform a description of how the transform and its parameters act._

  * (PS) _Fix any Import/Export and inflate/deflate issues due to recent DB changes._ - DONE
  * (PS) _Make UI, objects, and database be read-only when a pulse project is public_ - DONE
  * (PS) _When Saving: Implement deflate to dictionary for all objects. Add the last_saved to pulse_project. Then implement saving by first seeing if anything in the UI has changed, pop up a dialog if anything has (See get_cooked_gui_data and get_raw_gui_data)_ - DONE
  * (PS) _Fix machine-settings on basic info. page: How it works and adding new field to db._ - DONE
  * (PS) _Put up a error dialog (when the user hits run) if a user puts in an angle that is not 180, 90, or 0 to 30, for the create_slr transformation._ - DONE

  * (Philip and David) _Determine if major changes to RFPulse standalone DB are finished. Consider schedule for merging with Vespa DB_ - DONE

Items specifically for the Beta Release

  * (BJS) DONE - _Change plotting of profiles to use step graph, instead of point-to-point to emulate MR machines._
  * (BJS) DONE - needs pass 3 _Pass 2 on User Manual_
  
  * (BJS and Others) DONE - _Decide how to work Main wiki with underlying RFPulse and Simulation wiki architectures._
  * (BJS and Others) DONE - _Implement wiki redesign._
  * (DCT) (DONE - Needs 2nd edit) _Build an RFPulse version of Appendix A in documentation - describe how params, results, etc. all fit together under the hood._

  * (KY) Edit Appendix B in User Manual, fill in text describing the 'algorithm' for each transform. - DONE

  * (PS) _Pre-populate database with 2 (or more) examples of pulse projects._ - DONE
  * (PS) _Ensure uniqueness on name of pulse_projects_ - DONE
  * (PS) Integration of db code and db with main program.
    - _Move code from local misc.py to common.misc.py or rename, etc._ - DONE
    - _Move menu code to util_menu.py_ - DONE
    - _Alphabetize functions, especially in db.py_ - DONE
    - _Integrate rfpulse.sqlite with vespa.sqlite_ - DONE
  * (PS) Test integrated db for Open/Save, Import/Export. - DONE


### 02/17/11 to 03/31/11
  * (BJS) Add new TransformationBase object (that inherits from auto_gui/transformation_base) from which tab objects inherit; give clearer descriptions to names of checkboxes in transformation.py & change the write up on this.
  * (BJS) Add a subobject of TransformationBase, called CreatePulseBase (or a similar name)
  * (BJS) Put into lower tabs an "x" button to remove that tab, and a pop up control to warn users that this will force an update.
  * (BJS) Allow users to plot real and imaginary components with separate colors (e.g. for Spin Echo).
  * (BJS) Make changes to UI for root reflection based on feedback from Karl and David.
  * (BJS) Implement items in View (Plot Options) menu.
  * (BJS) Add check/warning if time_steps > 1/4 of calc_resolution.

  * (DCT) Removed amplitude_factor from db. Converted interpolation_factor to an integer.
  * (DCT) Describe what needs to be plotted for all the check boxes at bottom of transformation page.
  * (DCT) Return the x,y, and z values from bloch equations, not limited results that we now have. (Actually obtained the 4 possible raw results that we would need to calculate any of the 16 possible results based on the UI selections.)
  * (DCT) Change Bloch results into a lazily evaluated function or parameter. Delete Bloch results when update waveform. (Actually implemented this as stated in stated in the previous 'todo' item, using a function, but without lazy evaluation. Bloch results are regenerated at the same time as the rf waveform is changed, so that should take care of the second issue
  * (DCT) Implement delete transform (tab) functionality.
  * (DCT) Implement update all (downstream) calculations.
  * (DCT) Wire up calculation code for the "Analytic" pulse type, Hyperbolic-Secant.
  * (DCT) Compare my current Filter to Jerry's new filter.
  * (DCT) Implement clone functionality (clone in db) in manage pulse projects.
  * (DCT) Improve consistency issue on Machine Settings.
  * (DCT) See if possible to speed up Bloch routines in RFPulse.

  * (PS) Also pre-populate with a generic machine settings (or a Siemens, etc).
  * (PS) Add inflate/deflate to XML for all objects.
  * (PS) Implement export and import of pulse projects from XML.
  * (PS) Set up help menus with standard entries, from Simulation.

  * (KY) Convert Matpulse code for root reflection to python



### 12/06/10 to 02/16/11
  * Implement Bloch equations for calculating profile.
  * Fix issue with regenerating frequency profiles.
  * Dwell time issue, fix.
  * Fix auto_gui_object's so that when you click on the ".py" it starts up a test program (inherit from dialog, frame?).
  * Rethink flow on first transformation: put Concatenate, import on main menu or on list of transformations? Consider putting a submenu on New with these options (SLR, Hyperbolic-Secant, Gaussian, Sinc-Gaussian).
  * Implemented db routines for ifr transformation.
  * Add in Delete routines for all objects.
  * Implement "Update" in db.py for all rfpulse project items.
  * Implement a separate table for templated machine settings. Added db routines for reading, writing and searching.
  * "fix" Tools menu: Put actual transforms directly under Tools (rename IFR to "Interpolate, Filter, ReScale" in menu.
  * Review (and remove) plot routines in PulseProject.
  * Thin out the number of objects in mrs_transformation.py
  * Add plotting to IFR transformation.
  * Add insert/fetching/ 
  * Build a copy-tab (or clone) function (a la Simulation): e.g. cloned_project = copy.deep_copy(rfpulse_project); change uuid; notebook.add_project(cloned_project)
  * Consider whether we need to revise the technique used to store waveforms, and other array objects in the database. (Decision: Since only storing the time domain waveform (under 1000 pts) can keep it as is: i.e. storing each point as a row in the db, and specifying datatypes, etc. No need under these conditions to go to using a data blob.)
  * Propagate "get_type_for_value()" method to other enumeration objects.
  * Removed rfpulses table from db.
  * Simplified pulse project so it has only one ID. It is called ID, but contains the value that was in UUID.
  * Fixed IFR in db: I.e. changed name and composition of IFSR to IFR.
  * Decide on how to display plots (fixed size, variable size, etc). [Decision is to allow them to be variable size, and put them in the oder in which they are listed in the check boxes - for all that are checked].


### As of 12/06/10
  * Translated matpulse code (written in matlab) for SLR pulse generation into python to test the feasibility of project and to make sure there were no major show stoppers.
  * Planned the overall flow of the program in terms of transformations that are saved to database (db) for provenance, with each transformation having a set of parameters and results (rfpulse, waveform and gradient). The output result of one transformation is the input of the next transformation. Have Jerry Matson's sign-off on this overarching design.
  * DB layout using a web based tool (http://ondras.zarovi.cz/sql/demo/).
  * Creation of the actual database, including pulse projects, machine settings, and two transformations: The creation of pulses, and IFR (interpolation, filtering and Rescaling).
  * Built the initial user interface (UI) for a set of pulse_projects - each one having a set of transformations; the basic transformation user-interface object from which all other transformations will inherit (subclass); and the panels for pulse creation and IFR.
  * Wrote the database code for inserting and fetching pulse projects and the SLR Transformation (CREATE_SLR). 
  * Came up with an interesting way to deal with [wiki:RFPulseEnumerations that keeps all the db and UI information in one place.
