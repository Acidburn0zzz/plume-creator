'''
Created on 26 may 2015

@author:  Cyril Jacquet
'''

from PyQt5.QtCore import QSortFilterProxyModel, QByteArray
from gui.models.sheet_tree_model import SheetTreeModel



class WriteTreeProxyModel(QSortFilterProxyModel):

    '''
    WriteTreeProxyModel
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''

        super(WriteTreeProxyModel, self).__init__(parent=None)

    def node_from_index(self, index):
        return self.sourceModel().node_from_index(self.mapToSource(index))

    @property
    def id_of_last_created_node(self):
        return self.sourceModel().id_of_last_created_node

    def find_index_from_id(self, id_):
        index = self.sourceModel().find_index_from_id(id_)
        print(index.isValid())
        return self.mapFromSource(index)

    def insert_child_node(self, parent_index):
        return self.sourceModel().insert_child_node(self.mapToSource(parent_index))

    def insert_node_after(self, parent_index):
        return self.sourceModel().insert_node_by(self.mapToSource(parent_index))

    def remove_node(self, index):
        return self.sourceModel().remove_node(self.mapToSource(index))

    def filterAcceptsRow(self, p_int, index):
        if index.data(self.sourceModel().DeletedRole) == 1:
            return False
        else:
            return QSortFilterProxyModel.filterAcceptsRow(self, p_int, index)

    def roleNames(self):
        roles = {}
        roles[SheetTreeModel.IdRole] = QByteArray().append("sheet_id")
        roles[SheetTreeModel.TitleRole] = QByteArray().append("sheet_title")
        roles[SheetTreeModel.ContentRole] = QByteArray().append("sheet_content")
        return roles