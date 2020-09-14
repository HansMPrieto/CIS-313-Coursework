class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)

    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            self.__print(curr_node.right)
            print(str(curr_node.data), end=' ')  # save space

    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is null, calling n.getData() will cause an error
        if self.root is None:
            self.root = Node(data)
        else:
            n = Node(data)
            tree_root = self.root
            while tree_root is not None:
                if data < tree_root.data:
                    if tree_root.left is not None:
                        tree_root = tree_root.left
                    else:
                        tree_root.left = n
                        break
                elif data > tree_root.data:
                    if tree_root.right is not None:
                        tree_root = tree_root.right
                    else:
                        tree_root.right = n
                        break

    def min(self):
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        curr_node = self.root
        if curr_node is not None:
            while curr_node.left is not None:
                curr_node = curr_node.left
        return curr_node

    def max(self):
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        curr_node = self.root
        if curr_node is not None:
            while curr_node.right is not None:
                curr_node = curr_node.right
        return curr_node

    def __find_node(self, data):
        # returns the node with that particular data value else returns None
        curr_node = self.root
        while curr_node is not None and data != curr_node.data:
            if data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return curr_node

    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        if self.__find_node(data) is not None:
            return True
        else:
            return False

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        # helper method implemented using generators
        # all the traversals can be implemented using a single method
        if curr_node is not None:
            if traversal_type == Tree.INORDER:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield curr_node.data
                yield from self.__traverse(curr_node.right, traversal_type)
            elif traversal_type == Tree.PREORDER:
                yield curr_node.data
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
            elif traversal_type == Tree.POSTORDER:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
                yield curr_node.data

    def find_successor(self, data):
        # helper method to implement the delete method but may be called on its own
        # if the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty,then go up the tree until a node that is
        # the left child of its parent is encountered.
        succ = None
        curr_node = self.root
        if self.__find_node(data) is None:
            raise KeyError()

        if curr_node is None:
            return
        while curr_node is not None:
            if curr_node.data > data:
                succ = curr_node
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return succ

    def _delete(self, node, data):
        if node is None:
            return None

        if self.__find_node(data) is None:
            raise KeyError()

        if data < node.data:
            node.left = self._delete(node.left, data)
            return node
        elif data > node.data:
            node.right = self._delete(node.right, data)
            return node

        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                newRootVal = self.find_successor(node.data)
                newRootValData = newRootVal.data
                node.data = newRootValData
                node.right = self._delete(node.right, newRootValData)

    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does not exist in the tree, then don't change the tree.
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to Null.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Hint: you may want to write a new method, findSuccessor() to find the successor when there are two children
        self._delete(self.root, data)


