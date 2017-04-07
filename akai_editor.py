#!/usr/bin/env python3

# TODO
## get programs
## send programs
##     single
#     all
# get ram
# send ram
# interface
#     tabs for progs
#     autofill
# load/save config
#     single program
#     multi  programs
#     .mk2
#     mk1
#     human readable
# live update
# factory reset
# package
# PyPI?


import rtmidi
import time
from pprint import pprint

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.qt_ui import Ui_MainWindow

# [240, 71, 0, 38, 102, 0, 1, 1, 247]
midi_confg = [
 240,  # sysex start [240]
 71,  # [71]
 0,  # [0]
 38,  # [38]
 103,  # [103]
 0,  # [0]
 109,  # [109]

 1,  # programme [1,4]

 15,  # pad channel [0,15]
 14,  # key channel [0,15]

 3,  # key octave [0,8] (-4,4)

 1,  # arp ON [0=OFF; 1=ON] no effect on programmes...?
 5,  # arp mode [0=UP; 1=DOWN; 2=EXCLUSIVE; 3=INCLUSIVE; 4=ORDER; 5=RANDOM]
 5,  # arp time div [0=1/4; 1=1/4T;  2=1/8;  3=1/8T;  4=1/16;  5=1/16T;  6=1/32;  7=1/32T]
 0,  # arp clock [0=INTERNAL; 1=EXTERNAL]
 1,  # arp latch [0=OFF; 1=ON]
 4,  # arp swing [0=50%; 1=55%; 2=57%; 3=59%; 4=61%; 5=64%]
 3,  # arp taps [2,4]

 # The arpeggiator tempo is encoded using 2 bytes
 # the first one may be 0 or 1
 # if the first one is 0
 #    then the second one is in [30,127]
 # if the first one is 1
 #    then the second one is in [0,112] (128,240)
 0,  # arp tempo 0 [0,1]
 79,  # arp tempo 1 [30,127; 0,112]

 1,  # arp octave [0,3]

 2,  # x axis type [0=PITCHBEND; 1=CC1; 2=CC2]
 80,  # x axis L [0,127]
 81,  # x axis R [0,127]

 2,  # y axis type
 83,  # y axis D
 82,  # y axis U

 0,  # bA p1 NT [0,127]
 15,  # bA p1 PC [0,127]
 31,  # bA p1 CC [0,127]
 1,  # bA p1 TP [0=TOGGLE; 1=MOMENTARY]

 1,  # bA p2 NT
 16,  # bA p2 PC
 32,  # bA p2 CC
 1,  # bA p2 TP

 2,  # bA p3 NT
 17,  # bA p3 PC
 33,  # bA p3 CC
 1,  # bA p3 TP

 3,  # bA p4 NT
 18,  # bA p4 PC
 34,  # bA p4 CC
 1,  # bA p4 TP

 4,  # bA p5 NT
 19,  # bA p5 PC
 35,  # bA p5 CC
 1,  # bA p5 TP

 5,  # bA p6 NT
 20,  # bA p6 PC
 36,  # bA p6 CC
 1,  # bA p6 TP

 6,  # bA p7 NT
 21,  # bA p7 PC
 37,  # bA p7 CC
 1,  # bA p7 TP

 7,  # bA p8 NT
 22,  # bA p8 PC
 38,  # bA p8 CC
 1,  # bA p8 TP

 8,  # bB p1 NT
 23,  # bB p1 PC
 39,  # bB p1 CC
 0,  # bB p1 TP

 9,  # bB p2 NT
 24,  # bB p2 PC
 40,  # bB p2 CC
 0,  # bB p2 TP

 10,  # bB p3 NT
 25,  # bB p3 PC
 41,  # bB p3 CC
 0,  # bB p3 TP

 11,  # bB p4 NT
 26,  # bB p4 PC
 42,  # bB p4 CC
 0,  # bB p4 TP

 12,  # bB p5 NT
 27,  # bB p5 PC
 43,  # bB p5 CC
 0,  # bB p5 TP

 13,  # bB p6 NT
 28,  # bB p6 PC
 44,  # bB p6 CC
 0,  # bB p6 TP

 14,  # bB p7 NT
 29,  # bB p7 PC
 45,  # bB p7 CC
 0,  # bB p7 TP

 15,  # bB p8 NT
 30,  # bB p8 PC
 46,  # bB p8 CC
 0,  # bB p8 TP

 47,  # k1 CC [0,127]
 63,  # k1 LO [0,127]
 71,  # k1 HI [0,127]

 48,  # k2 CC
 64,  # k2 LO
 72,  # k2 HI

 49,  # k3 CC
 65,  # k3 LO
 73,  # k3 HI

 50,  # k4 CC
 66,  # k4 LO
 74,  # k4 HI

 59,  # k5 CC
 67,  # k5 LO
 75,  # k5 HI

 60,  # k6 CC
 68,  # k6 LO
 76,  # k6 HI

 61,  # k7 CC
 69,  # k7 LO
 77,  # k7 HI

 62,  # k8 CC
 70,  # k8 LO
 78,  # k8 HI

 13,  # key transpose [0,24]
 247  # sysex end [247]
]  #

class Akai_MPK_Mini(Ui_MainWindow):

    GET_CONFIG = [240, 71, 0, 38, 102, 0, 1, 1, 247]  #[0xf0, 0x47, 0x00, 0x26, 0x66, 0x00, 0x01, 0x02, 0xf7]

    def __init__(self):
        self.mo = rtmidi.MidiOut()
        self.mo.open_port(1)

        self.mi = rtmidi.MidiIn()
        self.mi.open_port(1)
        self.mi.ignore_types(sysex=False)

    def get_config(self, i):
        message = [[]]
        self.mo.send_message(self.GET_CONFIG)
        time.sleep(0.05)
        while message is None or len(message[0]) != 117:
            message = self.mi.get_message()
        print(message)

        print(self.progs[0]["knobs"][0]["knobCCSpinBox"].setValue(20))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Akai_MPK_Mini()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
