
# The Vespa Appliance (Virtual Machine)

We provide a [virtual machine](http://en.wikipedia.org/wiki/Virtual_machine)
appliance preloaded with Vespa. If you have virtualization software (like 
[VirtualBox](https://www.virtualbox.org/), 
[VMWare](http://www.vmware.com/products/player/),
or [Parallels](http://www.parallels.com/)), the Vespa appliance allows you to 
try Vespa without installing all of Vespa's dependencies. 

```
#!div style="width: 66%; border: 1px dashed #2B73D7; background-color: #ffd; text-align: center; padding: .5em; margin-left: auto; margin-right: auto;"

[//appliance/VespaAppliance.ova Download the Vespa appliance]

Note that the appliance is a very large file and will take some time to download.
```


You can use the appliance for as long as you like, but if you like Vespa we
recommend you install it directly on your computer. Vespa runs faster on 
real hardware.

## Using the Appliance
First, you need virtualization software if you don't already have that 
installed. We use [VirtualBox](https://www.virtualbox.org/) which is free and
open source.

Once you have virtualization software installed, 
[//appliance/VespaAppliance.ova download the appliance].
Next, follow your virtualization software's 
instructions for importing an appliance. 

For instance, under VirtualBox, select File/Import Appliance... from the menu
and follow the prompts. You shouldn't need to change any values from their
defaults.

## Copying Files onto the Appliance
There are four ways to get your data onto the appliance.

1. Put your data files somewhere on the Web and then download them using the Web browser installed in the appliance.
1. Email the files to yourself and use the Web browser installed in the appliance to read that mail and download the attachments.
1. Share your host's file system with the appliance. See the documentation for your virtualization software for instructions on how to do this.
1. Enable USB support. See the documentation for your virtualization software for instructions on how to do this.



