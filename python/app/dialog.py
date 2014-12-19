# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
import os
import sys
import threading

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog

wtd_pipeline = sgtk.platform.import_framework("tk-framework-wtd", "pipeline")
# wtd_maya = sgtk.platform.import_framework("tk-framework-wtd", "maya")

def show_dialog(app_instance):
	"""
	Shows the main dialog window.
	"""
	# in order to handle UIs seamlessly, each toolkit engine has methods for launching
	# different types of windows. By using these methods, your windows will be correctly
	# decorated and handled in a consistent fashion by the system. 
	
	# we pass the dialog class to this method and leave the actual construction
	# to be carried out by toolkit.
	app_instance.engine.show_dialog("Shotloader...", app_instance, AppDialog)
	


class AppDialog(QtGui.QWidget):
	"""
	Main application dialog window
	"""
	
	def __init__(self):
		"""
		Constructor
		"""
		# first, call the base class and let it do its thing.
		QtGui.QWidget.__init__(self)
		
		# now load in the UI that was created in the UI designer
		self.ui = Ui_Dialog() 
		self.ui.setupUi(self)
		
		# most of the useful accessors are available through the Application class instance
		# it is often handy to keep a reference to this. You can get it via the following method:
		self._app = sgtk.platform.current_bundle()
		
		# via the self._app handle we can for example access:
		# - The engine, via self._app.engine
		# - A Shotgun API instance, via self._app.shotgun
		# - A tk API instance, via self._app.tk 
		
		# lastly, set up our very basic UI
		print dir(self._app.context.sgtk.shotgun)
		print self._app.context.project
		# self.ui.context.setText("Current Context: %s" % self._app.context)
		
		self.shotlist = self.loadShots()
		# print self.shotlist
		
	def loadValues(self):
		print "Todo: load positionlist"
		self.poslist = None
		self.currenctShot = str(self.ui.context.getText())
		
		if self.currenctShot != "" and self.currenctShot in self.shotlist:
			print "go to next step with shot %s!" %self.currenctShot
		else:
			print "No existing shot found in shotgun"
			return None
			
		self.poslist = wtd_pipeline.Positionlist()

	def createCheckboxes(self):
		print "Todo: create checkboxes"
		
	def loadShots(self):
		current_project = self._app.context.project
		fields = ['id', 'code']
		filters = [
			['project','is',current_project]
			]
		shots = self._app.context.sgtk.shotgun.find("Shot",filters,fields)
		adjusted_shotlist = {}
		for s in shots:
			adjusted_shotlist[s["code"].replace("_","-").replace("q","").replace("s","")] = s
		return adjusted_shotlist
		
	def checkShotExistance(self):
		print "Todo: check if shot exists"
		
	