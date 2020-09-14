import lab1
import unittest


class T0_TestingQueue(unittest.TestCase):
    
    def test_basic_enqueue(self):
        #testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        
        self.assertEqual(q.printQueue(), [1,2,3,4])
        print("\n")

    def test_basic_dequeue(self):
        #testing the basic dequeue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.dequeue(), 1)
        print("\n")

    def test_dequeue_empty(self):
        #testing dequeue operation with empty queue
        print("\n")
        q = lab1.Queue()

        self.assertEqual(q.dequeue(), None)
        print("\n")

    def test_enqueue_dequeue(self):
        #testing enqueue dequeue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.dequeue()

        self.assertEqual(q.printQueue(), [2,3,4])
        print("\n")

    def test_is_empty_true(self):
        #testing if queue is empty
        print("\n")
        q = lab1.Queue()

        self.assertTrue(q.isEmpty())
        print("\n")

    def test_is_empty_false(self):
        #testing if queue is empty
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)

        self.assertFalse(q.isEmpty())
        print("\n")

    def test_print_empty_queue(self):
        print("\n")
        q = lab1.Queue()

        self.assertEqual(q.printQueue(), [])
        print("\n")

class T1_TestingStack(unittest.TestCase):
    def test_basic_push(self):
        #testing stack push operation
        print("\n")
        s = lab1.Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        self.assertEqual(s.printStack(), [5,4,3,2,1])
        print("\n")

    def test_basic_pop(self):
        print("\n")
        s = lab1.Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        self.assertEqual(s.pop(), 5)
        print("\n")

    def test_pop_empty(self):
        print("\n")
        s = lab1.Stack()
        self.assertEqual(s.pop(), None)
        print("\n")

    def test_push_pop(self):
        #testing stack push operation
        print("\n")
        print("Testing Stack: Push and Pop")
        s = lab1.Stack()
        s.push(1)
        s.push(2)
        s.pop()
        s.push(3)
        s.push(4)
        s.push(5)
        self.assertEqual(s.printStack(), [5,4,3,1])
        print("\n")

    def test_is_empty_true(self):
        #testing if queue is empty
        print("\n")
        s = lab1.Stack()
        print("return true if the stack is empty")
        self.assertEqual(s.isEmpty(), True)
        print("\n")

    def test_is_empty_false(self):
        #testing if queue is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")

    def test_print_empty_queue(self):
        print("\n")
        q = lab1.Queue()

        self.assertEqual(q.printQueue(), [])
        print("\n")


class T2_TestingPalindrome(unittest.TestCase):
    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        print("Is the string a palindrome?: ", p)
        self.assertEqual(p, False)
        print("\n")

    def test_empty_string(self):
        # testing with empty string
        print("\n")
        string = ""
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        print("Is the string a palindrome?: ", p)
        self.assertEqual(p, True)
        print("\n")

    def test_single_character_string(self):
        # testing with single character string
        print("\n")
        string = "h"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        print("Is the string a palindrome?: ", p)
        self.assertEqual(p, True)
        print("\n")

    def test_string_with_spaces(self):
        # testing with string with spaces
        print("\n")
        string = "ni t I n"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        print("Is the string a palindrome?: ", p)
        self.assertEqual(p, True)
        print("\n")

if __name__ == '__main__':
    unittest.main()
