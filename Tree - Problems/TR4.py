# INSERT A NODE IN A BINARY SEARCH TREE

class TNode:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None
        
def insert_node(root,data):
    if root is None:
        return TNode(data)
    if data < root.data:
        root.left = insert_node(root.left,data)
    if data > root.data:
        root.right = insert_node(root.right,data)

