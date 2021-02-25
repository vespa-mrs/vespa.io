# The Vespa Exception Hook
When an unhandled exception occurs in Python, Python calls an exception 
handler. Most apps use Python's default exception handler (which prints
the exception to stderr and ends the process) but Python allows one to
override the standard exception handler. 

For technical details on how this works, see the Python standard library
documentation for `sys.excepthook` and `sys.__excepthook__`. This document
assumes you already understand those details.

Each Vespa app sets a custom exception hook early in its initialization.
All applications use the same exception hook. As of this writing, our hook is
defined 
in [browser:/trunk/common/exception_handler.py common.exception_handler.py].
It does three things --

1. Calls Python's standard exception handler to print the error to stderr.
1. Logs the traceback to a file.
1. Displays a dialog to the user containing the traceback and some info
 useful for debugging (info about the machine, Python version, etc.). The
 dialog encourages the user to email the info to us and makes it as easy 
 as possible to do so.
 
## The Exception Dialog
We really want to encourage users to send us error reports, so we remove
as many barriers to that as possible. Ideally the user would just click
"Send Error Report", but we weren't able to make things quite that simple.

My original version of the dialog invoked the user's local email client and
started a new email, but David pointed out that some people user Webmail
exclusively and thus don't _have_ a dedicated local email client. So the
dialog has to faciliate copying and pasting into an email.

Also, even if the user has local email client, there's limits to what one 
can do when invoking it programmatically. Without getting into 
platform-specific scripting (e.g. Applescript), we're limited to what we can
stuff into a `mailto:` URL that we pass to Python's `webbrowser.open()`.
One can embed subject, to and even body text in a `mailto:` URL, but one 
can't specify a file to attach. Furthermore, encoding ~32k characters
(the size of a typical bug report) into a URL and expecting it to open 
correctly in a mail client seems doomed to fail sooner or later. So we
ask users to paste it in manually.


## Disabling the Exception Handler
The exception handler is on by default. You can turn it off 
by adding this to vespa.ini which is in the VespaDataDirectory --

```
[debug]
hook_exceptions=no
```


## The Exception Handler and IDEs
If you're using an IDE, you might want to disable the exception handler.

Brian has reported to me that Vespa's exception handler doesn't play nice 
with Eclipse-Pydev. I suspect that app tries to set its own exception 
handler and Vespa's clashes with it. My guess is that other IDEs would 
exhibit similar behavior. 

