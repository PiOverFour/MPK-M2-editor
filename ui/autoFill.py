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


class Ui_autoFill(QtWidgets.QMainWindow):

    SCALES = [
        [0, 1, 2, 3, 4, 5,  6,  7],  # chromatic
        [0, 2, 4, 5, 7, 9, 11, 12],  # major
        [0, 2, 3, 5, 7, 8, 10, 12],  # minor
        [0, 2, 4, 5, 7, 8, 11, 12],  # harmonic minor
        [0, 2, 3, 5, 7, 9, 10, 12],  # dorian
        [0, 1, 3, 5, 7, 8, 10, 12],  # phrygian
        [0, 2, 4, 6, 7, 9, 11, 12],  # lydian
        [0, 2, 4, 5, 7, 9, 10, 12],  # myxolidian
        [0, 1, 3, 5, 6, 8, 10, 12],  # locrian
    ]

    def apply_autofill_knobs(self):
        mw = self.main_window
        p_from = mw.get_active_tab_index()
        conf = mw.get_tab_programme(p_from)

        # .currentIndex()
        # .checkState()
        # .value()
        do_values = self.knobsCCStartCheckBox.checkState()
        do_min = self.knobsCCMinCheckBox.checkState()
        do_max = self.knobsCCMaxCheckBox.checkState()
        if do_values:
            start_value = self.knobsCCStartSpinBox.value()
            direction = self.knobsCCDirectionComboBox.currentIndex()
            direction = 1 if direction == 0 else -1
            for i in range(8):
                conf[91 + 3*i] = start_value + i*direction
        if do_min:
            min = self.knobsMinSpinBox.value()
            for i in range(8):
                conf[92 + 3*i] = min

        if do_max:
            max = self.knobsMaxSpinBox.value()
            for i in range(8):
                conf[93 + 3*i] = max

        mw.fill_tab(conf, p_from)

    def apply_autofill_programme(self, programme):
        mw = self.main_window
        p_from = mw.get_active_tab_index()
        conf = mw.get_tab_programme(p_from)

        programme = 0 if programme == 'A' else 32

        do_notes = self.padsNoteStartCheckBox.checkState()
        do_PC = self.padsPCStartCheckBox.checkState()
        do_CC = self.padsCCStartCheckBox.checkState()
        do_CC_type = self.padsCCTypeCheckBox.checkState()
        if do_notes:
            scale = self.padsNoteScaleComboBox.currentIndex()
            direction = self.padsNoteDirectionComboBox.currentIndex()
            start_note = self.padsNoteComboBox.currentIndex()
            octave = self.padsNoteSpinBox.value()
            values = self.SCALES[scale]

            start_note = start_note + (octave+1) * 12
            if direction:
                values.reverse()
                values = [n - values[0] for n in values]
            values = [n + start_note for n in values]

            for i, val in enumerate(values):
                conf[27 + 4*i + programme] = val

        if do_PC:
            pc = self.padsPCStartSpinBox.value()
            pc_direction = self.padsPCDirectionComboBox.currentIndex()
            pc_direction = 1 if pc_direction == 0 else -1
            for i in range(8):
                conf[28 + 4*i + programme] = pc + i*pc_direction

        if do_CC:
            cc = self.padsCCStartSpinBox.value()
            cc_direction = self.padsCCDirectionComboBox.currentIndex()
            cc_direction = 1 if cc_direction == 0 else -1
            for i in range(8):
                conf[29 + 4*i + programme] = cc + i*cc_direction

        if do_CC_type:
            cc_type = self.padsCCTypeComboBox.currentIndex()
            for i in range(8):
                conf[30 + 4*i + programme] = cc_type

        mw.fill_tab(conf, p_from)

    def setupUi(self, autoFill):
        autoFill.setObjectName("autoFill")
        autoFill.resize(400, 200)
        self.autoFillCentralwidget = QtWidgets.QWidget(autoFill)
        self.autoFillCentralwidget.setObjectName("autoFillCentralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.autoFillCentralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.padsGroupBox = QtWidgets.QGroupBox(self.autoFillCentralwidget)
        self.padsGroupBox.setObjectName("padsGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.padsGroupBox)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.padsSettings = QtWidgets.QGridLayout()
        self.padsSettings.setObjectName("padsSettings")
        self.padsPCStartCheckBox = QtWidgets.QCheckBox(self.padsGroupBox)
        self.padsPCStartCheckBox.setObjectName("padsPCStartCheckBox")
        self.padsSettings.addWidget(self.padsPCStartCheckBox, 1, 0, 1, 1)
        self.padsCCTypeCheckBox = QtWidgets.QCheckBox(self.padsGroupBox)
        self.padsCCTypeCheckBox.setObjectName("padsCCTypeCheckBox")
        self.padsSettings.addWidget(self.padsCCTypeCheckBox, 3, 0, 1, 1)
        self.padsNoteStartCheckBox = QtWidgets.QCheckBox(self.padsGroupBox)
        self.padsNoteStartCheckBox.setObjectName("padsNoteStartCheckBox")
        self.padsSettings.addWidget(self.padsNoteStartCheckBox, 0, 0, 1, 1)
        self.padsCCStartCheckBox = QtWidgets.QCheckBox(self.padsGroupBox)
        self.padsCCStartCheckBox.setObjectName("padsCCStartCheckBox")
        self.padsSettings.addWidget(self.padsCCStartCheckBox, 2, 0, 1, 1)
        self.padsNoteGridLayout = QtWidgets.QGridLayout()
        self.padsNoteGridLayout.setHorizontalSpacing(0)
        self.padsNoteGridLayout.setObjectName("padsNoteGridLayout")
        self.padsNoteSpinBox = QtWidgets.QSpinBox(self.padsGroupBox)
        self.padsNoteSpinBox.setMinimum(-1)
        self.padsNoteSpinBox.setMaximum(9)
        self.padsNoteSpinBox.setProperty("value", 4)
        self.padsNoteSpinBox.setObjectName("padsNoteSpinBox")
        self.padsNoteGridLayout.addWidget(self.padsNoteSpinBox, 1, 1, 1, 1)
        self.padsNoteComboBox = QtWidgets.QComboBox(self.padsGroupBox)
        self.padsNoteComboBox.setObjectName("padsNoteComboBox")
        self.padsNoteComboBox.addItem("")
        self.padsNoteComboBox.addItem("")
        self.padsNoteComboBox.addItem("")
        self.padsNoteComboBox.addItem("")
        self.padsNoteComboBox.addItem("")
        self.padsNoteComboBox.addItem("")
        self.padsNoteComboBox.addItem("")
        self.padsNoteComboBox.addItem("")
        self.padsNoteComboBox.addItem("")
        self.padsNoteComboBox.addItem("")
        self.padsNoteComboBox.addItem("")
        self.padsNoteComboBox.addItem("")
        self.padsNoteGridLayout.addWidget(self.padsNoteComboBox, 1, 0, 1, 1)
        self.padsNoteDirectionComboBox = QtWidgets.QComboBox(self.padsGroupBox)
        self.padsNoteDirectionComboBox.setObjectName("padsNoteDirectionComboBox")
        self.padsNoteDirectionComboBox.addItem("")
        self.padsNoteDirectionComboBox.addItem("")
        self.padsNoteGridLayout.addWidget(self.padsNoteDirectionComboBox, 0, 1, 1, 1)
        self.padsNoteScaleComboBox = QtWidgets.QComboBox(self.padsGroupBox)
        self.padsNoteScaleComboBox.setObjectName("padsNoteScaleComboBox")
        self.padsNoteScaleComboBox.addItem("")
        self.padsNoteScaleComboBox.addItem("")
        self.padsNoteScaleComboBox.addItem("")
        self.padsNoteScaleComboBox.addItem("")
        self.padsNoteScaleComboBox.addItem("")
        self.padsNoteScaleComboBox.addItem("")
        self.padsNoteScaleComboBox.addItem("")
        self.padsNoteScaleComboBox.addItem("")
        self.padsNoteScaleComboBox.addItem("")
        self.padsNoteGridLayout.addWidget(self.padsNoteScaleComboBox, 0, 0, 1, 1)
        self.padsSettings.addLayout(self.padsNoteGridLayout, 0, 1, 1, 1)
        self.padsPCHorizontalLayout = QtWidgets.QHBoxLayout()
        self.padsPCHorizontalLayout.setSpacing(0)
        self.padsPCHorizontalLayout.setObjectName("padsPCHorizontalLayout")
        self.padsPCStartSpinBox = QtWidgets.QSpinBox(self.padsGroupBox)
        self.padsPCStartSpinBox.setMaximum(127)
        self.padsPCStartSpinBox.setObjectName("padsPCStartSpinBox")
        self.padsPCHorizontalLayout.addWidget(self.padsPCStartSpinBox)
        self.padsPCDirectionComboBox = QtWidgets.QComboBox(self.padsGroupBox)
        self.padsPCDirectionComboBox.setObjectName("padsPCDirectionComboBox")
        self.padsPCDirectionComboBox.addItem("")
        self.padsPCDirectionComboBox.addItem("")
        self.padsPCHorizontalLayout.addWidget(self.padsPCDirectionComboBox)
        self.padsSettings.addLayout(self.padsPCHorizontalLayout, 1, 1, 1, 1)
        self.padsCCHorizontalLayout = QtWidgets.QHBoxLayout()
        self.padsCCHorizontalLayout.setSpacing(0)
        self.padsCCHorizontalLayout.setObjectName("padsCCHorizontalLayout")
        self.padsCCStartSpinBox = QtWidgets.QSpinBox(self.padsGroupBox)
        self.padsCCStartSpinBox.setMaximum(127)
        self.padsCCStartSpinBox.setObjectName("padsCCStartSpinBox")
        self.padsCCHorizontalLayout.addWidget(self.padsCCStartSpinBox)
        self.padsCCDirectionComboBox = QtWidgets.QComboBox(self.padsGroupBox)
        self.padsCCDirectionComboBox.setObjectName("padsCCDirectionComboBox")
        self.padsCCDirectionComboBox.addItem("")
        self.padsCCDirectionComboBox.addItem("")
        self.padsCCHorizontalLayout.addWidget(self.padsCCDirectionComboBox)
        self.padsSettings.addLayout(self.padsCCHorizontalLayout, 2, 1, 1, 1)
        self.padsCCTypeComboBox = QtWidgets.QComboBox(self.padsGroupBox)
        self.padsCCTypeComboBox.setObjectName("padsCCTypeComboBox")
        self.padsCCTypeComboBox.addItem("")
        self.padsCCTypeComboBox.addItem("")
        self.padsSettings.addWidget(self.padsCCTypeComboBox, 3, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.padsSettings)
        self.padsApplyHorizontalLayout = QtWidgets.QHBoxLayout()
        self.padsApplyHorizontalLayout.setObjectName("padsApplyHorizontalLayout")
        self.padsApplylabel = QtWidgets.QLabel(self.padsGroupBox)
        self.padsApplylabel.setObjectName("padsApplylabel")
        self.padsApplyHorizontalLayout.addWidget(self.padsApplylabel)
        self.padsApplyAPushButton = QtWidgets.QPushButton(self.padsGroupBox)
        self.padsApplyAPushButton.setObjectName("padsApplyAPushButton")
        self.padsApplyAPushButton.setStyleSheet("background-color: green")
        self.padsApplyAPushButton.clicked.connect(partial(self.apply_autofill_programme, "A"))

        self.padsApplyHorizontalLayout.addWidget(self.padsApplyAPushButton)
        self.padsApplyBPushButton = QtWidgets.QPushButton(self.padsGroupBox)
        self.padsApplyBPushButton.setObjectName("padsApplyBPushButton")
        self.padsApplyBPushButton.setStyleSheet("background-color: red")
        self.padsApplyBPushButton.clicked.connect(partial(self.apply_autofill_programme, "B"))

        self.padsApplyHorizontalLayout.addWidget(self.padsApplyBPushButton)
        self.verticalLayout_5.addLayout(self.padsApplyHorizontalLayout)
        self.verticalLayout_5.setStretch(0, 6)
        self.verticalLayout_5.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.padsGroupBox)
        self.knobsGroupBox = QtWidgets.QGroupBox(self.autoFillCentralwidget)
        self.knobsGroupBox.setObjectName("knobsGroupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.knobsGroupBox)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.knobsMinSpinBox = QtWidgets.QSpinBox(self.knobsGroupBox)
        self.knobsMinSpinBox.setMaximum(127)
        self.knobsMinSpinBox.setObjectName("knobsMinSpinBox")
        self.gridLayout.addWidget(self.knobsMinSpinBox, 1, 1, 1, 1)
        self.knobsCCStartCheckBox = QtWidgets.QCheckBox(self.knobsGroupBox)
        self.knobsCCStartCheckBox.setObjectName("knobsCCStartCheckBox")
        self.gridLayout.addWidget(self.knobsCCStartCheckBox, 0, 0, 1, 1)
        self.knobsMaxSpinBox = QtWidgets.QSpinBox(self.knobsGroupBox)
        self.knobsMaxSpinBox.setMaximum(127)
        self.knobsMaxSpinBox.setProperty("value", 127)
        self.knobsMaxSpinBox.setObjectName("knobsMaxSpinBox")
        self.gridLayout.addWidget(self.knobsMaxSpinBox, 2, 1, 1, 1)
        self.knobsCCMaxCheckBox = QtWidgets.QCheckBox(self.knobsGroupBox)
        self.knobsCCMaxCheckBox.setObjectName("knobsCCMaxCheckBox")
        self.gridLayout.addWidget(self.knobsCCMaxCheckBox, 2, 0, 1, 1)
        self.knobsCCStartHorizontalLayout = QtWidgets.QHBoxLayout()
        self.knobsCCStartHorizontalLayout.setSpacing(0)
        self.knobsCCStartHorizontalLayout.setObjectName("knobsCCStartHorizontalLayout")
        self.knobsCCStartSpinBox = QtWidgets.QSpinBox(self.knobsGroupBox)
        self.knobsCCStartSpinBox.setMaximum(127)
        self.knobsCCStartSpinBox.setObjectName("knobsCCStartSpinBox")
        self.knobsCCStartHorizontalLayout.addWidget(self.knobsCCStartSpinBox)
        self.knobsCCDirectionComboBox = QtWidgets.QComboBox(self.knobsGroupBox)
        self.knobsCCDirectionComboBox.setObjectName("knobsCCDirectionComboBox")
        self.knobsCCDirectionComboBox.addItem("")
        self.knobsCCDirectionComboBox.addItem("")
        self.knobsCCStartHorizontalLayout.addWidget(self.knobsCCDirectionComboBox)
        self.gridLayout.addLayout(self.knobsCCStartHorizontalLayout, 0, 1, 1, 1)
        self.knobsCCMinCheckBox = QtWidgets.QCheckBox(self.knobsGroupBox)
        self.knobsCCMinCheckBox.setObjectName("knobsCCMinCheckBox")
        self.gridLayout.addWidget(self.knobsCCMinCheckBox, 1, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)

        self.knobsApplyKnobsPushButton = QtWidgets.QPushButton(self.knobsGroupBox)
        self.knobsApplyKnobsPushButton.setObjectName("knobsApplyKnobsPushButton")
        self.knobsApplyKnobsPushButton.clicked.connect(self.apply_autofill_knobs)

        self.verticalLayout_6.addWidget(self.knobsApplyKnobsPushButton, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addWidget(self.knobsGroupBox)

        autoFill.setCentralWidget(self.autoFillCentralwidget)

        self.retranslateUi(autoFill)
        QtCore.QMetaObject.connectSlotsByName(autoFill)

    def retranslateUi(self, autoFill):
        _translate = QtCore.QCoreApplication.translate
        autoFill.setWindowTitle(_translate("autoFill", "Auto Fill"))
        self.padsGroupBox.setTitle(_translate("autoFill", "Pads"))
        self.padsPCStartCheckBox.setText(_translate("autoFill", "PC start"))
        self.padsCCTypeCheckBox.setText(_translate("autoFill", "CC type"))
        self.padsNoteStartCheckBox.setText(_translate("autoFill", "Note start"))
        self.padsCCStartCheckBox.setText(_translate("autoFill", "CC start"))
        self.padsNoteComboBox.setItemText(0, _translate("autoFill", "C"))
        self.padsNoteComboBox.setItemText(1, _translate("autoFill", "C#"))
        self.padsNoteComboBox.setItemText(2, _translate("autoFill", "D"))
        self.padsNoteComboBox.setItemText(3, _translate("autoFill", "D#"))
        self.padsNoteComboBox.setItemText(4, _translate("autoFill", "E"))
        self.padsNoteComboBox.setItemText(5, _translate("autoFill", "F"))
        self.padsNoteComboBox.setItemText(6, _translate("autoFill", "F#"))
        self.padsNoteComboBox.setItemText(7, _translate("autoFill", "G"))
        self.padsNoteComboBox.setItemText(8, _translate("autoFill", "G#"))
        self.padsNoteComboBox.setItemText(9, _translate("autoFill", "A"))
        self.padsNoteComboBox.setItemText(10, _translate("autoFill", "A#"))
        self.padsNoteComboBox.setItemText(11, _translate("autoFill", "B"))
        self.padsNoteDirectionComboBox.setItemText(0, _translate("autoFill", "Up"))
        self.padsNoteDirectionComboBox.setItemText(1, _translate("autoFill", "Down"))
        self.padsNoteScaleComboBox.setItemText(0, _translate("autoFill", "Chromatic"))
        self.padsNoteScaleComboBox.setItemText(1, _translate("autoFill", "Major"))
        self.padsNoteScaleComboBox.setItemText(2, _translate("autoFill", "Minor"))
        self.padsNoteScaleComboBox.setItemText(3, _translate("autoFill", "Harmonic"))
        self.padsNoteScaleComboBox.setItemText(4, _translate("autoFill", "Dorian"))
        self.padsNoteScaleComboBox.setItemText(5, _translate("autoFill", "Phrygian"))
        self.padsNoteScaleComboBox.setItemText(6, _translate("autoFill", "Lydian"))
        self.padsNoteScaleComboBox.setItemText(7, _translate("autoFill", "Myxolidian"))
        self.padsNoteScaleComboBox.setItemText(8, _translate("autoFill", "Locrian"))
        self.padsPCDirectionComboBox.setItemText(0, _translate("autoFill", "Up"))
        self.padsPCDirectionComboBox.setItemText(1, _translate("autoFill", "Down"))
        self.padsCCDirectionComboBox.setItemText(0, _translate("autoFill", "Up"))
        self.padsCCDirectionComboBox.setItemText(1, _translate("autoFill", "Down"))
        self.padsCCTypeComboBox.setItemText(0, _translate("autoFill", "Momentary"))
        self.padsCCTypeComboBox.setItemText(1, _translate("autoFill", "Toggle"))
        self.padsApplylabel.setText(_translate("autoFill", "  Apply to..."))
        self.padsApplyAPushButton.setText(_translate("autoFill", "A", "program"))
        self.padsApplyBPushButton.setText(_translate("autoFill", "B", "program"))
        self.knobsGroupBox.setTitle(_translate("autoFill", "Knobs"))
        self.knobsCCStartCheckBox.setText(_translate("autoFill", "CC start"))
        self.knobsCCMaxCheckBox.setText(_translate("autoFill", "Set max"))
        self.knobsCCDirectionComboBox.setItemText(0, _translate("autoFill", "Up"))
        self.knobsCCDirectionComboBox.setItemText(1, _translate("autoFill", "Down"))
        self.knobsCCMinCheckBox.setText(_translate("autoFill", "Set min"))
        self.knobsApplyKnobsPushButton.setText(_translate("autoFill", "Apply to knobs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    autoFill = QtWidgets.QMainWindow()
    ui = Ui_autoFill()
    ui.setupUi(autoFill)
    autoFill.show()
    sys.exit(app.exec_())
