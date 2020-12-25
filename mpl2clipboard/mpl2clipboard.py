#!/usr/bin/env python

# Note that if you want to use from matplotlib.pyplot import * (e.g. in an interactive session), you need to do so after you've executed the above code, otherwise the figure you import into the default namespace will be the unpatched version.
# Original from https://stackoverflow.com/a/31607459/6881989
# tested on Linux

import io
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QImage

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