from unittest import TestCase, main
from main import MySortedDict
class TestMySortedDict(TestCase):
    def setUp(self):
        self.testDict = MySortedDict()
        self.testDict["a"] = 1
        self.testDict["b"] = 2
        self.testDict["c"] = 3
    def test_set_existing_item(self):
        self.testDict["a"] = 20
        self.assertEqual(20, self.testDict["a"])
        self.testDict.update("a", 40)
        self.assertEqual(40, self.testDict["a"])
    def test_set_new_item(self):
        self.testDict["d"] = 20
        self.assertEqual(20, self.testDict["d"])
        self.testDict.update("e", 40)
        self.assertEqual(40, self.testDict["e"])    
    def test_set_default_existing_item(self):
        self.assertEqual(1, self.testDict.setdefault("a",40))
        self.assertEqual(1, self.testDict["a"])
    def test_set_default_new_item(self):
        self.assertEqual(40, self.testDict.setdefault("d",40))
        self.assertEqual(40, self.testDict["d"])
    def test_items(self):
        actual: list[(str, int)] = sorted(self.testDict.items())
        expected: list[(str, int)] = [("a", 1), ("b", 2), ("c", 3)]  
        self.assertEqual(expected, actual)
    def test_keys(self):
        actual: list[(str)] = sorted(self.testDict.keys())
        expected: list[str] = ["a", "b", "c"]  
        self.assertEqual(expected, actual)
    def test_values(self):
        actual: list[(int)] = sorted(self.testDict.values())
        expected: list[int] = [1, 2, 3]  
        self.assertEqual(expected, actual) 
    def test_pop_existing_item(self):
        self.assertEqual(1, self.testDict.pop("a"))
        self.assertFalse(self.testDict.get("a"))
    def test_pop_non_existing_item_with_no_key_error(self):
        self.assertEqual(None, self.testDict.pop("d", None))
    def test_pop_non_existing_item_with_key_error(self):
        with self.assertRaises(KeyError):
            self.testDict.pop("d")        
    def test_get_existing_item(self):
        self.assertEqual(1, self.testDict["a"])
        self.assertEqual(1, self.testDict.get("a"))
    def test_get_non_existing_item_no_error(self):
        self.assertEqual(None, self.testDict.get("d"))     
    def test_get_non_existin_item_with_error(self):
        with self.assertRaises(KeyError):
            self.testDict["d"]
    def test_bsect_left_existing_item(self):
        self.assertEqual(0, self.testDict.bisect_left("a"))
        
    def test_bsect_left_non_existing_item(self):
        self.assertEqual(3, self.testDict.bisect_left("d")) 
        self.assertEqual(0, self.testDict.bisect_left("A"))
        
    def test_bsect_right_existing_item(self):
        self.assertEqual(1, self.testDict.bisect_right("a"))
        self.assertEqual(3, self.testDict.bisect_right("c"))
        
    def test_bsect_right_non_existing_item(self):
        self.assertEqual(3, self.testDict.bisect_right("d")) 
        self.assertEqual(0, self.testDict.bisect_right("A"))
    
    def test_peekitem_right_index(self):
        self.assertEqual(("a", 1), self.testDict.peekitem(0))
        self.assertEqual(("b", 2), self.testDict.peekitem(1))
        self.assertEqual(("c", 3), self.testDict.peekitem(2)) 
        self.assertEqual(("c",3), self.testDict.peekitem(-1))
        self.assertEqual(("b",2), self.testDict.peekitem(-2))
        self.assertEqual(("a",1), self.testDict.peekitem(-3)) 
        
    def test_peekitem_wrong_index(self) :
        with self.assertRaises(IndexError) :
            self.testDict.peekitem(3)
        with self.assertRaises(IndexError) :
            self.testDict.peekitem(-4)                                     
                     
                