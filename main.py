import sys
sys.path.insert(0, 'C:/Users/sidd/Desktop/AVL_Tree/')
import avl_tree


myavl = avl_tree.avl_tree()
myavl.insert_node(20)
myavl.insert_node(25)
myavl.insert_node(22)
myavl.insert_node(18)
myavl.insert_node(17)
myavl.insert_node(100)
myavl.insert_node(105)
myavl.insert_node(120)
myavl.insert_node(115)



#mybst.minimum_element(mybst.root)
#mybst.maximum_element(mybst.root)
myavl.preorder(myavl.root)
print("\n*****")
print()

#myavl.preorder(myavl.root)
print("\n*****")
print()
myavl.delete_a_node(22)
#mybst.preorder(mybst.root)
print()
myavl.preorder(myavl.root)
print("\n*****")
#print(mybst.height_BST(mybst.root))
