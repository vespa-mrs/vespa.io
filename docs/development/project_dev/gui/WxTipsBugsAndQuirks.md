# Miscellaneous wx-Related Tips, Bugs and Quirks
## Printing The VersionTo print your wx version, execute this at the command line:
```
python -c "import wx; print wx.version()"
```

## The Inspector
The Widget Inspection Tool is an extremely useful tool for debugging. To turn it on, add this to your Python code:

```
#!python
import wx.lib.inspection
wx.lib.inspection.InspectionTool().Show()
```

Sometimes when I place this code inline, I get a strange runtime error on the first line of code that references wx:

```
UnboundLocalError: local variable 'wx' referenced before assignment
```

I think wx is doing something funny under the covers. For me, moving the `import wx.lib.inspection` statement to the top of the file just after `import wx` is sufficient to solve the problem.

## Floatspins Throughout wx History
The floatspin control was first introduced in wxPython 2.8.9, I think, but it was buggy. The first version of wxPython that contained a floatspin with patches that we require was 2.8.11.0. In addition, the 2.8.11.0 version contained backwards-incompatible syntax changes. This means it's easy to support the floatspin in wx >= 2.8.11.0, but not if we want to support older versions of wxPython too. The solution for us is to use the wxPython floatspin when the wx version is high enough and fall back on a custom version of the control when it's not.


## Spin Controls, Enter, and OS XUnder OS X, a spin control can't capture the EVT_TEXT_ENTER event. The problem is that on the Mac, there's 
no native spin control, so wx fakes one with a text control and a spin button placed side by side. When the
text control is created, it is not passed the wx.TE_PROCESS_ENTER flag which is required to make it capture
enter. You can see this for yourself with the following code:

```
for kid in your_spin_control.GetChildren()
    if isinstance(kid, wx._controls.TextCtrl):
        print (kid.GetWindowStyle() & wx.TE_PROCESS_ENTER)
```

## Spin Controls and OS X Size IssuesFor some reason (probably related to the lack of a native spin control under OS X), one must call SetMinSize() on a spin control before calling SetSize() for the latter to have any effect. This is not the case under Windows or Linux. 

## Spin Controls, SP_ARROW_KEYS, TE_AUTO_URL, SP_WRAP and TE_NOHIDESEL
When using a spin control in wxWidgets, it's impossible to set SP_ARROW_KEYS independently of TE_AUTO_URL. Ditto for SP_WRAP and TE_NOHIDESEL. The problem is that the former are both 4096 (0x1000) while the latter are both 8192 (0x2000). When a textbox and spin button are combined into one control, the constants overlap. 

I filed this ticket against wxWidgets to track this: http://trac.wxwidgets.org/ticket/11461

## `wx.RESIZE_BORDER is the same as wx.THICK_FRAME`
`wx.RESIZE_BORDER` and `wx.THICK_FRAME` both have values of 64, so it's impossible to set one without setting the other. 

## Floatspin Controls and Enter
The floatspin control in the wxPython library doesn't trap enter. I submitted a patch for this problem and it was accepted as r62685: http://trac.wxwidgets.org/changeset/62685/wxPython/3rdParty/AGW/agw/floatspin.py

This is already integrated in our custom version of the floatspin control.

## wxWidgets under KDE
Under KDE, wxWidgets uses GTK to draw its widgets, so there's no KDE-specific version of wx. AFAICT that's mostly because KDE uses QT as its windowing toolkit, and QT is a competitor to wxWidgets. As a result, there may be licensing problems if wx was to wrap QT's widget set. Thus there is not and probably never will be a KDE version of wx.


## Floatspin Controls, Size and MinSize
Floatspin controls require some care to size properly. Here's some things to
be aware of.

 * By default, most (all?) newly-created controls in wxGlade start with a 
   proportion of 0. Floatspins, however, start with a proportion of 1. If you
   don't change that to 0, they'll expand to fill their sizer even if you have
   wxEXPAND turned off.
  
 Since this means floatspins work differently than most controls, I might
 report it as a bug.
  
 * The size passed to a wx control in the constructor also becomes the 
   control's minimum size. This is strange to me, but apparently it's by  
   design, so there must be a good reason for it. 
  
 Good reason or no, this affects us directly. The code that wxGlade 
 generates never sets the size in the constructor even if you specify a size
 for the control in design mode. (It creates the control and sets the size 
 later, if necessary.)  The floatspin control, therefore, uses the default 
 width of 95 which is hardcoded in the constructor. This combined with 
 wxWidget's min size quirk means that '''floatspins created by wxGlade always
 start with a min width of 95'''.
  
 Therefore, if you want your floatspins to be able to be smaller than 95
 pixels wide, you need to call SetMinSize() before calling SetSize(). e.g.
  
```
#!python
self.spinThingy.SetMinSize( (60, -1) )
self.spinThingy.SetSize( (60, -1) )
```
  
  
