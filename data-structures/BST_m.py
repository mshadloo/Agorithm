class TreeNode:
    def __init__(self,deta):
        self.data=data;
        self.right-None;
        self.left=None;
class BST:
    def __init__(self):
        self.root=None;
    def insert(self, data):
        if(self.root is None):
            self.root=TreeNode(data)
        else:
            if(data<self.root.data):
                self.root.left=insertNode(self.root.left,data)
            else:
                if(data>self.root.data):
                   self.root.right=insertNode(self.root.right,data)
    def insert2(self,data):
        if(self.root is None):
            self.root=TreeNode(data)
        else:
            currentNode=self.root;
            inserted=False;
            while(!inserted):
                if(currentNode.data==data):
                    inserted=True;
                else:
                    if(data>currentNode.data):
                        if(currentNode.right==None):
                            currentNode.right=TreeNode(data)
                            inserted=True;
                        else:
                            currentNode=currentNode.right
                    else:
                        if(currentNode.left==None):
                            currentNode.left=TreeNode(data)
                            inserted=True;
                        else:
                            currentNode=currentNode.left

    def insertNode(self,node,data):
        if(node is None):
            return TreeNode(data)
        if(data<node.data):
                node.left=self.insertNode(node.left,data)
        else:
            if(data>node.data):
                node.right=self.insertNode(node.right,data)
        return node
    def delete(self,data):
        self.root=self.deleteNode(self.root,data)
    def find(self,data):
        if(self.root.data==data):
            return self.root;
        else:
            if(data>self.root.data):
                return self.findNode(self.root.right,data)
            else:
                return self.findNode(self.root.left,data)
    def findNode(self,node,data):
        if(node is None):
            print(str(data)+' is not in BST')
            return None;
        if(node.data==data):
            return self.root;
        else:
            if(data>node.data):
                return self.findNode(node.right,data)
            else:
                return self.findNode(node.left,data)
    def deleteNode(self,node,data):
        if(node.data>data):
             node.right=self.deleteNode(node.right,data)
        elif(node.data<data):
             node.left=self.deleteNode(node.left,data)
        else:
            if(node.left is None):
                return node.right
            elif(node.right is None):
                return node.left
            else:
                successor=self.inorderSuccessor(node)
                node.data=successor.data
                node.right=self.deleteNode(node.right,data)
        return node
    def inorderSuccesor(self,node):
        if(node is None or node.right is None):
            print('bad situation')
            return None
        successor=node.right;
        while(successor.left is not None):
            successor=successor.left
        return successor




