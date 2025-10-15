from test_my_dict_common import TestMyDictCommon
from main import MySortedDict
class TestMySortedDict(TestMyDictCommon):
    def getDict(self):
        return MySortedDict()
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
                     
                