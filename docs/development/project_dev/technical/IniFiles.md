# Vespa's INI Files
Vespa has four INI files that reside in the 
[VespaDataDirectory Vespa data directory]. There's one INI file for each
application and a fourth called `vespa.ini`.

Each INI file contains a comment at the top that gives an overview of the
entries in the INI file.

Vespa knows how to recreate an INI file _de novo_, so if your INI file has
become broken or you just want to return to factory settings, you can exit all
Vespa apps, delete one or more INI files, and then re-run the app.

## Debug Entries in `vespa.ini`
Developers might want to add a [debug] section to `vespa.ini`. At present,
that section can take four entries. We suggest that developers use these 
settings --

```
[debug]
hook_exceptions=False
numpy_error_response=raise
show_wx_inspector=yes
verbose_oc=yes
```

Note that INI file booleans can be "true", "false", "yes", "no", "on", "off", "1" or "0". Case doesn't matter.

*`hook_exceptions`* is a boolean. When True (the default), exceptions are
captured and displayed in a user-friendly "oops" dialog. When False,
exceptions are not captured. Most developers will want to set this to False.

*`show_wx_inspector`* is also a boolean. When True, Each Vespa app will add an item 
the bottom of the Help menu that allows you to launch the 
[wx window inspector](http://www.wxpython.org/docs/api/wx.lib.mixins.inspection.InspectionMixin-class.html).
This is off by default.

*`numpy_error_response`* defines how a subset of numpy errors are
reported, as described in
[numpy's `seterr()` function](http://docs.scipy.org/doc/numpy/reference/generated/numpy.seterr.html). Valid values for this INI file setting are "ignore", "print", "warn" and "raise". You can also leave it blank, in which case
numpy's default behavior (which is distribution-dependent) will not be
altered.

In my limited experience, under OS X numpy is set to `{'over': 'print', 'divide': 'print', 'invalid': 'print', 'under': 'ignore'}`. Under Windows & Ubuntu, this is set to `ignore` all the way through. This can (and probably does) vary per numpy distro, so don't assume too much.

*`verbose_oc`* is a boolean. It enables or disables printing of activity to the console when RFPulse's Optimal Control is running.



