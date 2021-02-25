# Vespa GUI Development
This document describes how we develop Vespa's GUI -- both the visual elements
and the code behind them. After reading it, you should have an idea of how to
edit the existing GUI and how to add new dialogs, tabs and windows yourself.

It is _not_ a tutorial on wxGlade itself. It's a tutorial on the process by
which we use wxGlade.

## Defining the GUI: wxGlade
We build all of our GUIs in wxGlade. It's not perfect, but it works well 
enough for us.

As I said above, this document isn't a tutorial on wxGlade. However, I will call
your attention to a few key aspects of it. For this document, I'll
use `vespa/common/wxglade/experiment_browser.wxg` as an example. 

wxGlade works by allowing you to define a GUI by positioning elements on a
canvas (typically a dialog or window), and then generating Python code that 
calls wx to construct the GUI you defined. The Python code isn't generated 
until you explicitly request it.

When one opens `experiment_browser.wxg` or any Vespa `.wxg` file, the 
application properties window shows two important settings and one important
button. 

[[Image(screenshot.png)]]

The "Overwrite existing sources" and "Output path" affect the behavior of
the "Generate code" button. 

The output path is the name of the file to which wxGlade will write when one
clicks "Generate code". 

In Vespa, "Output path" always starts with `../auto_gui/`. The name "auto_gui"
is short for "_auto_matically generated _GUI_ files". Vespa needs these
files at runtime, but we Vespa developers almost never look at them. Grouping 
them in their own directory keeps them from cluttering up directories we use 
on a regular basis. The name we choose for the automatically generated file 
is arbitrary, but is usually quite similar to the  name
of the `.wxg` file.

*Windows users, please be sure to use forward slashes as path separators*  (as in
the example above) in the output path. The backslash that Windows typically uses
as a  path separator will be interpreted as an escape character on non-Windows
machines. 

*"Overwrite existing sources" should always be checked.* This option 
controls whether or not "Generate code" will overwrite the filename in "Output 
path" if that file already exists. If it's not 
checked and you click "Generate code", wxGlade will tell you that 
"Code generation completed successfully" but it won't tell you that the 
generated code went into the bit bucket. 


## Using the GUI
Once wxGlade has generated code, how does one use that code? We follow a model
that works very well for us. 
*It's important to understand our model because every single bit of our GUI uses it*.

The code
that wxGlade generates contains a class (e.g. MyDialog -- we often use the
generic default name because the name is unimportant). Our implementation is 
a subclass that resides in a file entirely 
separate from the `auto_gui` file and up one level in the directory hierarchy.
We instantiate our subclass to create the window or dialog we want.

For instance, 
[browser:/trunk/common/wxglade/experiment_browser.wxg vespa/common/wxglade/experiment_browser.wxg]
generates the file
[browser:/trunk/common/auto_gui/experiment_browser.py vespa/common/auto_gui/experiment_browser.py]. 
The latter file contains the
class `MyDialog`. (There's that lazy default name.) Our implementation of this
dialog (i.e. all the interesting code) resides in
[browser:/trunk/common/dialog_experiment_browser.py vespa/common/dialog_experiment_browser.py] 
in a class called `DialogExperimentBrowser` which has 
`auto_gui.experiment_browser.MyDialog` as its base class.

Here's an abbreviated snippet of the relevant code:


```
#!python
# Python modules
from __future__ import division

# 3rd party modules
import wx

# Our modules
import vespa.common.auto_gui.experiment_browser as gui_experiment_browser


class DialogExperimentBrowser(gui_experiment_browser.MyDialog):
    def __init__(self, parent, db):
        if not parent:
            parent = wx.GetApp().GetTopWindow()

        gui_experiment_browser.MyDialog.__init__(self, parent)

    def on_list_click(self, event):
        # Handle click event
        index = self.ListExperiments.GetSelection()
        # etc.

```


## The Placeholder Convention
There are some controls that wxGlade doesn't know about 
(e.g. `wx.html.HtmlWindow`). When we need to use one of these controls, we
instead create a placeholder control (often with "placeholder" explicitly in 
the name) so that it's easy to see in wxGlade what will appear there at runtime.
Then, during the `__init__()` of the window or dialog, we replace the 
placeholder with what we need.

We use this technique twice in `DialogExperimentBrowser`. Here we replace 
a placeholder called `LabelHtml` with a `wx.html.HtmlWindow` control:

```
#!python
html_sizer = self.LabelHtml.GetContainingSizer()
parent = self.LabelHtml.GetParent()
self.LabelHtml.Destroy()

self.html_ctrl = wx.html.HtmlWindow(parent)

html_sizer.Add(self.html_ctrl, 1, wx.EXPAND|wx.ALIGN_TOP)
```

Just below that code, we replace `LabelOpenCancelPlaceholder` with OK and 
Cancel buttons. This is something we do in so many places that I wrote
a utility function for it.

```
#!python

# We add the Open & Cancel buttons dynamically so that they're in the 
# right order under OS X, GTK, Windows, etc.
self.ButtonOpen, self.ButtonCancel = \
    wx_util.add_ok_cancel(self, self.LabelOpenCancelPlaceholder,
                          self.on_open, ok_text="Open")
```



