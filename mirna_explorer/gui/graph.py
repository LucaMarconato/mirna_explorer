from PySide2.QtWidgets import (QLabel, QWidget, QMainWindow, QApplication, QAction, 
                               QFileDialog, QGridLayout, QVBoxLayout, QPushButton)

class Graph(QWidget):
    
    def __init__(self, parent):        
        super(Graph, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.button1 = QPushButton("Button 1")
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2")
        self.layout.addWidget(self.button2)

        self.setLayout(self.layout)
