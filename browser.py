#by Dinesh 



from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets  import *

import sys
import os


class AboutDialog(QDialog):
	
	def __init__(self, *args,**kwargs):
		super(AboutDialog,self).__init__(*args,**kwargs)
		
		QBtn = QDialogButtonBox.Ok
		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)
	
		layout = QVBoxLayout()
		title = QLabel("A simple Web Browser Devloped by Dinesh(DKm)")
		font = title.font()
		font.setPointSize(20)
		title.setFont(font)
		title.setAlignment(Qt.AlignHCenter)
		layout.addWidget(title)
		layout.addWidget(self.buttonBox)
		logo = QLabel()
		logo.setPixmap(QPixmap(os.path.join('icons','icon.png')))
		layout.addWidget(logo)
		self.setLayout(layout)
		n1 = QLabel("Version 1.0")
		n1.setAlignment(Qt.AlignHCenter)
		n2 =  QLabel("(c) Copyright 2018 Dinesh Mali Dkm.")
		n2.setAlignment(Qt.AlignHCenter)
		layout.addWidget(n1)
		layout.addWidget(n2)
	
class MainWindow(QMainWindow):

	def __init__(self, *args,**kwargs):
		super(MainWindow,self).__init__(*args,**kwargs)
		
		self.show()
		self.setWindowTitle("web broswer by DKm")
		self.setWindowIcon(QIcon(os.path.join('icons','icon.png')))
		self.browser =  QWebEngineView()
		self.browser.setUrl(QUrl("https://www.google.com"))
		self.setCentralWidget(self.browser)
		
		navtb = QToolBar("Navigation")
		navtb.setIconSize(QSize(16,16))
		self.addToolBar(navtb)
		
		back_btn = QAction( QIcon(os.path.join('icons','back')),"back",self)
		back_btn.setStatusTip("Back to previous page")
		back_btn.triggered.connect(self.browser.back)
		navtb.addAction(back_btn)


		next_btn = QAction( QIcon(os.path.join('icons','forward')),"forward",self)
		next_btn.setStatusTip("Back to Next page")
		next_btn.triggered.connect(self.browser.forward)
		navtb.addAction(next_btn)
		
		reload_btn = QAction( QIcon(os.path.join('icons','reload')),"reload",self)
		reload_btn.setStatusTip("reload the page")
		reload_btn.triggered.connect(self.browser.reload)
		navtb.addAction(reload_btn)
		
		home_btn = QAction( QIcon(os.path.join('icons','home')),"home",self)
		home_btn.setStatusTip("home page")
		home_btn.triggered.connect(self.navigate_home)
		navtb.addAction(home_btn)
		
	
		
		self.urlbar = QLineEdit()
		self.urlbar.returnPressed.connect(self.navigation_to_url)
		navtb.addSeparator()
		navtb.addWidget(self.urlbar)
		
		stop_btn = QAction( QIcon(os.path.join('icons','stop')),"stop",self)
		stop_btn.setStatusTip("stop loading the page")
		stop_btn.triggered.connect(self.browser.stop)
		navtb.addAction(stop_btn)
		
		self.browser.urlChanged.connect(self.update_urlbar)
		
		help_menu = self.menuBar().addMenu("&Help")
		about_action = QAction(QIcon(os.path.join('icons','about.png')),"About" ,self)
		about_action.setStatusTip("Find out more about")
		about_action.triggered.connect(self.about)
		help_menu.addAction(about_action)
		
		navigate_site_action = QAction(QIcon(os.path.join('icons','visit.png')),"Go to Home page",self)
		navigate_site_action.setStatusTip("Find out more ")
		navigate_site_action.triggered.connect(self.navigate_site)
		help_menu.addAction(navigate_site_action)
		

		
	def update_urlbar(self,q):
		
		self.urlbar.setText(q.toString())
		self.urlbar.setCursorPosition(0)
			
	def navigation_to_url(self):
		q = QUrl(self.urlbar.text())
		if q.scheme() == " ":
			q.setScheme("http")
		self.browser.setUrl(q)
	
	def navigate_home(self):
		self.browser.setUrl(QUrl("https://www.google.com"))
	
	def navigate_site(self):
		self.browser.setUrl(QUrl("https://thedkm.github.io/"))
	
	def about(self):
		dlg =AboutDialog()
		dlg.exec_()
	
app = QApplication(sys.argv)
app.setApplicationName("Browser by DKm")
app.setOrganizationName("Dkm")


window = MainWindow()
window.show()

app.exec_()