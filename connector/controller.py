# -*- coding: utf-8 -*-

"""
Implements SAP Logon widget.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from abc import abstractmethod
from connector import GUI, Model


class Connector:
    """
    the Controller is controller class that accepts user’s inputs
    and delegates data representation to a View and data handling to a Model.
    """

    def __init__(self, **options):
        self.model = Model(**options)
        self.gui = GUI(self.model)

        # Commands and bindings
        self.gui.controls.btn_connect['command'] = self.connect
        self.gui.controls.btn_disconnect['command'] = self.disconnect
        self.gui.controls.btn_close['command'] = self.close

        if options.get('sap'):
            self.gui.options.saplogon.lbx_sap_services.bind('<Double-Button-1>', self._connect)
        elif options.get('rsa'):
            pass
            self.gui.after(250, self.check_rsa_key)
        else:
            self.gui.bind('<Return>', self._connect)

    def check_rsa_key(self):
        # print('checking rsa')
        rsa_key = self.gui.options.rsa.ent_security_id.get()
        if len(rsa_key) == 6:
            self.gui.controls.btn_connect['state'] = 'enabled'
            self.gui.bind('<Return>', self._connect)
        else:
            self.gui.controls.btn_connect['state'] = 'disabled'
            self.gui.unbind('<Return>')

        self.gui.after(250, self.check_rsa_key)

    def _connect(self, event):
        self.connect()

    @staticmethod
    def switch(func):
        def switcher(*args):
            self = args[0]
            func(self)
            self.gui.controls.switch()
        return switcher

    @abstractmethod
    def connect(self):
        """
        Abstract method to connect.
        :return: None
        """
        pass

    @abstractmethod
    def disconnect(self):
        """
        Abstract method to disconnect.
        :return: None
        """
        pass

    def close(self):
        """
        Disconnects and closes application.
        :return: None
        """
        try:
            self.disconnect()
        except Exception:
            pass
        finally:
            self.gui.quit()

    def run(self):
        self.gui.mainloop()

