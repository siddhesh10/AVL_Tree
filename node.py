class node(object):

    def __init__(self,data,parent):
        self.data=data
        self.leftchild=None
        self.rightchild=None
        self.balance=0
        self.parent=parent
