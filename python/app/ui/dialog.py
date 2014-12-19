# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(331, 291)
		Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
		self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 311, 181))
		self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
		self.layout_checkboxes = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
		self.layout_checkboxes.setContentsMargins(6, -1, -1, -1)
		self.layout_checkboxes.setObjectName("layout_checkboxes")
		self.checkBox_specimen = QtGui.QCheckBox(self.verticalLayoutWidget_2)
		self.checkBox_specimen.setObjectName("checkBox_specimen")
		self.layout_checkboxes.addWidget(self.checkBox_specimen)
		self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 31))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.shot_label = QtGui.QLabel(self.horizontalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.shot_label.setFont(font)
		self.shot_label.setObjectName("shot_label")
		self.horizontalLayout.addWidget(self.shot_label)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.shotname = QtGui.QLineEdit(self.horizontalLayoutWidget)
		self.shotname.setMinimumSize(QtCore.QSize(150, 0))
		self.shotname.setMaximumSize(QtCore.QSize(150, 16777215))
		self.shotname.setStyleSheet("border-width: 1px; \n"
			"background-image: url(:/res/search.png);\n"
			"background-repeat: no-repeat;\n"
			"background-position: center left;\n"
			"border-style: inset; \n"
			"border-color: #535353; \n"
			"border-radius: 9px; \n"
			"padding-left: 15px")
		self.shotname.setObjectName("shotname")
		self.horizontalLayout.addWidget(self.shotname)
		self.lbl_extraInfo = QtGui.QLabel(self.horizontalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(7)
		self.lbl_extraInfo.setFont(font)
		self.lbl_extraInfo.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.lbl_extraInfo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.lbl_extraInfo.setObjectName("lbl_extraInfo")
		self.horizontalLayout.addWidget(self.lbl_extraInfo)
		self.Line = QtGui.QFrame(Dialog)
		self.Line.setGeometry(QtCore.QRect(10, 40, 420, 16))
		self.Line.setFrameShape(QtGui.QFrame.HLine)
		self.Line.setFrameShadow(QtGui.QFrame.Sunken)
		self.Line.setObjectName("Line")
		self.build_btn = QtGui.QPushButton(Dialog)
		self.build_btn.setGeometry(QtCore.QRect(10, 250, 420, 31))
		self.build_btn.setObjectName("build_btn")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
		self.checkBox_specimen.setText(QtGui.QApplication.translate("Dialog", "Select all", None, QtGui.QApplication.UnicodeUTF8))
		self.shot_label.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:large;\">Load shot</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
		self.lbl_extraInfo.setText(QtGui.QApplication.translate("Dialog", "(001-001)", None, QtGui.QApplication.UnicodeUTF8))
		self.build_btn.setText(QtGui.QApplication.translate("Dialog", "Build shot", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
