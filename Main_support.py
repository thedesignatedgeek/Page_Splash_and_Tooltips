#! /usr/bin/env python
#
# Support module generated by PAGE version 4.11f
# In conjunction with Tcl version 8.6
#    Mar 05, 2018 06:49:01 AM

# ======================================================
#     Main_support.py
# ------------------------------------------------------
# Created for the Learning Page Book Project
# Written by G.D. Walters
# Copyright (c) 2018 by G.D. Walters
# This source code is released under the MIT License
# (See MIT_License.txt)
# ======================================================
# Additional imports are splash and tooltip
# ======================================================
import sys
import splash1
import splash1_support   # This is so we can call destroy_window()
from tooltip import ToolTip


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def mbAbout():
    print('Main_support.mbAbout')
    sys.stdout.flush()


def mbCopy():
    print('Main_support.mbCopy')
    sys.stdout.flush()


def mbCut():
    print('Main_support.mbCut')
    sys.stdout.flush()


def mbExit():
    print('Main_support.mbExit')
    sys.stdout.flush()
    destroy_window()


def mbFileNew():
    print('Main_support.mbFileNew')
    sys.stdout.flush()


def mbFileOpen():
    print('Main_support.mbFileOpen')
    sys.stdout.flush()


def mbPaste():
    print('Main_support.mbPaste')
    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    # ======================================================
    #  Hide the main window until the splash screen is done
    # ======================================================
    root.withdraw()
    # ======================================================
    # Set the width and height you want the splash screen to be
    # ======================================================
    splashwidth = 640
    splashheight = 400
    # ======================================================
    # Call the splash screen with the delay, width, height and image file
    # ======================================================
    splash1.create_Splash(
        root,
        [4000, splashwidth, splashheight, "./graphics/splash.png"])
    # ======================================================
    # Center our main screen
    # ======================================================
    centre_screen()
    # ======================================================
    # Set the Tooltips
    # ======================================================
    setup_tooltips()


# ======================================================
# This shows the main window after being hidden
# ======================================================
def show_me():
    # Show main...
    root.deiconify()
    # and close the splash screen window
    splash1_support.destroy_window()


# ======================================================
# This will centre the main Toplevel in the screen
# ======================================================
def centre_screen():
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    w = 1024
    h = 700
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


# ======================================================
# Set up the tool tips, attaching each to a widget
# ======================================================
def setup_tooltips():
    ToolTip(
        w.tbtnFileNew,
        msg='Create a NEW file',
        follow=False,
        delay=0.5)
    ToolTip(
        w.tbtnFileOpen,
        msg='Open an EXISTING file',
        follow=False,
        delay=0.5)
    ToolTip(
        w.tbtnCopy,
        msg='Copy selected text to clipboard',
        follow=False,
        delay=0.5)
    ToolTip(
        w.tbtnCut,
        msg='Cuts selected text to clipboard',
        follow=False,
        delay=0.5)
    ToolTip(
        w.tbtnPaste,
        msg='Pastes clipboard data to cursor position',
        follow=False,
        delay=0.5)
    ToolTip(
        w.tbtnAbout,
        msg='Shows information about\nthis program',
        follow=False,
        delay=0.5)
    ToolTip(
        w.tbtnExit,
        msg='Exits this program',
        follow=False,
        delay=0.5)
    # ======================================================
    #              End of SetupToolTips
    # ======================================================


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import Main
    Main.vp_start_gui()

# ======================================================
#               End of Main_support.py
# ======================================================
