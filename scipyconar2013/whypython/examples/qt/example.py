#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from PyQt4 import QtCore, QtGui

import pycante

PATH = os.path.abspath(os.path.dirname(__file__))

UI_DIR = pycante.EDir(PATH)


class Dialog(UI_DIR("Dialog.ui")):

    def on_pushButton_clicked(self):
        text = self.lineEdit.text()
        self.label.setText("Hola " + unicode(text) + "!")


app = QtGui.QApplication([])
d = Dialog()
d.show()
app.exec_()


