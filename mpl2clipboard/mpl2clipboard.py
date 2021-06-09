#!/usr/bin/env python

# Note that if you want to use from matplotlib.pyplot import * (e.g. in an interactive session), you need to do so after you've executed the above code, otherwise the figure you import into the default namespace will be the unpatched version.
# Original from https://stackoverflow.com/a/31607459/6881989
# tested on Linux

import io
# Must use Qt backend, otherwise following error
#QGuiApplication: Must construct a QGuiApplication before accessing a QClipboard
#Traceback (most recent call last):
#  File "/usr/lib/python3.8/site-packages/matplotlib/cbook/__init__.py", line 224, in process
#    func(*args, **kwargs)
#  File "/home/junfeng/git/mpl2clipboard/mpl2clipboard/mpl2clipboard.py", line 29, in clipboard_handler
#    QApplication.clipboard().setImage(QImage.fromData(buf.getvalue()))
#AttributeError: 'NoneType' object has no attribute 'setImage'
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
try:
    from PySide2.QtWidgets import QApplication
    from PySide2.QtGui import QImage
except ImportError as e:
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QImage

def add_clipboard_to_figures():
    # use monkey-patching to replace the original plt.figure() function with
    # our own, which supports clipboard-copying
    oldfig = plt.figure

    def newfig(*args, **kwargs):
        fig = oldfig(*args, **kwargs)
        def clipboard_handler(event):
            if event.key == 'ctrl+c':
                # store the image in a buffer using savefig(), this has the
                # advantage of applying all the default savefig parameters
                # such as background color; those would be ignored if you simply
                # grab the canvas using Qt
                buf = io.BytesIO()
                fig.savefig(buf)
                QApplication.clipboard().setImage(QImage.fromData(buf.getvalue()))
                buf.close()

        fig.canvas.mpl_connect('key_press_event', clipboard_handler)
        return fig

    plt.figure = newfig

#add_clipboard_to_figures()
