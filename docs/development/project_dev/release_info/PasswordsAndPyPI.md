# Passwords, PyPI Uploads, `twine`, and `.pypirc`
This document describes some pitfalls of interacting with PyPI.

## Caveat
`setuptools` is a 3rd party enhancement of the Python standard library's
`distutils`. It's hard for me to tell where on begins and the other ends,
especially because `setuptools` often operates by subclassing `distutils`
features. Some of the blame below aimed at `setuptools` might more
properly be directed at `distutils`.

## Uploading with `setuptools`
Uploading wheels to PyPI is a little awkward. The obvious way to
do it is with this `setuptools` command --
```
python setup.py bdist_wheel upload
```

There's already a shortcoming there, which is that one must create
the wheel and upload it in the same step. There's no way to
create the wheel, test it, and _then_ upload it. That's just a
quibble, though, since one can just create the wheel, test it, and
then re-create it for the upload step. It's annoying if your wheel
takes a long time to build. Fortunately, none of ours do.

## `setuptools`, Uploads and Passwords
Another annoyance is that `setuptools` relies on `~/.pypirc`
for authentication information, and
it's a bit stupid about it.

If there's no authentication info present, it
tries to upload your wheel without authentication, resulting in this:
```
Upload failed (401): You must be identified to edit package information
```

If there's partial authentication info present (say, a username without a
password, which would be a convenient setup), rather than prompting you for a password,
`setuptools` just passes the password `None` to `distutils` which then fails
with this --

```
File "/Users/vespa/miniconda2/lib/python2.7/distutils/command/upload.py", line 135, in upload_file
    self.password)
TypeError: cannot concatenate 'str' and 'NoneType' objects
```

This is an easy problem to fix -- just add the username and password
to `~/.pypirc`. Now you have a much bigger problem, which is that your password
is stored in cleartext on your hard drive.

## `setuptools`, Package Registration and Passwords
For some reason, `setuptools` is smarter when running this command --
```
python setup.py register
```

If your password isn't in `.pypirc`, it prompts you for it. Go figger.

## Real Solution !#1 - `keyring`
[KeyRing](https://pypi.python.org/pypi/keyring) is a Python package that
interacts with the OS keychain (Windows Credential Vault, Mac Keychain, etc.).
This allows you to store your passwords securely and still access them with
Python.

`setuptools` can use `keyring` if it's available. I haven't figured out
how to set it up yet, though.

## Real Solution !#2 - `twine`
[Twine](https://pypi.python.org/pypi/twine) is a Python package that does
one thing -- upload stuff to PyPI. It allows you to upload your wheels
independently of creating them, which is nice.

More importantly, it is smart enough to prompt you for a username/password
if there isn't one present in `.pypirc`.

Unfortunately, `twine` doesn't use `keyring`, so you have to manually
enter your username/password when prompted.



