# lineedit.py
# IMport necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton)
from PyQt5.QtCore import Qt

class EntryWindow(QWidget):     # Inherits QWidget
    def __init__(self):
        super().__init__()  # Initialize which calls constructor for QWidget
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        :return:
        """
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('QLineEdit Widget')
        self.displayWidgets()
        self.show()

    def displayWidgets(self):
        """
        Setup the QLineEdit and other widgets
        :return:
        """
        # Create name label and line edit widgets
        QLabel("Please enter your name below.", self).move(100, 10)
        name_label = QLabel("Name:", self)
        name_label.move(70, 50)

        self.name_entry = QLineEdit(self)
        self.name_entry.setAlignment(Qt.AlignLeft)  # The default alignment is AlignLeft
        self.name_entry.move(130, 50)
        self.name_entry.resize(200, 20)     # change size of entry field

        self.clear_button = QPushButton('Clear', self)
        self.clear_button.clicked.connect(self.clearEntries)
        self.clear_button.move(160, 110)

    def clearEntries(self):
        """
        If Button is pressed, clear the line edit input field
        :return:
        """
        sender = self.sender()
        if sender.text() == 'Clear':
            self.name_entry.clear()

#Run Program
# if __name__ == '__main__':
app = QApplication(sys.argv)
window = EntryWindow()
sys.exit(app.exec_())


