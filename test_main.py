from unittest import TestCase, main

from main import bSearchSortedList
class BinarySearchTest(TestCase): 
    def setUp(self):
        self.numbers: list[int] = [1, 1, 5, 20, 20, 20, 20, 20, 30, 100]
        
    def test_found_first(self):
        self.assertEqual(bSearchSortedList(self.numbers, 1), 0) 
        self.assertEqual(bSearchSortedList(self.numbers, 100), len(self.numbers) - 1) 
        self.assertEqual (bSearchSortedList(self.numbers, 20), 3) 
    
    def test_not_found(self):
        self.assertEqual(bSearchSortedList(self.numbers,-10), -1) 
        self.assertEqual(bSearchSortedList(self.numbers, 18), -4)
        self.assertEqual(bSearchSortedList(self.numbers, 200), -(len(self.numbers) + 1))
        
    def test_empty_list(self):
        self.assertEqual(bSearchSortedList([],5), -1)
        
        
        