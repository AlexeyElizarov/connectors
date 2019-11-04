from tkinter import ttk
from widgets.rsa import LFrRSA


class FrmOptions(ttk.Frame):
    """
    Implements manager to display optional parameters for connection.
    """

    _padx = 2
    _pady = 2

    def __init__(self, root, **options):
        ttk.Frame.__init__(self, root)

        if options.get('rsa'):
            self.rsa = LFrRSA(self)
            self.rsa.pack(expand=True, fill='x', padx=self._padx, pady=self._pady)