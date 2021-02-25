# About Upgrading Vespa from 32- to 64-Bit
This is background information for users upgrading an existing install of
32-bit Vespa (versions < 0.9.1) to 64-bit Vespa (versions > 0.9.1). It tells you
some things you might like to know before you upgrade.

## What Changes
Moving to 64-bit Vespa is similar to installing Vespa for the very first time,
but with two important differences. First,
*all of your Vespa data will be preserved*.
Second, it's easier to install Vespa than it used to be.

In actual day-to-day usage, you probably won't notice a difference between
32- and 64-bit Vespa. We're moving Vespa to 64-bit because that's where
the Python world is headed, and we don't want Vespa to be left behind.

## What Happens to Your Saved Vespa Data (Experiments, etc.)
All of your data will be present when you run 64-bit Vespa. You don't need
to do anything special.

## What to Clean Up
Once you have installed 64-bit Python and Vespa,
feel free to uninstall 32-bit Python if you're not using it for anything else.

If you're unsure whether or not you're using your 32-bit Python, you can
leave it alone. There's no harm to having a Python
installed that you're not using, other than a little wasted disk space.
