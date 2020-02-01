# -*- coding: utf-8 -*-

"""
Implements Connector base class.
"""

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from abc import abstractmethod
from connector import GUI
from connector.models import Model


class Connector:
    """
    the Controller is controller class that accepts user’s inputs
    and delegates data representation to a View and data handling to a Model.
    """

    def __init__(self,  title=None):
        self.model = Model()
        self.model.title = title
        self.gui = GUI(self.model)

        # Commands and bindings
        self.gui.controls.btn_connect['command'] = self.connect
        self.gui.bind('<Return>', self._connect)
        self.gui.controls.btn_disconnect['command'] = self.disconnect
        self.gui.controls.btn_close['command'] = self.close

    def _connect(self, event):
        # Connect if connection button is not disabled.
        if not str(self.gui.controls.btn_connect['state']) == 'disabled':
            self.connect()

    @staticmethod
    def switch(func):
        def switcher(*args):
            self = args[0]
            self.model.status.code *= -1
            func(self)
            self.gui.controls.switch()
            self.model.status.code += 1
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

        if self.model.is_connected:
            try:
                self.disconnect()
            except Exception as e:
                print(e)

        self.gui.quit()

    def run(self):
        self.gui.mainloop()

