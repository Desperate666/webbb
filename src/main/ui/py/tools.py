import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QFileDialog
from pyqt5_plugins.examplebutton import QtWidgets


class TreeModel(QStandardItemModel):
    def __init__(self, parent=None):
        super(TreeModel, self).__init__(parent)

    def setTreeData(self, data):
        self.clear()
        root_item = self.invisibleRootItem()
        item1 = QStandardItem("网站")
        root_item.appendRow(item1)
        # 把两个元素添加到根目录下的一行
        for item in data:
            per_item = QStandardItem(item)
            per_item.setToolTip(item)  # 设置完整的网址为提示信息
            item1.appendRow(per_item)  # 子元素设置为根目录 再次添加
            per_item.setCheckable(True)
        item1.setCheckable(False)
        self.setHeaderData(0, Qt.Horizontal, '扫描数据')
    # 检测被选中的子项
    def getCheckedItems(self):
        checked_items = []
        root_item = self.invisibleRootItem()
        item1 = root_item.child(0)  # 获取网站节点
        for row in range(item1.rowCount()):
            child_item = item1.child(row)
            if child_item.checkState() == Qt.Checked:
                checked_items.append(child_item.text())
        return checked_items

class Tools():
    def __init__(self):
        self.model = None
    # def addFilesToTreeView(self, data, component):
    #     model = TreeModel()
    #     component.setModel(model)
    #     self.loadData(data, model)
    #     self.adjustTreeViewHeader(component)  # 调整树形控件的列宽适应内容宽度

    def addFilesToTreeView(self, data, component):
        self.model = TreeModel()
        component.setModel(self.model)
        self.loadData(data, self.model)
        self.adjustTreeViewHeader(component)  # 调整树形控件的列宽适应内容宽度

    def handleHeaderClicked(self):
        path = r''
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "选择文件夹", path)
        allfiles = self.get_files(folder_path)
        return allfiles

    def get_files(self, folder_path):
        # 在这里实现获取指定文件夹下的所有 PHP 文件的逻辑
        # 返回 PHP 文件的列表
        all_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith((".php",".py",".txt",'.log')):#可改
                    all_files.append(os.path.join(root, file))
        return all_files

    def adjustTreeViewHeader(self, component):
        component.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        component.header().setStretchLastSection(False)

    def loadData(self, data, model):
        model.setTreeData(data)

    def open_log_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None, "选择文件夹", r"D:\PyCharmTest\PyCharmPackets\Models\WebScannerProject\reference\pythonProject\src\log")
        print(folder_path)