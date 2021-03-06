# -*- coding: utf-8 -*-

"""
Logger provides a text handler for logging feature.
Taken from https://stackoverflow.com/questions/13318742/python-logging-to-tkinter-text-widget
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'

import logging
import tkinter as tk


class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget
    # Adapted from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06

    def __init__(self, widget):

        # run the regular Handler __init__
        logging.Handler.__init__(self)

        # Store a reference to the Text it will log to
        self.widget = widget

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.widget.configure(state='normal')
            self.widget.insert(tk.END, msg + '\n')
            self.widget.configure(state='disabled')

            # Autoscroll to the bottom
            self.widget.yview(tk.END)

        # This is necessary because we can't modify the Text from other threads
        self.widget.after(0, append)

