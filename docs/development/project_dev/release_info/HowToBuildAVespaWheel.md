# How To Build a Vespa Wheel
This explains how to build `pip`-installable wheels for Vespa.

## How To Build the Wheel
1. Start a command prompt and change to directory that contains `setup.py`.
1. Remove any build caches from previous wheel building --
```
 python setup.py clean --all
```
1. Build the wheel --
```
 python setup.py bdist_wheel --python-tag py27
```

That's it! Your wheel will be in the `dist` directory.

To upload the wheel, use the guide for uploading PyGamma wheels. The process is the same for Vespa and PyGamma (and HLSVDPRO): [gamma:PyGammaHowToUploadWheels]

## About `setup.py`
Prior to version 0.9.1, Vespa's `setup.py` had a number of features and
responsibilities. As of 0.9.1, it's much smaller and does very little.

In fact, `setup.py` isn't even distributed with Vespa. Users are instructed to
install Vespa from a wheel file via `pip` (which basically just unzips the
Vespa wheel), so `setup.py` couldn't influence
the installation process even if we wanted it to.

It's possible to do a local (developer) install with `python setup.py install`,
although offhand I can't think of a reason for doing so. The only reason
you need `setup.py` is to build wheels.

## `MANIFEST.IN` and `setuptools`
`MANIFEST.IN` defines which files get included in the wheel.
See [Python's doc on MANIFEST.IN](https://docs.python.org/2/distutils/sourcedist.html#specifying-the-files-to-distribute).

Vespa's `setup.py` uses `setuptools`, and we pass the `include_package_data`
to `setuptools.setup()` in `setup.py`. That tells it to read `MANIFEST.IN`
to know which files to include in the wheel.

## Dueling Vespas
If you're modifying `setup.py`, chances are that you're a Vespa developer and
you have a `vespa.pth` file in your `site-packages` directory. When you test
your Vespa wheel, you'll then have a `vespa` directory in
`site-packages` in addition to `vespa.pth`. When Python looks in site-packages
to resolve an `import vespa.something` statement, it will have two Vespas from
which to choose. I don't
know what Python's behavior is in this case and I suspect it's undefined.

The practical upshot is that you need to remove `site-packages/vespa.pth`
while you're working on `setup.py` and testing wheels.