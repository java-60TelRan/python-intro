from main import MyStackInt
from unittest import TestCase, main
numbers: list[int] = [10, 20, 20, 5, 7, 2 ,1]
class TestMyStackInt(TestCase):
    def setUp(self):
        self.stack = MyStackInt()
        [self.stack.push(num) for num in numbers]
    def test_max_after_pushes(self):
        self.assertEqual(20, self.stack.max()) 
        self.stack.push(50)
        self.assertEquals(50, self.stack.max())
    def test_max_after_pops(self):
        for num in reversed(numbers[2:]):
            self.assertEqual(num, self.stack.pop())
            self.assertEqual(20, self.stack.max())
        self.assertEqual(20, self.stack.pop())
        self.assertEqual(10, self.stack.max()) 
    def test_errors_for_empty_stack(self):
        for i in range(len(numbers)):
            self.stack.pop()
        self.assertRaises(IndexError, lambda: self.stack.pop())
        self.assertRaises(IndexError, lambda: self.stack.max())
                 
if __name__ == "__main__" :
    main()             