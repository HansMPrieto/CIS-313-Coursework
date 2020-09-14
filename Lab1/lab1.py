
class Node(object):
    def __init__(self, data = None, next = None):
        self.__data = data
        self.__next = next
            
    def setData(self, data):
        # Set the "data" data field to the corresponding input
        self.__data = data

    def setNext(self, next):
        # Set the "next" data field to the corresponding input
        self.__next = next

    def getData(self):
        # Return the "data" data field
        return self.__data

    def getNext(self):
        # return the "next" data field
        return self.__next


class Queue(object):
    def __init__(self):
        self.__head = None
        self.__tail = None

    def enqueue(self, newData):
        # Create a new node whose data is newData and whose next node is null
        # Update head and tail
        # Hint: Think about what's different for the first node added to the Queue
        newNode = Node()
        newNode.setData(newData)
        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.setNext(newNode)
            self.__tail = newNode

    def dequeue(self):
        #  Return the head of the Queue
        #  Update head
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        if self.isEmpty():
            return None
        else:
            temp = self.__head
            self.__head = self.__head.getNext()
            return temp.getData()

    def isEmpty(self):
        # Check if the Queue is empty
        if self.__head is None and self.__tail is None:
            return True
        return False

    def printQueue(self):
        # Loop through your queue and print each Node's data
        current = self.__head
        temp = []
        while current:
            temp.append(current.getData())
            current = current.getNext()
        return temp


class Stack(object):
    def __init__(self):
        # We want to initialize our Stack to be empty
        # (ie) Set top as null
        self.__top = None

    def push(self, newData):
        # We want to create a node whose data is newData and next node is top
        # Push this new node onto the stack
        # Update top
        newNode = Node()
        newNode.setData(newData)
        newNode.setNext(self.__top)
        self.__top = newNode

    def pop(self):
        # Return the Node that currently represents the top of the stack
        # Update top
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        if self.isEmpty():
            return None
        else:
            temp = self.__top
            self.__top = self.__top.getNext()
            return temp.getData()

    def isEmpty(self):
        # Check if the Stack is empty
        if self.__top is None:
            return True
        else:
            return False

    def printStack(self):
        # Loop through your stack and print each Node's data
        current = self.__top
        temp = []
        while current:
            temp.append(current.getData())
            current = current.getNext()
        return temp


def isPalindrome(s):
    # Use your Queue and Stack class to test whether an input is a palindrome
    myStack = Stack()
    myQueue = Queue()

    s = s.casefold()
    s.replace(" ", "")

    if len(s) == 0:
        return True

    for elem in s:
        myStack.push(elem)
        myQueue.enqueue(elem)

    ## Helper function ##
    print("stack data")
    myStack.printStack()

    print("queue data")
    myQueue.printQueue()

    while not myStack.isEmpty() and not myQueue.isEmpty():
        top = myStack.pop()
        head = myQueue.dequeue()
        if top != head:
            return False
        else:
            return True
