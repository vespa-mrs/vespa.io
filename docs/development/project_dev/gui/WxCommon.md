# The `vespa.common.wx_gravy` Library
vespa.common.gravy is a library that, as of this writing, contains some
utilities and two custom controls
for use in Analysis. "Custom" control is a bit of a misnomer as only one
of them is really custom. They are the `floatspin` control and the 
`floatspin_multiplier` control. They're explained below.

## `floatspin`
The 
[floatspin control](http://www.wxpython.org/docs/api/wx.lib.agw.floatspin-module.html) resembles 
a standard spin control, but it accepts
floating point input. (The standard control accepts only integer input.)
It was added to wxPython in version 2.8.9.2 along with the rest of 
`wx.lib.agw`; it is not in 2.8.9.1 or any earlier versions. However,
that version contained some bugs. We submitted patches 
(wxPython revs [62685](http://trac.wxwidgets.org/changeset/62685) and 
[62920](http://trac.wxwidgets.org/changeset/62920)). Our patched
version appeared in wxPython 2.8.11.0.

Since we only require wxPython 2.8.8.0, we can't rely on any version of 
floatpsin being available from the wxPython library, let alone the patched
version.

## `floatspin_multiplier`
This control subclass `floatspin` and is therefore mostly the same, but it 
de/increments the
value by a percentage of the value rather than by a consistent increment. 
It has one additional attribute called `multiplier` which defaults to 1. 
When set to e.g. 1.25, the control will de/increment its value in jumps
of 25%.




