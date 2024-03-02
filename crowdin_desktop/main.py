# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from . import resource_rc # noqa: F401

def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    engine.load("qrc:///qml/main.qml")
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
