#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MPK M2-editor
# Copyright (C) 2017  Damien Picard dam.pic AT free.fr
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


# class DragDropTab(QtWidgets.QTabWidget, QtWidgets.QAbstractButton):
#
#     def __init__(self, parent):
#         super().__init__(parent)
#
#         self.setAcceptDrops(True)
#
#     def mouseMoveEvent(self, e):
#
#         mimeData = QtCore.QMimeData()
#
#         drag = QtGui.QDrag(self)
#         drag.setMimeData(mimeData)
#         drag.setHotSpot(e.pos() - self.rect().topLeft())
#
#         dropAction = drag.exec_(QtCore.Qt.MoveAction)
#
#     def mousePressEvent(self, e):
#         # QtWidgets.QPushButton.mousePressEvent(self, e)
#         # if e.button() == QtCore.Qt.LeftButton:
#         print('press')
#
#     def dragEnterEvent(self, e):
#         # if e.mimeData().hasFormat('text/plain'):
#         e.accept()
#         # else:
#         # e.ignore()
#
#     def dropEvent(self, e):
#         print(e)
#         # print(dir(e))
#         print(e.mimeData().text())
#         # self.setText(e.mimeData().text())

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1032, 764)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.options = QtWidgets.QGridLayout()
        self.options.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.options.setContentsMargins(1, 5, 5, 5)
        self.options.setObjectName("options")

        self.getCurrentPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.getCurrentPushButton.setObjectName("getCurrentPushButton")
        self.getCurrentPushButton.clicked.connect(self.get_active_programme)
        self.options.addWidget(self.getCurrentPushButton, 0, 0, 1, 1)

        self.sendCurrentPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendCurrentPushButton.setObjectName("sendCurrentPushButton")
        self.sendCurrentPushButton.clicked.connect(self.send_active_programme)
        self.options.addWidget(self.sendCurrentPushButton, 1, 0, 1, 1)

        self.getAllPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.getAllPushButton.setObjectName("getAllPushButton")
        self.getAllPushButton.clicked.connect(self.get_all_programmes)
        self.options.addWidget(self.getAllPushButton, 0, 1, 1, 1)

        self.sendAllPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendAllPushButton.setObjectName("sendAllPushButton")
        self.sendAllPushButton.clicked.connect(self.send_all_programmes)
        self.options.addWidget(self.sendAllPushButton, 1, 1, 1, 1)

        # self.liveUpdateCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        # self.liveUpdateCheckBox.setObjectName("liveUpdateCheckBox")
        # self.liveUpdateCheckBox.setEnabled(False)
        # self.options.addWidget(self.liveUpdateCheckBox, 0, 2, 1, 1)

        self.getRAMPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.getRAMPushButton.setObjectName("getRAMPushButton")
        self.getRAMPushButton.clicked.connect(self.get_RAM)
        self.options.addWidget(self.getRAMPushButton, 0, 2, 1, 1)

        self.sendRAMPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendRAMPushButton.setObjectName("sendRAMPushButton")
        self.sendRAMPushButton.clicked.connect(self.send_RAM)
        self.options.addWidget(self.sendRAMPushButton, 1, 2, 1, 1)

        self.gridLayout.addLayout(self.options, 1, 0, 1, 1)

        self.programmes = QtWidgets.QTabWidget(self.centralwidget)
        self.programmes.setEnabled(True)
        self.programmes.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.programmes.setObjectName("programmes")

        # Programmes
        self.progs = []
        for prog_i in range(1, 5):
            prog = {}
            prog["prog1"] = QtWidgets.QWidget()
            prog["prog1"].setObjectName("prog%s" % prog_i)
            prog["gridLayout_2"] = QtWidgets.QGridLayout(prog["prog1"])
            prog["gridLayout_2"].setContentsMargins(0, 0, 0, 0)
            prog["gridLayout_2"].setObjectName("gridLayout_2")
            prog["knobsGroupBox"] = QtWidgets.QGroupBox(prog["prog1"])
            prog["knobsGroupBox"].setObjectName("knobsGroupBox")
            prog["gridLayout_5"] = QtWidgets.QGridLayout(prog["knobsGroupBox"])
            prog["gridLayout_5"].setContentsMargins(0, 0, 0, 0)
            prog["gridLayout_5"].setSpacing(0)
            prog["gridLayout_5"].setObjectName("gridLayout_5")

            # Knobs
            prog["knobs"] = []
            for knob_i in range(8):
                knob = {}
                knob["knobGroupBox"] = QtWidgets.QGroupBox(prog["knobsGroupBox"])
                knob["knobGroupBox"].setObjectName("knobGroupBox")
                knob["knobGridLayout"] = QtWidgets.QGridLayout(knob["knobGroupBox"])
                knob["knobGridLayout"].setContentsMargins(0, 0, 0, 0)
                knob["knobGridLayout"].setSpacing(0)
                knob["knobGridLayout"].setObjectName("knobGridLayout")
                knob["knobCCSpinBox"] = QtWidgets.QSpinBox(knob["knobGroupBox"])
                knob["knobCCSpinBox"].setMaximum(127)
                knob["knobCCSpinBox"].setObjectName("knobCCSpinBox")
                knob["knobGridLayout"].addWidget(knob["knobCCSpinBox"], 0, 1, 1, 1)
                knob["knobMinSpinBox"] = QtWidgets.QSpinBox(knob["knobGroupBox"])
                knob["knobMinSpinBox"].setMaximum(127)
                knob["knobMinSpinBox"].setObjectName("knobMinSpinBox")
                knob["knobGridLayout"].addWidget(knob["knobMinSpinBox"], 1, 1, 1, 1)
                knob["knobMinLabel"] = QtWidgets.QLabel(knob["knobGroupBox"])
                knob["knobMinLabel"].setObjectName("knobMinLabel")
                knob["knobGridLayout"].addWidget(knob["knobMinLabel"], 1, 0, 1, 1)
                knob["knobMaxSpinBox"] = QtWidgets.QSpinBox(knob["knobGroupBox"])
                knob["knobMaxSpinBox"].setMaximum(127)
                knob["knobMaxSpinBox"].setProperty("value", 127)
                knob["knobMaxSpinBox"].setObjectName("knobMaxSpinBox")
                knob["knobGridLayout"].addWidget(knob["knobMaxSpinBox"], 2, 1, 1, 1)
                knob["knobMaxLabel"] = QtWidgets.QLabel(knob["knobGroupBox"])
                knob["knobMaxLabel"].setObjectName("knobMaxLabel")
                knob["knobGridLayout"].addWidget(knob["knobMaxLabel"], 2, 0, 1, 1)
                knob["knobCCLabel"] = QtWidgets.QLabel(knob["knobGroupBox"])
                knob["knobCCLabel"].setObjectName("knobCCLabel")
                knob["knobGridLayout"].addWidget(knob["knobCCLabel"], 0, 0, 1, 1)

                prog["gridLayout_5"].addWidget(knob["knobGroupBox"], knob_i/4+1, knob_i%4, 1, 1)
                prog["knobs"].append(knob)
            prog["gridLayout_2"].addWidget(prog["knobsGroupBox"], 0, 1, 1, 1)

            prog["miscLayout"] = QtWidgets.QHBoxLayout()
            prog["miscLayout"].setObjectName("miscLayout")
            prog["joystickLayout"] = QtWidgets.QGroupBox(prog["prog1"])
            prog["joystickLayout"].setObjectName("joystickLayout")
            prog["verticalLayout"] = QtWidgets.QVBoxLayout(prog["joystickLayout"])
            prog["verticalLayout"].setObjectName("verticalLayout")
            prog["jsXAxisLayout"] = QtWidgets.QHBoxLayout()
            prog["jsXAxisLayout"].setObjectName("jsXAxisLayout")
            prog["jsXAxisLabel"] = QtWidgets.QLabel(prog["joystickLayout"])
            prog["jsXAxisLabel"].setObjectName("jsXAxisLabel")
            prog["jsXAxisLayout"].addWidget(prog["jsXAxisLabel"])
            prog["jsXAxisLayout_2"] = QtWidgets.QVBoxLayout()
            prog["jsXAxisLayout_2"].setSpacing(0)
            prog["jsXAxisLayout_2"].setObjectName("jsXAxisLayout_2")
            prog["jsXAxisComboBox"] = QtWidgets.QComboBox(prog["joystickLayout"])
            prog["jsXAxisComboBox"].setObjectName("jsXAxisComboBox")
            prog["jsXAxisComboBox"].addItem("")
            prog["jsXAxisComboBox"].addItem("")
            prog["jsXAxisComboBox"].addItem("")
            prog["jsXAxisLayout_2"].addWidget(prog["jsXAxisComboBox"])
            prog["jsXLeftWidget"] = QtWidgets.QWidget(prog["joystickLayout"])
            # prog["jsXLeftWidget"].setEnabled(False)
            prog["jsXLeftWidget"].setObjectName("jsXLeftWidget")
            prog["gridLayout_3"] = QtWidgets.QGridLayout(prog["jsXLeftWidget"])
            prog["gridLayout_3"].setContentsMargins(0, 0, 0, 0)
            prog["gridLayout_3"].setSpacing(0)
            prog["gridLayout_3"].setObjectName("gridLayout_3")
            prog["jsXLeftLabel"] = QtWidgets.QLabel(prog["jsXLeftWidget"])
            prog["jsXLeftLabel"].setObjectName("jsXLeftLabel")
            prog["gridLayout_3"].addWidget(prog["jsXLeftLabel"], 0, 0, 1, 1)
            prog["jsXLeftSpinBox"] = QtWidgets.QSpinBox(prog["jsXLeftWidget"])
            prog["jsXLeftSpinBox"].setMaximum(127)
            prog["jsXLeftSpinBox"].setObjectName("jsXLeftSpinBox")
            prog["gridLayout_3"].addWidget(prog["jsXLeftSpinBox"], 0, 1, 1, 1)
            prog["jsXRightLabel"] = QtWidgets.QLabel(prog["jsXLeftWidget"])
            prog["jsXRightLabel"].setObjectName("jsXRightLabel")
            prog["gridLayout_3"].addWidget(prog["jsXRightLabel"], 1, 0, 1, 1)
            prog["jsXRightSpinBox"] = QtWidgets.QSpinBox(prog["jsXLeftWidget"])
            prog["jsXRightSpinBox"].setMaximum(127)
            prog["jsXRightSpinBox"].setObjectName("jsXRightSpinBox")
            prog["gridLayout_3"].addWidget(prog["jsXRightSpinBox"], 1, 1, 1, 1)
            prog["jsXLeftSpinBox"].raise_()
            prog["jsXRightSpinBox"].raise_()
            prog["jsXLeftLabel"].raise_()
            prog["jsXRightLabel"].raise_()
            prog["jsXAxisLayout_2"].addWidget(prog["jsXLeftWidget"])
            prog["jsXAxisLayout"].addLayout(prog["jsXAxisLayout_2"])
            prog["verticalLayout"].addLayout(prog["jsXAxisLayout"])
            prog["jsYAxisLayout"] = QtWidgets.QHBoxLayout()
            prog["jsYAxisLayout"].setObjectName("jsYAxisLayout")
            prog["jsYAxisLabel"] = QtWidgets.QLabel(prog["joystickLayout"])
            prog["jsYAxisLabel"].setObjectName("jsYAxisLabel")
            prog["jsYAxisLayout"].addWidget(prog["jsYAxisLabel"])
            prog["jsYAxisLayout_2"] = QtWidgets.QVBoxLayout()
            prog["jsYAxisLayout_2"].setSpacing(0)
            prog["jsYAxisLayout_2"].setObjectName("jsYAxisLayout_2")
            prog["jsYAxisComboBox"] = QtWidgets.QComboBox(prog["joystickLayout"])
            prog["jsYAxisComboBox"].setObjectName("jsYAxisComboBox")
            prog["jsYAxisComboBox"].addItem("")
            prog["jsYAxisComboBox"].addItem("")
            prog["jsYAxisComboBox"].addItem("")
            prog["jsYAxisLayout_2"].addWidget(prog["jsYAxisComboBox"])
            prog["jsYWidget"] = QtWidgets.QWidget(prog["joystickLayout"])
            # prog["jsYWidget"].setEnabled(False)
            prog["jsYWidget"].setObjectName("jsYWidget")
            prog["gridLayout_7"] = QtWidgets.QGridLayout(prog["jsYWidget"])
            prog["gridLayout_7"].setContentsMargins(0, 0, 0, 0)
            prog["gridLayout_7"].setSpacing(0)
            prog["gridLayout_7"].setObjectName("gridLayout_7")
            prog["jsYUpLabel"] = QtWidgets.QLabel(prog["jsYWidget"])
            prog["jsYUpLabel"].setObjectName("jsYUpLabel")
            prog["gridLayout_7"].addWidget(prog["jsYUpLabel"], 0, 0, 1, 1)
            prog["jsYUpSpinBox"] = QtWidgets.QSpinBox(prog["jsYWidget"])
            prog["jsYUpSpinBox"].setMaximum(127)
            prog["jsYUpSpinBox"].setObjectName("jsYUpSpinBox")
            prog["gridLayout_7"].addWidget(prog["jsYUpSpinBox"], 0, 1, 1, 1)
            prog["jsYDownLabel"] = QtWidgets.QLabel(prog["jsYWidget"])
            prog["jsYDownLabel"].setObjectName("jsYDownLabel")
            prog["gridLayout_7"].addWidget(prog["jsYDownLabel"], 1, 0, 1, 1)
            prog["jsYDownSpinBox"] = QtWidgets.QSpinBox(prog["jsYWidget"])
            prog["jsYDownSpinBox"].setMaximum(127)
            prog["jsYDownSpinBox"].setObjectName("jsYDownSpinBox")
            prog["gridLayout_7"].addWidget(prog["jsYDownSpinBox"], 1, 1, 1, 1)
            prog["jsYAxisLayout_2"].addWidget(prog["jsYWidget"])
            prog["jsYAxisLayout"].addLayout(prog["jsYAxisLayout_2"])
            prog["verticalLayout"].addLayout(prog["jsYAxisLayout"])
            prog["miscLayout"].addWidget(prog["joystickLayout"])
            prog["arpegGroupBox"] = QtWidgets.QGroupBox(prog["prog1"])
            prog["arpegGroupBox"].setObjectName("arpegGroupBox")
            prog["verticalLayout_3"] = QtWidgets.QVBoxLayout(prog["arpegGroupBox"])
            prog["verticalLayout_3"].setContentsMargins(0, 0, 0, 0)
            prog["verticalLayout_3"].setSpacing(0)
            prog["verticalLayout_3"].setObjectName("verticalLayout_3")
            prog["tempoLayout"] = QtWidgets.QHBoxLayout()
            prog["tempoLayout"].setObjectName("tempoLayout")
            prog["tempoLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["tempoLabel"].setObjectName("tempoLabel")
            prog["tempoLayout"].addWidget(prog["tempoLabel"])
            prog["tempoSpinBox"] = QtWidgets.QSpinBox(prog["arpegGroupBox"])
            prog["tempoSpinBox"].setMinimum(30)
            prog["tempoSpinBox"].setMaximum(240)
            prog["tempoSpinBox"].setProperty("value", 120)
            prog["tempoSpinBox"].setObjectName("tempoSpinBox")
            prog["tempoLayout"].addWidget(prog["tempoSpinBox"])
            prog["verticalLayout_3"].addLayout(prog["tempoLayout"])
            prog["timeDivLayout"] = QtWidgets.QHBoxLayout()
            prog["timeDivLayout"].setObjectName("timeDivLayout")
            prog["timeDivLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["timeDivLabel"].setObjectName("timeDivLabel")
            prog["timeDivLayout"].addWidget(prog["timeDivLabel"])
            prog["timeDivComboBox"] = QtWidgets.QComboBox(prog["arpegGroupBox"])
            prog["timeDivComboBox"].setObjectName("timeDivComboBox")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivLayout"].addWidget(prog["timeDivComboBox"])
            prog["verticalLayout_3"].addLayout(prog["timeDivLayout"])
            prog["swingLayout"] = QtWidgets.QHBoxLayout()
            prog["swingLayout"].setObjectName("swingLayout")
            prog["swingLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["swingLabel"].setObjectName("swingLabel")
            prog["swingLayout"].addWidget(prog["swingLabel"])
            prog["swingComboBox"] = QtWidgets.QComboBox(prog["arpegGroupBox"])
            prog["swingComboBox"].setObjectName("swingComboBox")
            prog["swingComboBox"].addItem("")
            prog["swingComboBox"].addItem("")
            prog["swingComboBox"].addItem("")
            prog["swingComboBox"].addItem("")
            prog["swingComboBox"].addItem("")
            prog["swingComboBox"].addItem("")
            prog["swingLayout"].addWidget(prog["swingComboBox"])
            prog["verticalLayout_3"].addLayout(prog["swingLayout"])
            prog["arpOctaveLayout"] = QtWidgets.QHBoxLayout()
            prog["arpOctaveLayout"].setObjectName("arpOctaveLayout")
            prog["arpOctaveLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["arpOctaveLabel"].setObjectName("arpOctaveLabel")
            prog["arpOctaveLayout"].addWidget(prog["arpOctaveLabel"])
            prog["arpOctaveSpinBox"] = QtWidgets.QSpinBox(prog["arpegGroupBox"])
            prog["arpOctaveSpinBox"].setMinimum(1)
            prog["arpOctaveSpinBox"].setMaximum(4)
            prog["arpOctaveSpinBox"].setProperty("value", 0)
            prog["arpOctaveSpinBox"].setObjectName("arpOctaveSpinBox")
            prog["arpOctaveLayout"].addWidget(prog["arpOctaveSpinBox"])
            prog["verticalLayout_3"].addLayout(prog["arpOctaveLayout"])
            prog["modeLayout"] = QtWidgets.QHBoxLayout()
            prog["modeLayout"].setObjectName("modeLayout")
            prog["modeLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["modeLabel"].setObjectName("modeLabel")
            prog["modeLayout"].addWidget(prog["modeLabel"])
            prog["modeComboBox"] = QtWidgets.QComboBox(prog["arpegGroupBox"])
            prog["modeComboBox"].setObjectName("modeComboBox")
            prog["modeComboBox"].addItem("")
            prog["modeComboBox"].addItem("")
            prog["modeComboBox"].addItem("")
            prog["modeComboBox"].addItem("")
            prog["modeComboBox"].addItem("")
            prog["modeComboBox"].addItem("")
            prog["modeLayout"].addWidget(prog["modeComboBox"])
            prog["verticalLayout_3"].addLayout(prog["modeLayout"])
            prog["tempoTapsLayout"] = QtWidgets.QHBoxLayout()
            prog["tempoTapsLayout"].setObjectName("tempoTapsLayout")
            prog["tempoTapsLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["tempoTapsLabel"].setObjectName("tempoTapsLabel")
            prog["tempoTapsLayout"].addWidget(prog["tempoTapsLabel"])
            prog["tempoTapsSpinBox"] = QtWidgets.QSpinBox(prog["arpegGroupBox"])
            prog["tempoTapsSpinBox"].setMinimum(2)
            prog["tempoTapsSpinBox"].setMaximum(4)
            prog["tempoTapsSpinBox"].setProperty("value", 2)
            prog["tempoTapsSpinBox"].setObjectName("tempoTapsSpinBox")
            prog["tempoTapsLayout"].addWidget(prog["tempoTapsSpinBox"])
            prog["verticalLayout_3"].addLayout(prog["tempoTapsLayout"])
            prog["clockLayout"] = QtWidgets.QHBoxLayout()
            prog["clockLayout"].setObjectName("clockLayout")
            prog["clockLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["clockLabel"].setObjectName("clockLabel")
            prog["clockLayout"].addWidget(prog["clockLabel"])
            prog["clockComboBox"] = QtWidgets.QComboBox(prog["arpegGroupBox"])
            prog["clockComboBox"].setObjectName("clockComboBox")
            prog["clockComboBox"].addItem("")
            prog["clockComboBox"].addItem("")
            prog["clockLayout"].addWidget(prog["clockComboBox"])
            prog["verticalLayout_3"].addLayout(prog["clockLayout"])
            prog["latchCheckBox"] = QtWidgets.QCheckBox(prog["arpegGroupBox"])
            prog["latchCheckBox"].setObjectName("latchCheckBox")
            prog["verticalLayout_3"].addWidget(prog["latchCheckBox"])
            prog["arpCheckBox"] = QtWidgets.QCheckBox(prog["arpegGroupBox"])
            prog["arpCheckBox"].setObjectName("arpCheckBox")
            # prog["arpCheckBox"].stateChanged.connect(self.send_RAM)
            prog["verticalLayout_3"].addWidget(prog["arpCheckBox"])
            prog["miscLayout"].addWidget(prog["arpegGroupBox"])
            prog["chanKeysLayout"] = QtWidgets.QVBoxLayout()
            prog["chanKeysLayout"].setObjectName("chanKeysLayout")
            prog["channelsGroupBox"] = QtWidgets.QGroupBox(prog["prog1"])
            prog["channelsGroupBox"].setObjectName("channelsGroupBox")
            prog["verticalLayout_5"] = QtWidgets.QVBoxLayout(prog["channelsGroupBox"])
            prog["verticalLayout_5"].setObjectName("verticalLayout_5")
            prog["padLayout"] = QtWidgets.QHBoxLayout()
            prog["padLayout"].setObjectName("padLayout")
            prog["padLabel"] = QtWidgets.QLabel(prog["channelsGroupBox"])
            prog["padLabel"].setObjectName("padLabel")
            prog["padLayout"].addWidget(prog["padLabel"])
            prog["padSpinBox"] = QtWidgets.QSpinBox(prog["channelsGroupBox"])
            prog["padSpinBox"].setMinimum(1)
            prog["padSpinBox"].setMaximum(16)
            prog["padSpinBox"].setObjectName("padSpinBox")
            prog["padLayout"].addWidget(prog["padSpinBox"])
            prog["verticalLayout_5"].addLayout(prog["padLayout"])
            prog["keysLayout"] = QtWidgets.QHBoxLayout()
            prog["keysLayout"].setObjectName("keysLayout")
            prog["keysLabel"] = QtWidgets.QLabel(prog["channelsGroupBox"])
            prog["keysLabel"].setObjectName("keysLabel")
            prog["keysLayout"].addWidget(prog["keysLabel"])
            prog["keySpinBox"] = QtWidgets.QSpinBox(prog["channelsGroupBox"])
            prog["keySpinBox"].setMinimum(1)
            prog["keySpinBox"].setMaximum(16)
            prog["keySpinBox"].setObjectName("keySpinBox")
            prog["keysLayout"].addWidget(prog["keySpinBox"])
            prog["verticalLayout_5"].addLayout(prog["keysLayout"])
            prog["chanKeysLayout"].addWidget(prog["channelsGroupBox"])
            prog["keyboardGroupBox"] = QtWidgets.QGroupBox(prog["prog1"])
            prog["keyboardGroupBox"].setObjectName("keyboardGroupBox")
            prog["verticalLayout_4"] = QtWidgets.QVBoxLayout(prog["keyboardGroupBox"])
            prog["verticalLayout_4"].setObjectName("verticalLayout_4")
            prog["transposeLayout"] = QtWidgets.QHBoxLayout()
            prog["transposeLayout"].setObjectName("transposeLayout")
            prog["transposeLabel"] = QtWidgets.QLabel(prog["keyboardGroupBox"])
            prog["transposeLabel"].setObjectName("transposeLabel")
            prog["transposeLayout"].addWidget(prog["transposeLabel"])
            prog["transposeSpinBox"] = QtWidgets.QSpinBox(prog["keyboardGroupBox"])
            prog["transposeSpinBox"].setMinimum(-12)
            prog["transposeSpinBox"].setMaximum(12)
            prog["transposeSpinBox"].setObjectName("transposeSpinBox")
            prog["transposeLayout"].addWidget(prog["transposeSpinBox"])
            prog["verticalLayout_4"].addLayout(prog["transposeLayout"])
            prog["octaveLayout"] = QtWidgets.QHBoxLayout()
            prog["octaveLayout"].setObjectName("octaveLayout")
            prog["octaveLabel"] = QtWidgets.QLabel(prog["keyboardGroupBox"])
            prog["octaveLabel"].setObjectName("octaveLabel")
            prog["octaveLayout"].addWidget(prog["octaveLabel"])
            prog["octaveSpinBox"] = QtWidgets.QSpinBox(prog["keyboardGroupBox"])
            prog["octaveSpinBox"].setMinimum(-4)
            prog["octaveSpinBox"].setMaximum(4)
            prog["octaveSpinBox"].setObjectName("octaveSpinBox")
            prog["octaveLayout"].addWidget(prog["octaveSpinBox"])
            prog["verticalLayout_4"].addLayout(prog["octaveLayout"])
            prog["chanKeysLayout"].addWidget(prog["keyboardGroupBox"])
            prog["miscLayout"].addLayout(prog["chanKeysLayout"])
            prog["gridLayout_2"].addLayout(prog["miscLayout"], 1, 1, 1, 1)

            # Banks
            prog["banks"] = []
            for bank_i in range(2):
                bank = {}
                bank["bankGroupBox"] = QtWidgets.QGroupBox(prog["prog1"])
                bank["bankGroupBox"].setObjectName("bankGroupBox")
                bank["bankGroupBox"].setStyleSheet("""#bankGroupBox{
    border: 2px solid %s;
    margin-top: 1.0em;
}""" % ("red" if bank_i else "green"))

                bank["gridLayout_6"] = QtWidgets.QGridLayout(bank["bankGroupBox"])
                bank["gridLayout_6"].setContentsMargins(2, 2, 2, 2)
                bank["gridLayout_6"].setSpacing(2)
                bank["gridLayout_6"].setObjectName("gridLayout_6")

                # Pads
                bank["pads"] = []
                for pad_i in range(8):
                    pad = {}
                    pad["padGroupBox"] = QtWidgets.QGroupBox(bank["bankGroupBox"])
                    pad["padGroupBox"].setObjectName("padGroupBox")
                    pad["gridLayout_43"] = QtWidgets.QGridLayout(pad["padGroupBox"])
                    pad["gridLayout_43"].setContentsMargins(0, 0, 0, 0)
                    pad["gridLayout_43"].setSpacing(0)
                    pad["gridLayout_43"].setObjectName("gridLayout_43")
                    pad["padNoteLayout"] = QtWidgets.QHBoxLayout()
                    pad["padNoteLayout"].setObjectName("padNoteLayout")
                    pad["padNoteLabel"] = QtWidgets.QLabel(pad["padGroupBox"])
                    pad["padNoteLabel"].setObjectName("padNoteLabel")
                    pad["padNoteLayout"].addWidget(pad["padNoteLabel"])
                    pad["padNoteComboBox"] = QtWidgets.QComboBox(pad["padGroupBox"])
                    pad["padNoteComboBox"].setObjectName("padNoteComboBox")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteLayout"].addWidget(pad["padNoteComboBox"])
                    pad["padNoteSpinBox"] = QtWidgets.QSpinBox(pad["padGroupBox"])
                    pad["padNoteSpinBox"].setMinimum(-1)
                    pad["padNoteSpinBox"].setMaximum(9)
                    pad["padNoteSpinBox"].setProperty("value", 4)
                    pad["padNoteSpinBox"].setObjectName("padNoteSpinBox")
                    pad["padNoteLayout"].addWidget(pad["padNoteSpinBox"])
                    pad["gridLayout_43"].addLayout(pad["padNoteLayout"], 0, 0, 1, 1)
                    pad["padCCLayout"] = QtWidgets.QHBoxLayout()
                    pad["padCCLayout"].setObjectName("padCCLayout")
                    pad["padCCLabel"] = QtWidgets.QLabel(pad["padGroupBox"])
                    pad["padCCLabel"].setObjectName("padCCLabel")
                    pad["padCCLayout"].addWidget(pad["padCCLabel"])
                    pad["padCCSpinBox"] = QtWidgets.QSpinBox(pad["padGroupBox"])
                    pad["padCCSpinBox"].setMaximum(127)
                    pad["padCCSpinBox"].setProperty("value", 0)
                    pad["padCCSpinBox"].setObjectName("padCCSpinBox")
                    pad["padCCLayout"].addWidget(pad["padCCSpinBox"])
                    pad["gridLayout_43"].addLayout(pad["padCCLayout"], 2, 0, 1, 1)
                    pad["padPCLayout"] = QtWidgets.QHBoxLayout()
                    pad["padPCLayout"].setObjectName("padPCLayout")
                    pad["padPCLabel"] = QtWidgets.QLabel(pad["padGroupBox"])
                    pad["padPCLabel"].setObjectName("padPCLabel")
                    pad["padPCLayout"].addWidget(pad["padPCLabel"])
                    pad["padPCSpinBox"] = QtWidgets.QSpinBox(pad["padGroupBox"])
                    pad["padPCSpinBox"].setMaximum(127)
                    pad["padPCSpinBox"].setProperty("value", 0)
                    pad["padPCSpinBox"].setObjectName("padPCSpinBox")
                    pad["padPCLayout"].addWidget(pad["padPCSpinBox"])
                    pad["gridLayout_43"].addLayout(pad["padPCLayout"], 3, 0, 1, 1)
                    pad["padTypeComboBox"] = QtWidgets.QComboBox(pad["padGroupBox"])
                    pad["padTypeComboBox"].setObjectName("padTypeComboBox")
                    pad["padTypeComboBox"].addItem("")
                    pad["padTypeComboBox"].addItem("")
                    pad["gridLayout_43"].addWidget(pad["padTypeComboBox"], 4, 0, 1, 1)
                    bank["gridLayout_6"].addWidget(pad["padGroupBox"], 1-(pad_i//4), pad_i % 4, 1, 1)
                    bank["pads"].append(pad)
                prog["gridLayout_2"].addWidget(bank["bankGroupBox"], bank_i%2, 0, 1, 1)
                prog["banks"].append(bank)
            self.programmes.addTab(prog["prog1"], "")
            self.progs.append(prog)

        self.gridLayout.addWidget(self.programmes, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.file_open)

        # self.actionSave = QtWidgets.QAction(MainWindow)
        # self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionSaveAs.triggered.connect(self.file_save_as)


        self.menuCopyTo = QtWidgets.QMenu(MainWindow)
        self.menuCopyTo.setObjectName("menuCopyTo")

        self.actionCopyProgs = []
        for p_i in range(1, 5):
            actionCopyProg = QtWidgets.QAction(MainWindow)
            actionCopyProg.setObjectName("actionCopyProg_%s" % p_i)
            actionCopyProg.triggered.connect(partial(self.copy_to, p_i))
            self.menuCopyTo.addAction(actionCopyProg)
            self.actionCopyProgs.append(actionCopyProg)

        self.actionShowAutofill = QtWidgets.QAction(MainWindow)
        self.actionShowAutofill.setObjectName("actionShowAutofill")
        self.actionShowAutofill.triggered.connect(self.show_autofill)
        # self.actionFactory_preset = QtWidgets.QAction(MainWindow)
        # self.actionFactory_preset.setObjectName("actionFactory_preset")
        self.menuFile.addAction(self.actionOpen)
        # self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        # self.menuFile.addAction(self.actionFactory_preset)

        self.menuEdit.addAction(self.menuCopyTo.menuAction())
        self.menuEdit.addAction(self.actionShowAutofill)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.programmes.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_active_tab_index(self):
        return self.programmes.currentIndex()+1

    def fill_tab(self, config, p_i=None):
        if p_i is None:
            p_i = config[7]
        p_i -= 1
        # for i, k in enumerate(self.midi_config.keys()):
        prog = self.progs[p_i]
        prog["padSpinBox"].setValue(config[8]+1)
        prog["keySpinBox"].setValue(config[9]+1)

        # arp
        prog["tempoSpinBox"].setValue(config[18]*128 + config[19])
        prog["timeDivComboBox"].setCurrentIndex(config[13])
        prog["swingComboBox"].setCurrentIndex(config[16])
        prog["arpOctaveSpinBox"].setValue(config[20] + 1)
        prog["modeComboBox"].setCurrentIndex(config[12])
        prog["tempoTapsSpinBox"].setValue(config[17])
        prog["clockComboBox"].setCurrentIndex(config[14])
        prog["latchCheckBox"].setCheckState(config[15] * 2)
        prog["arpCheckBox"].setCheckState(config[11] * 2)

        # joystick
        prog["jsXAxisComboBox"].setCurrentIndex(config[21])
        prog["jsXLeftSpinBox"].setValue(config[22])
        prog["jsXRightSpinBox"].setValue(config[23])
        prog["jsYAxisComboBox"].setCurrentIndex(config[24])
        prog["jsYDownSpinBox"].setValue(config[25])
        prog["jsYUpSpinBox"].setValue(config[26])

        prog["transposeSpinBox"].setValue(config[115] - 12)
        prog["octaveSpinBox"].setValue(config[10] - 4)

        for k_i, knob in enumerate(prog["knobs"]):
            knob["knobCCSpinBox"].setValue(config[91 + k_i*3])
            knob["knobMinSpinBox"].setValue(config[91 + 1 + k_i*3])
            knob["knobMaxSpinBox"].setValue(config[91 + 2 + k_i*3])

        for b_i, bank in enumerate(prog["banks"]):
            for pad_i, pad in enumerate(bank["pads"]):
                note = config[27 + b_i*4*8 + pad_i*4]
                pad["padNoteComboBox"].setCurrentIndex(note % 12)
                pad["padNoteSpinBox"].setValue(note // 12 - 1)
                pad["padPCSpinBox"].setValue(config[27 + b_i*4*8 + 1 + pad_i*4])
                pad["padCCSpinBox"].setValue(config[27 + b_i*4*8 + 2 + pad_i*4])
                pad["padTypeComboBox"].setCurrentIndex(config[27 + b_i*4*8 + 3 + pad_i*4])


    def get_tab_programme(self, p_i):
        config = self.midi_config.copy()
        prog = self.progs[p_i-1]

        config["programme"] = p_i

        config["pad_channel"] = prog["padSpinBox"].value() - 1
        config["key_channel"] = prog["keySpinBox"].value() - 1

        # arp
        config["arp_tempo_0"] = prog["tempoSpinBox"].value() // 128
        config["arp_tempo_1"] = prog["tempoSpinBox"].value() % 128
        config["arp_time"] = prog["timeDivComboBox"].currentIndex()
        config["arp_swing"] = prog["swingComboBox"].currentIndex()
        config["arp_octave"] = prog["arpOctaveSpinBox"].value() - 1
        config["arp_mode"] = prog["modeComboBox"].currentIndex()
        config["arp_taps"] = prog["tempoTapsSpinBox"].value()
        config["arp_clock"] = prog["clockComboBox"].currentIndex()
        config["arp_latch"] = prog["latchCheckBox"].isChecked()
        config["arp_on"] = prog["arpCheckBox"].isChecked()

        # joystick
        config["x_axis_type"] = prog["jsXAxisComboBox"].currentIndex()
        config["x_axis_L"] = prog["jsXLeftSpinBox"].value()
        config["x_axis_R"] = prog["jsXRightSpinBox"].value()
        config["y_axis_type"] = prog["jsYAxisComboBox"].currentIndex()
        config["y_axis_D"] = prog["jsYDownSpinBox"].value()
        config["y_axis_U"] = prog["jsYUpSpinBox"].value()

        config["key_transpose"] = prog["transposeSpinBox"].value() + 12
        config["key_octave"] = prog["octaveSpinBox"].value() + 4

        for k_i, knob in enumerate(prog["knobs"]):
            config["k%s_CC" % (k_i+1)] = knob["knobCCSpinBox"].value()
            config["k%s_LO" % (k_i+1)] = knob["knobMinSpinBox"].value()
            config["k%s_HI" % (k_i+1)] = knob["knobMaxSpinBox"].value()

        for b_i, bank in enumerate(prog["banks"]):
            for pad_i, pad in enumerate(bank["pads"]):
                # note = config[27 + b_i*4*8 + pad_i*4]
                config["b%s_p%s_NT" % (b_i+1, pad_i+1)] = pad["padNoteComboBox"].currentIndex() + (pad["padNoteSpinBox"].value()+1) * 12
                config["b%s_p%s_PC" % (b_i+1, pad_i+1)] = pad["padPCSpinBox"].value()
                config["b%s_p%s_CC" % (b_i+1, pad_i+1)] = pad["padCCSpinBox"].value()
                config["b%s_p%s_TP" % (b_i+1, pad_i+1)] = pad["padTypeComboBox"].currentIndex()
        return list(config.values())

    def file_open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file…', '', 'MK2 files (*.mk2)')
        if filename:
            if filename[0].endswith('.mk2'):
                self.load_mk2(filename[0])
            else:
                print('Unrecognized filetype')

    def file_save_as(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(None, 'Save file…', '', 'MK2 files (*.mk2)')
        if filename:
            if filename[0].endswith('.mk2'):
                self.save_mk2(filename[0])
            else:
                print('Unrecognized filetype')

    def get_tooltip(self, string):
        return "<html><head/><body><p>" + string.replace("\n", "</p><p>") + "</p></body></html>"

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MPK Mini Mk2 Editor"))
        self.getAllPushButton.setText(_translate("MainWindow", "Get all"))
        self.getAllPushButton.setToolTip(self.get_tooltip(_translate("MainWindow", "Get all programmes")))
        self.getCurrentPushButton.setText(_translate("MainWindow", "Get current"))
        self.getCurrentPushButton.setToolTip(self.get_tooltip(_translate("MainWindow", "Get only programme on current tab")))
        self.sendCurrentPushButton.setText(_translate("MainWindow", "Send current"))
        self.sendCurrentPushButton.setToolTip(self.get_tooltip(_translate("MainWindow", "Send only programme on current tab")))
        self.sendAllPushButton.setText(_translate("MainWindow", "Send all"))
        self.sendAllPushButton.setToolTip(self.get_tooltip(_translate("MainWindow", "Send all programmes")))
        # self.liveUpdateCheckBox.setText(_translate("MainWindow", "Live update"))
        # self.liveUpdateCheckBox.setToolTip(self.get_tooltip(_translate("MainWindow", "Send values as they are changed")))
        self.getRAMPushButton.setText(_translate("MainWindow", "Get RAM"))
        self.getRAMPushButton.setToolTip(self.get_tooltip(_translate("MainWindow", "Get current controller status")))
        self.sendRAMPushButton.setText(_translate("MainWindow", "Send RAM"))
        self.sendRAMPushButton.setToolTip(self.get_tooltip(_translate("MainWindow", "Send current tab to the controller, without overwriting any programme")))
        for p_i, prog in enumerate(self.progs):
            prog["knobsGroupBox"].setTitle(_translate("MainWindow", "Knobs"))
            for k_i, knob in enumerate(prog["knobs"]):
                knob["knobGroupBox"].setTitle(_translate("MainWindow", "Knob ") + str(k_i+1))
                knob["knobMinLabel"].setText(_translate("MainWindow", "Min"))
                knob["knobMaxLabel"].setText(_translate("MainWindow", "Max"))
                knob["knobCCLabel"].setText(_translate("MainWindow", "CC"))
            prog["joystickLayout"].setTitle(_translate("MainWindow", "Joystick"))
            prog["jsXAxisLabel"].setText(_translate("MainWindow", "X Axis"))
            prog["jsXAxisComboBox"].setItemText(0, _translate("MainWindow", "Pitchbend"))
            prog["jsXAxisComboBox"].setItemText(1, _translate("MainWindow", "CC 1"))
            prog["jsXAxisComboBox"].setItemText(2, _translate("MainWindow", "CC 2"))
            prog["jsXAxisComboBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Behaviour on the X axis\nPitchbend: send bend signal\nCC 1: send CC signal on channel from <i>Left</i> field\nCC 2: send CC signal on channels from either <i>Left</i> or <i>Right</i> field")))
            prog["jsXLeftLabel"].setText(_translate("MainWindow", "Left"))
            prog["jsXRightLabel"].setText(_translate("MainWindow", "Right"))
            prog["jsYAxisLabel"].setText(_translate("MainWindow", "Y Axis"))
            prog["jsYAxisComboBox"].setItemText(0, _translate("MainWindow", "Pitchbend"))
            prog["jsYAxisComboBox"].setItemText(1, _translate("MainWindow", "CC 1"))
            prog["jsYAxisComboBox"].setItemText(2, _translate("MainWindow", "CC 2"))
            prog["jsYAxisComboBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Behaviour on the Y axis\nPitchbend: send bend signal\nCC 1: send CC signal on channel from <i>Up</i> field \nCC 2: send CC signal on channels from either <i>Up</i> or <i>Down</i> field")))
            prog["jsYUpLabel"].setText(_translate("MainWindow", "Up"))
            prog["jsYDownLabel"].setText(_translate("MainWindow", "Down"))
            prog["arpegGroupBox"].setTitle(_translate("MainWindow", "Arpeggiator"))
            prog["tempoLabel"].setText(_translate("MainWindow", "Tempo"))
            prog["timeDivLabel"].setText(_translate("MainWindow", "Time div"))
            prog["timeDivComboBox"].setItemText(0, _translate("MainWindow", "1/4"))
            prog["timeDivComboBox"].setItemText(1, _translate("MainWindow", "1/4T"))
            prog["timeDivComboBox"].setItemText(2, _translate("MainWindow", "1/8"))
            prog["timeDivComboBox"].setItemText(3, _translate("MainWindow", "1/8T"))
            prog["timeDivComboBox"].setItemText(4, _translate("MainWindow", "1/16"))
            prog["timeDivComboBox"].setItemText(5, _translate("MainWindow", "1/16T"))
            prog["timeDivComboBox"].setItemText(6, _translate("MainWindow", "1/32"))
            prog["timeDivComboBox"].setItemText(7, _translate("MainWindow", "1/32T"))
            prog["timeDivComboBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Arpeggiator time signature")))
            prog["swingLabel"].setText(_translate("MainWindow", "Swing"))
            prog["swingComboBox"].setItemText(0, _translate("MainWindow", "50%"))
            prog["swingComboBox"].setItemText(1, _translate("MainWindow", "55%"))
            prog["swingComboBox"].setItemText(2, _translate("MainWindow", "57%"))
            prog["swingComboBox"].setItemText(3, _translate("MainWindow", "59%"))
            prog["swingComboBox"].setItemText(4, _translate("MainWindow", "61%"))
            prog["swingComboBox"].setItemText(5, _translate("MainWindow", "64%"))
            prog["swingComboBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Arpeggiator time shifting")))
            prog["arpOctaveLabel"].setText(_translate("MainWindow", "Octave"))
            prog["modeLabel"].setText(_translate("MainWindow", "Mode"))
            prog["modeComboBox"].setItemText(0, _translate("MainWindow", "UP"))
            prog["modeComboBox"].setItemText(1, _translate("MainWindow", "DOWN"))
            prog["modeComboBox"].setItemText(2, _translate("MainWindow", "EXCLUSIVE"))
            prog["modeComboBox"].setItemText(3, _translate("MainWindow", "INCLUSIVE"))
            prog["modeComboBox"].setItemText(4, _translate("MainWindow", "ORDER"))
            prog["modeComboBox"].setItemText(5, _translate("MainWindow", "RANDOM"))
            prog["modeComboBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Arpeggiator mode")))
            prog["tempoTapsLabel"].setText(_translate("MainWindow", "Tempo taps"))
            prog["clockLabel"].setText(_translate("MainWindow", "Clock"))
            prog["clockComboBox"].setItemText(0, _translate("MainWindow", "Internal"))
            prog["clockComboBox"].setItemText(1, _translate("MainWindow", "External"))
            prog["clockComboBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Arpeggiator clock synchronization mode")))
            prog["latchCheckBox"].setText(_translate("MainWindow", "Latch"))
            prog["latchCheckBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Arpeggiator latch: keep the arp going")))
            prog["arpCheckBox"].setText(_translate("MainWindow", "ON/OFF"))
            prog["arpCheckBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Activate arpeggiator")))
            prog["channelsGroupBox"].setTitle(_translate("MainWindow", "Channels"))
            prog["padLabel"].setText(_translate("MainWindow", "Pad"))
            prog["keysLabel"].setText(_translate("MainWindow", "Keys/CC"))
            prog["keyboardGroupBox"].setTitle(_translate("MainWindow", "Keyboard"))
            prog["transposeLabel"].setText(_translate("MainWindow", "Transpose"))
            prog["octaveLabel"].setText(_translate("MainWindow", "Octave"))
            for b_i, bank in enumerate(prog["banks"]):
                bank_name = "Bank B" if b_i else "Bank A"
                bank["bankGroupBox"].setTitle(_translate("MainWindow", bank_name))
                for pa_i, pad in enumerate(bank["pads"]):
                    pad["padGroupBox"].setTitle(_translate("MainWindow", "Pad " + str(pa_i+1)))
                    pad["padCCLabel"].setText(_translate("MainWindow", "CC"))
                    pad["padTypeComboBox"].setItemText(0, _translate("MainWindow", "Momentary"))
                    pad["padTypeComboBox"].setItemText(1, _translate("MainWindow", "Toggle"))
                    pad["padNoteLabel"].setText(_translate("MainWindow", "Note"))
                    pad["padNoteComboBox"].setItemText(0, _translate("MainWindow", "C"))
                    pad["padNoteComboBox"].setItemText(1, _translate("MainWindow", "C♯"))
                    pad["padNoteComboBox"].setItemText(2, _translate("MainWindow", "D"))
                    pad["padNoteComboBox"].setItemText(3, _translate("MainWindow", "D♯"))
                    pad["padNoteComboBox"].setItemText(4, _translate("MainWindow", "E"))
                    pad["padNoteComboBox"].setItemText(5, _translate("MainWindow", "F"))
                    pad["padNoteComboBox"].setItemText(6, _translate("MainWindow", "F♯"))
                    pad["padNoteComboBox"].setItemText(7, _translate("MainWindow", "G"))
                    pad["padNoteComboBox"].setItemText(8, _translate("MainWindow", "G♯"))
                    pad["padNoteComboBox"].setItemText(9, _translate("MainWindow", "A"))
                    pad["padNoteComboBox"].setItemText(10, _translate("MainWindow", "A♯"))
                    pad["padNoteComboBox"].setItemText(11, _translate("MainWindow", "B"))
                    pad["padPCLabel"].setText(_translate("MainWindow", "PC"))

                    pad["padNoteComboBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Pad note")))
                    pad["padNoteSpinBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Pad octave")))
                    pad["padCCSpinBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Pad CC value")))
                    pad["padPCSpinBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Pad PC value")))
                    pad["padTypeComboBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Pad behaviour")))
            for knob in prog["knobs"]:
                knob["knobCCSpinBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Knob CC value")))
                knob["knobMinSpinBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Knob minimum value")))
                knob["knobMaxSpinBox"].setToolTip(self.get_tooltip(_translate("MainWindow", "Knob maximum value")))
            self.programmes.setTabText(self.programmes.indexOf(prog["prog1"]), _translate("MainWindow", "PROG") + " " + str(p_i+1))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuCopyTo.setTitle(_translate("MainWindow", "Copy to…"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        # self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save as…"))
        self.actionShowAutofill.setText(_translate("MainWindow", "Auto fill…"))
        # self.actionFactory_preset.setText(_translate("MainWindow", "Factory preset"))
        # self.actionCopyProgs[0].setText(_translate("MainWindow", "PROG"))
        for p_i, action in enumerate(self.actionCopyProgs):
            action.setText(_translate("MainWindow", "PROG ") + str(p_i + 1))
