from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args , **kwargs)
        self.setGeometry(QRect(0,0,1200,800))
        self.setWindowTitle("My Browser")
        
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)
        
        self.browser =QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com.tr/"))
        
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        
        self.back_button = QAction("Back", self)
        self.back_button.setStatusTip("Back to previous page")
        self.back_button.triggered.connect(self.browser.back)
        self.toolbar.addAction(self.back_button)
        
        self.setCentralWidget(self.browser)
        self.addToolBar(Qt.BottomToolBarArea,QToolBar("Navigation"))
        self.toolbar.addWidget(self.urlbar)


        self.go_button = QAction ("Go", self)
        self.go_button.setStatusTip ("Go to a web page") 
        self.go_button.triggered.connect(self.navigate_to_url) 
        self.toolbar.addAction (self.go_button)
        
        self.show()
        
def navigate_to_url(self): 
    q = self.urlbar.text() 
    if q.startswith("http://" ) :
        url = q
    else:
      url = "http://" + q 
      self.browser.setUrl(QUrl(url))
      
app = QApplication(sys.argv) 
window = MainWindow()
app.exec_()

