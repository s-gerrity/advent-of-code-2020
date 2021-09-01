# # day 5 practice

# class Binary_Search_Tree:
    
#     """
#     Constructor with vaue we are going 
#     to insert in tree with assigning
#     left and right child with default None 
#     """
    
#     def __init__(self, data):
#         self.data = data
#         self.Left_child = None
#         self.Right_child = None

#     def __repr__(self):
#         """Debugging-friendly representation."""

#         return "<BinaryNode {data}>".format(data=self.data)

#     """
#     If the data we are inserting already 
#     present in tree it will not add it 
#     to avoid the duplicate values
#     """
        
#     def Add_Node(self, data):
#         if data == self.data:
#             return # node already exist



#         """
#         If the data we are inserting is Less
#         than the value of the current node, then
#         data will insert in Left node
#         """
        
#         if data < self.data:
#             if self.Left_child:
#                 self.Left_child.Add_Node(data)
#             else:
#                 self.Left_child = Binary_Search_Tree(data)
         
#             """
#             If the data we are inserting is Greater
#             than the value of the current node, then
#             data will insert in Right node
#             """
            
#         else:
#             if self.Right_child:
#                 self.Right_child.Add_Node(data)
#             else:
#                 self.Right_child = Binary_Search_Tree(data)


#     def Find_Node(self, val):
        
#         """
#         If current node is equal to 
#         data we are finding return true
#         """
        
#         if self.data == val:
#             return True
        
#         """
#         If current node is lesser than 
#         data we are finding we have search 
#         in Left child node
#         """

#         if val < self.data:
#             if self.Left_child:
#                 return self.Left_child.Find_Node(val)
#             else:
#                 return False
        
#         """
#         If current node is Greater than 
#         data we are finding we have search 
#         in Right child node
#         """

#         if val > self.data:
#             if self.Right_child:
#                 return self.Right_child.Find_Node(val)
#             else:
#                 return False
            
       

# new_node = Binary_Search_Tree('rabbit')
# print(new_node)

# ## from a medium article
# ## https://medium.com/@siddharthgupta555t/finally-understanding-recursion-and-binary-search-trees-857c85e72978

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None


# def insert(value,node):
#     if value < node.data:
#         if node.left == None:
#             node.left = Node(value)
#         else:
#             print ("Going Left")
#             insert(value,node.left)
#     else:
#         if node.right == None:
#             node.right = Node(value)
#         else:
#             print ("Going Right")
#             insert(value,node.right)
#     return

# Node(63)


# pseudocode
# try building a bst that has numbers
# it can take in a command that tells it to go left or right, rather than searching for a specific Value
# after that, make a bst that assembles the nodes based on the commands of left or right?
# could be done with division















class Node:
    # constructor
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        # checks to see if the data being added already exists;
        # prevents duplicate data from being added
        if self.value == data:
            return print(False, "this " + data + " cannot be added more than once")
        # check if the data being added is less than the current node
        elif self.value > data:
            if self.leftChild:
                # check if there is a left child already
                # if there is a left child, it will call the function again
                # until it finds an opening to insert at
                return self.leftChild.insert(data)
            else:
                # if there is no left child, create a new node as left child
                self.leftChild = Node(data)
                return print(True, "new left child created with " + data)
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    # if the current node contains the data we're looking for
    # it will return true
    def find(self, data):
        if(self.value == data):
            return True

# main interface for the user
class Tree:
    #constructor
    def __init__(self):
        self.root = None

    # check if the root node exists, if it does, that means theres
    # at least one node in the tree
    def insert(self, data):
        if self.root:
            # when root does exist, call insert in Node class
            return self.root.insert(data)
        else:
            # if the root node does not exist we will create a root node
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False



bst = Tree()
bst.insert(14)


























