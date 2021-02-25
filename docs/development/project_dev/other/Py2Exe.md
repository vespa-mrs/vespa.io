# py2exe
py2exe is an open source package that allows one to bundle a Python interpreter, a Python application and its related modules into a single EXE that users can download and run under Windows without any fuss. It's (original?) author and lead developer is Thomas Heller. He seems like a nice guy. Other folks contribute occasionally, but it's pretty much a one-man show.


I've been experimenting with packaging Analysis with py2xe. For the time being, I'm going to stop working with py2exe and try alternatives like PyInstaller, bbfreeze, cx_freeze and perhaps Portable Python. The setup.py that I used for this experiment is attached to this page. 

Here's the results of my py2exe experiments so far.


## p2exe in our environment
At first glance, py2exe looks like the perfect solution for making a one-click, downloadable EXE for Windows users. To some extent, it fits this description. It's popular and works well for simple apps. It does not, however, work so well for us.

One problem is that py2exe has trouble with packages that do tricky things with imports and namespaces. Many non-trivial packages do this, and all of the 3rd party packages that we use are non-trivial.

It's difficult to assess the impact of this weakness of py2exe without testing individual packages, but this gives me a sense that the process of building an EXE using py2exe will always be fragile.

## py2exe and SciPy - An Example
Here's an example of a py2exe problem that I found while running py2exe on Analysis.

The SciPy function `factorial()` is implemented in `scipy.misc.common.py`, yet one imports it as `scipy.factorial` thanks to tricks that scipy does under the covers. This works fine in normal Python but under py2exe produces "`ImportError: cannot import name factorial`". 

Py2exe's author/lead developer [acknowledged this problem and recommended only to ask for a solution on the scipy list](http://sourceforge.net/mailarchive/forum.php?thread_name=gsspc2%24u8d%241%40ger.gmane.org&forum_name=py2exe-users). 

The OP didn't ask on the SciPy list, but someone else did and got no reply:
http://mail.scipy.org/pipermail/scipy-user/2009-May/021216.html

It's hard to argue that py2exe is broken in this case; it has never promised to be able to mimic import voodoo. That's out of its scope. Nevertheless, the only possible workarounds for the OP and for us are to "fix" scipy or "fix" py2exe.

The SciPy folks aren't tripping over themselves to fix this problem, and who can blame them? It's a credit to py2exe's influence that at least one large package has provided a py2exe-specific modification (matplotlib added the function `get_py2exe_datafiles()`). My guess is that the change required of SciPy to resolve the `factorial()` problem would be a lot more complicated than matplotlib's change.

As far contributing to py2exe, I'd love to help. But if the author/lead developer doesn't see a fix offhand, then I think it would take me a lot of time to understand and resolve the problem, if that's even possible.


## Some Other Drawbacks
py2exe has no support for Python 3.x. 

The last release of py2exe was about a year ago (Nov 2008), and there haven't been many commits since then. Thomas Heller has [acknowledged that he doesn't have as much time as he'd like to put into py2exe](http://sourceforge.net/mailarchive/forum.php?thread_name=49F870CB.3000304%40arimaz.com&forum_name=py2exe-users). The project seems in danger of stagnating if it hasn't already. I don't mean to bury py2exe, but popular packages do occasionally stagnate, wither away and die. It would be unfortunate for us to build a dependency on a project that was headed for that fate. 






