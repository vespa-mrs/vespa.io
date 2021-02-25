# Import, Concatenate, Machine Settings, Gradients, etc
Q&A and discussion with Jerry Matson on 12/23/10 and 01/20/11.

### 1. Regarding "Import" (i.e. importing a pulse from an unrelated program into the RFPulse database), What do we need to specify other than the file name, location, and file type?
  * [Of course] the project name, investigator (creator), and comments.  
  * The location of both the pulse file, and the gradient file (if there is one).
  * Machine settings and Master parameters - assuming this information is not in the pulse file.
  * We should be able to import: Bruker, Varian, Philips, GE, Siemens, and of course Matpulse. 
  * For the beta we should focus on Matpulse, Siemens, and Varian.  To look at templates for these, Jerry's Matpulse already has an import feature for Varian pulses (but he indicated that it was not complete) and an export feature for Siemens pulses.

### 2. In the "Concatenate" process (i.e. concatenating two pulses from the RFPulse database into one new pulse), what can we specify as variables, and what are the constraints?
#### Variables  * Relative timing
  * The order in which the pulses should be placed
  * And relative amplitude.

#### Constraints  * Then need to have the same dwell time increment.
  * The other machine-settings do not have to be the same, but we need to specify what machine we are targeting and it's settings (of course).
  * We need to keep the timing of the gradients in sync with the pulses.

*Dealing with the gradient amplitude vs the pulse amplitude?*
This is a topic that needs to be researched further. Jerry has some facilities to change the range of a pulses selectivity when concatenating two pulses - which impacts the intensity of the gradient. However we might want to limit that in earlier versions of RFPulse so a user would have to edit and save (or clone, edit, save) a pulse before concatenating to get this effect.

### 3. How should we handle Machine Settings...
  * _i.e. Are the specifications on machines with the same manufacturer, model and field strength likely to be exactly the same, or will they vary too much from site to site?_
  * _Should they be exported as a separate entity with their own uuid?_
  * _Should they be part of a pulse project, or exist as separate entity that are referenced by a pulse project?_

It turns out that the specifics - at least for machines in the research field - are too varied to think of them as likely to be the same for a given manufacturer and a given field strength.  There are too many variables: Custom heads, inconsistent application of software upgrades, custom tweeks, inconsistent application of upgrades in models, etc.

It's best to think of the machine settings as something that will vary from one institution to another even for a given model number and manufacturer.

The implication of this is that we should have the Machine Settings be part of a pulse project - at least when they are exported - and machine settings should not be exported with their own uuid.

** However, the issue on whether there should be a separate management window, and whether these will be reused within an individual clients workspace is still up for consideration and debate, as a single user is very likely to reuse the exact same machine settings for a large number of calculations!*

### 4. Should gradients be exported with the RFPulse (time domain profile)
Yes. Usually they are exported as two separate files, but at the same time.
And if there is a frequency profile (i.e. a frequency modulation of the carrier wave) that should also be a separate file on export.
