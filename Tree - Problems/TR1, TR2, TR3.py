# INORDER TRAVERSAL, PREORDER TRAVERSAL, POSTORDER TRAVERSAL

class TNode:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None
    
    def Preorder(self):
        print(self.val,end='')
        if self.left:
            self.left.Preorder()
        if self.right:
            self.right.Preorder()

    def Inorder(self):
        if self.left:
            self.left.Inorder()
        print(self.val,end='')
        if self.right:
            self.right.Inorder()

    def Postorder(self):
        if self.left:
            self.left.Postorder()
        if self.right:
            self.right.Postorder() 
        print(self.val,end='')      
        
root = TNode(4)
root.left = TNode(7)
root.right = TNode(2)
root.left.left = TNode(8)
root.left.right = TNode(1
root.right.left = TNode(6)
root.right.right = TNode(3)

print("\nPreorder Traversal : ",end='')
root.Preorder()

print("\nInorder Traversal : ",end='')
root.Inorder()

print("\nPostorder Traversal : ",end='')
root.Postorder()