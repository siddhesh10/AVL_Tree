import sys
sys.path.insert(0, 'C:/Users/sidd/Desktop/AVL_Tree/')
import node

class avl_tree(object):

    def __init__(self):
        self.root=None

    def insert_node(self,data):
        new_node=node.node(data,None)

        if self.root==None:
            self.root=new_node
        else:
            current_node=self.root
            while True:
                if data<current_node.data:
                    if current_node.leftchild==None:
                        current_node.leftchild=new_node
                        new_node.parent=current_node
                        self.updateBalance(current_node.leftchild)
                        break
                    else:
                        current_node=current_node.leftchild
                else:
                    if current_node.rightchild==None:

                        current_node.rightchild=new_node
                        new_node.parent=current_node
                        self.updateBalance(current_node.rightchild)
                        break
                    else:
                        current_node=current_node.rightchild

    def updateBalance(self,node):

        node.balance=self.height_AVL(node.leftchild)-self.height_AVL(node.rightchild)
        if node.balance > 1 or node.balance < -1:
            self.rebalance(node)
            return
        if node.parent != None:

            if node.parent.leftchild==node:
                node.parent.balance += 1
            elif node.parent.rightchild==node:
                node.parent.balance -= 1
            if node.parent.balance != 0:
                    self.updateBalance(node.parent)

    def rebalance(self,node):

        if node.balance<-1:

             a=node.rightchild
             if (a.rightchild):
                 print("Rotating left")
                 self.left_rotation(node)
             else:

                 print("rotating right-left")
                 self.right_left_rotation(a)


        elif node.balance>1:


            a=node.leftchild
            if(a.leftchild):
                 print("Rotating right")
                 self.right_rotation(node)
            else:
                 print("Rotating left-right")
                 self.left_rotation(a)
                 self.right_rotation(node)

        else:
            pass

    def left_rotation(self,node):
            print("BEIGINNING LEFT ROTATION")

            a=node.rightchild
            t2=a.leftchild
            a.leftchild=node
            node.rightchild=t2

            if(self.root==node):
                self.root=a
                node.parent=a
                a.parent=None
            else:
                node.parent.rightchild=a
                a.parent=node.parent
                node.parent=a

            self.updateBalance(a)
            self.updateBalance(node)

    def left_right_rotation(self,node):
            print("BEIGINNING LEFT ROTATION")
            a=node.rightchild
            t2=a.leftchild
            a.leftchild=node
            node.rightchild=t2

            if(self.root==node):
                self.root=a
                node.parent=a
                a.parent=None
            else:
                node.parent.leftchild=a
                a.parent=node.parent
                node.parent=a

            self.updateBalance(a)
            self.updateBalance(node)

    def right_rotation(self,node):
                print("BEGINNING RIGHT ROTATION")
                a=node.leftchild
                t3=a.rightchild
                a.rightchild=node
                node.leftchild=t3

                if(self.root==node):
                    self.root=a
                    node.parent=a
                    a.parent=None
                else:
                    node.parent.leftchild=a
                    a.parent=node.parent
                    node.parent=a

                self.updateBalance(a)
                self.updateBalance(node)

    def right_left_rotation(self,node):
                print("BEGINNING RIGHT ROTATION")

                a=node.leftchild
                t3=a.rightchild
                a.rightchild=node
                node.leftchild=t3

                if(self.root==node):
                    self.root=a
                    node.parent=a
                    a.parent=None
                else:
                    node.parent.rightchild=a
                    a.parent=node.parent
                    node.parent=a

                self.updateBalance(a)
                self.updateBalance(node)

    def preorder(self,node):
        if node ==None :
            return
        else:
            print(node.data,end="--")
            self.preorder(node.leftchild)
            self.preorder(node.rightchild)

    def height_AVL(self,node):
        if node==None:
            return -1
        else:
            lh=self.height_AVL(node.leftchild)
            rh=self.height_AVL(node.rightchild)
            return max(lh,rh) + 1

    def delete_a_node(self,data):
        if self.root==None:
            print("Empty AVL")
        else:


            parent=None
            node=self.root
            replace_node=None
            while(node!=None and node.data!=data):
                parent=node
                if data>=node.data:
                    node=node.rightchild
                    flag=1
                else:
                    node=node.leftchild
                    flag=0


            if node is None:
                print("node not in AVL.")

            else:
                x=node



                if (node.leftchild==None) and (node.rightchild==None):
                    if (flag):
                        parent.rightchild=None
                    else:
                        parent.leftchild=None
                    del node

                elif (node.leftchild==None) or (node.rightchild==None):
                    if node.leftchild==None:
                        if(flag):
                            parent.rightchild=node.rightchild
                        else:
                            parent.leftchild=node.rightchild
                    else  :
                        if(flag):
                            parent.rightchild==node.leftchild
                        else:
                            parent.leftchild=node.leftchild
                    node.rightchild.parent=x
                    del node


                else:
                     replace_node=self.minimum_element(node.rightchild)
                     temp=replace_node.data
                     self.delete_a_node(replace_node.data)
                     node.data=temp

                self.updateBalance(x)

    def minimum_element(self,node):
        if self.root==None:
            print("Empty AVL")
        else:
            while(node.leftchild!=None):
                node=node.leftchild
            print(node.data)
            return (node)
