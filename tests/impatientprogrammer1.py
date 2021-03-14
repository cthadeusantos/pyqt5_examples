import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTableView, QTreeWidget, QTreeWidgetItem, QVBoxLayout)

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout(window)

tw = QTreeWidget()
tw.setHeaderLabels(['name', 'Cost ($)'])
cg = QTreeWidgetItem(tw, ['carrots', '0.99'])
c1 = QTreeWidgetItem(cg, ['carrot', '0.33'])

layout.addWidget(tw)
window.show()

sys.exit(app.exec_())