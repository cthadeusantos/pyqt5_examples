# How to get an current object (or data) when clicked a tree item

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

class Model(QStandardItemModel):

    def __init__(self, inputData):
        QStandardItemModel.__init__(self)

        # inputData
        # [ {"type": "Fruit", "objects": ["Apple", "Banana"]} ]
        d = inputData[0]  # Fruit
        item = QStandardItem(d["type"])
        child = QStandardItem(d["objects"][0])  # Apple
        item.appendRow(child)
        child = QStandardItem(d["objects"][1])  # Banana
        item.appendRow(child)
        self.setItem(0, 0, item)

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("ItemView QTreeView")
        self.setFixedWidth(210)
        self.setFixedHeight(150)

        # Data
        data = [
            {"type": "Fruit", "objects": ["Apple", "Banana"]}
        ]
        # QTreeView
        self.treeView = QTreeView(self)
        self.treeView.doubleClicked.connect(self.test)

        # Model
        self.model = Model(data)
        self.treeView.setModel(self.model)

    def test(self, selectedItem:QModelIndex):
        text = self.model.data(selectedItem)
        print(text)
        ### I want to make & get "Banana" Object (or data), not a text ###

# if __name__ == "__main__":
app = QApplication(sys.argv)
form = Form()
form.show()
exit(app.exec_())