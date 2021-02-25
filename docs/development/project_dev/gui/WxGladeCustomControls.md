# Custom Controls and wxGlade
wxGlade is capable of integrating custom controls. In this context, "custom"
means "anything that wxGlade doesn't know about by default". For instance, 
everything in the 
[wxPython Advanced Generic Widgets module](http://www.wxpython.org/docs/api/wx.lib.agw-module.html) 
is a custom control as far as wxGlade is concerned, despite the fact that 
it's a standard part of wxPython.

## For Vespa Developers
You'll need to tell wxGlade where our custom controls reside. Start wxGlade 
and open the preferences. On the "Other" tab, near the bottom you'll find
a textbox for "Local widget path". In that textbox, enter the path to the
`widgets` directory under `vespa/common/wx_gravy`, e.g. 
`/home/me/w/vespa/common/wx_gravy/widgets`.


## In General
wxGlade's documentation is pretty quiet on the subject of custom controls.
Fortunately, there's a decent tutorial which
helped me when I created the [common.wx_gravy](/wiki:WxCommon/) library. 
That tutorial is attached to this page; there might be an updated version
[at the original author's site](http://sites.google.com/site/lvmarcoux/Home/wxglade). 

I could not have created our `vespa.common.wx_gravy` library without the additional help of 
[Kevin Dahlhausen's blog posting](http://powertwenty.com/kpd/blog/index.php/python/adding-custom-widgets-to-wxglade)
which, luckily for us, was about using the floatspin control as a custom
control. Note that the code that Kevin offers is a little broken; I think
it worked with an older version of wxPython or wxGlade (note that the
blog posting is from 2006). The code in `vespa.common.wx_gravy` is very close to his
code, but I made some changes. I sent him my patches but as of this writing he hasn't
posted the patched code.

