#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from uic/phrasepage.ui on Thu Jan  7 13:58:13 2010
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

class Ui_PhrasePage(object):
    def setupUi(self, PhrasePage):
        PhrasePage.setObjectName("PhrasePage")
        PhrasePage.resize(540, 602)
        self.verticalLayout_2 = QtGui.QVBoxLayout(PhrasePage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.phraseText = KTextEdit(PhrasePage)
        self.phraseText.setTabChangesFocus(True)
        self.phraseText.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.phraseText.setAcceptRichText(False)
        self.phraseText.setObjectName("phraseText")
        self.verticalLayout_2.addWidget(self.phraseText)
        self.settingsGroupBox = QtGui.QGroupBox(PhrasePage)
        self.settingsGroupBox.setObjectName("settingsGroupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.settingsGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.promptCheckbox = QtGui.QCheckBox(self.settingsGroupBox)
        self.promptCheckbox.setObjectName("promptCheckbox")
        self.verticalLayout.addWidget(self.promptCheckbox)
        self.showInTrayCheckbox = QtGui.QCheckBox(self.settingsGroupBox)
        self.showInTrayCheckbox.setObjectName("showInTrayCheckbox")
        self.verticalLayout.addWidget(self.showInTrayCheckbox)
        self.kseparator = KSeparator(self.settingsGroupBox)
        self.kseparator.setObjectName("kseparator")
        self.verticalLayout.addWidget(self.kseparator)
        self.settingsWidget = SettingsWidget(self.settingsGroupBox)
        self.settingsWidget.setObjectName("settingsWidget")
        self.verticalLayout.addWidget(self.settingsWidget)
        self.verticalLayout_2.addWidget(self.settingsGroupBox)

        self.retranslateUi(PhrasePage)
        QtCore.QMetaObject.connectSlotsByName(PhrasePage)

    def retranslateUi(self, PhrasePage):
        PhrasePage.setWindowTitle(kdecore.i18n("Form"))
        self.settingsGroupBox.setTitle(kdecore.i18n("Phrase Settings"))
        self.promptCheckbox.setText(kdecore.i18n("Always prompt before pasting this phrase"))
        self.showInTrayCheckbox.setText(kdecore.i18n("Show in tray menu"))

from PyKDE4.kdeui import KSeparator, KTextEdit
from configwindow import SettingsWidget
