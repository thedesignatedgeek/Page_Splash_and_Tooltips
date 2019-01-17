#Page, Splash Screen and Tooltips

[![Python](https://img.shields.io/badge/Python-3.x-green.svg)]()
[![Page](https://img.shields.io/badge/Page-4.19-green.svg)](https://sourceforge.net/projects/page/?source=directory)
[![Tkinter](https://img.shields.io/badge/Tkinter-%20-green.svg)]()

##Introduction

This project is a quick demonstration of using Splash Screens and Tooltips within a ***Page*** GUI Project.

The original Tooltip code is code that I found at # Found the original code at:
 http://code.activestate.com/recipes/576688-tooltip-for-tkinter/ and I modified it to be a bit more generic.  I've included all the python and .tcl files for you.
 
 The files that you need if you only want to have Tooltips in your project is the ***tooltip.py*** file.  

As I'm sure that you know that Page uses two files per screen (or form), so the file structure is as follows...
   Working_Directory-
  					|-- \graphics_folder
                                       |-- \Main.py
                                       |-- \Main.tcl
                                       |-- \Main_Support.py
                                       |-- \splash1.py
                                       |-- \splash1.tck
                                       |-- \splash1_support.py
                                       |-- \tooltip.py


##Installation

Put alll files into a single folder.  The 'graphics' folder is for the toolbar within the Main.py and Main_support.py file.  The tooltip.py file **MUST** be in the code folder.


##Breakdown of the code and project
This project was originally designed to be a very simple demo for use as part of a tutorial on Advance Page projects.  The breakdown is as follows...

###Main.*
This code set contails the three Page files.  This will be your entry point into the program.  Once the Main module starts, it hides itself and calls the splash1 code modules to display the splash sreen.  The splash screen is shown, centered in the monitor for a specified number of milliseconds (5 seconds in the demo), then re-opens the Main form and sets the tooltips text for each widget that is desired.  The function ***setup_tooltips()*** in Main_support.py shows how to easily setup the tooltips on a widget per widget basis.  I have included the ***Page*** .tcl file for your use.

###splash1.*
Once Main.* calls this code module, it uses the Tkinter trick
 root.overridedirect(True)
which turns off all decorations (the upper window bar and any of the window bar tools (minimize, maxamize and close).  Then sets the image into the form, waits the specified delay length then withdraws itself and returns control to the Main code  set.

###tooltip.py
There should be no changes needed to this file, since the tooltip information (text and which widget the tooltip is associated with) is done within the Main_setup.py file (or your project file).

###Tooltip setup
As mentioned above, I put the tooltip definitions in the "main" support file in its own function.  Each tooltip is setup as follows...
```python
	Tooltip(
	            w.tbtnFileNew,                # Which widget
	            msg = 'Create a NEW file',    # Text for the tooltip box
	            follow=False,                 # See tooltip.py for information on this
	            delay=0.5)                    # See tooltip.py for information on this
```
            

##Links
The original tooltip source code is available at http://code.activestate.com/recipes/576688-tooltip-for-tkinter/

Page can be found at https://sourceforge.net/projects/page/
