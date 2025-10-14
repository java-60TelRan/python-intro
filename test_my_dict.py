from unittest import TestCase, main
from main import MyDict
class TestMyDict(TestCase):
    def setUp(self):
        self.testDict = MyDict()
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
                     
                