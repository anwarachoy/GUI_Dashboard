#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import QUrl, QObject, pyqtSignal, pyqtSlot, QTimer
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine

class RotateValue(QObject):
        def __init__(self):
                super(RotateValue,self).__init__()
                self.r = 0

        # if a slot returns a value the return value type must be explicitly
        # defined in the decorator
        @pyqtSlot(result=float)
        def val(self):
                self.r = float (input("Angle rotation: "))
                #self.r = 90
                return self.r

if __name__ == "__main__":
        app = QGuiApplication(sys.argv)

        view = QQuickView()
        view.setSource(QUrl('main.qml'))

        rotatevalue = RotateValue()

        timer = QTimer()
        timer.start(10)

        context = view.rootContext()
        context.setContextProperty("rotatevalue", rotatevalue)

        root = view.rootObject()
        timer.timeout.connect(root.updateValue)

        engine = QQmlApplicationEngine(app)
        engine.quit.connect(app.quit)

        view.showFullScreen()

        sys.exit(app.exec_())
