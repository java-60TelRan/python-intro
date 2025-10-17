from main import NumberBox
from unittest import TestCase
numbersAll: list[int] = [-10, 3, 7, 10, 20, 40, 100]
numbersNo100: list[int] = [-10, 3, 7, 10, 20, 40]
numbersOdd: list[int] = [3, 7]
numbersLess3: list[int] = [-10]
numbersGreater7: list[int] =  [10, 20, 40, 100]
numbersNo_7_20: list[int] = [-10, 3, 40, 100]
numbersDuplicates: list[int] = [-10, 3, 7, 10, 10, 10, 10, 20, 40, 100, 100, 100] 
class TestNumberBox(TestCase):
    def setUp(self):
        self.numberBox = NumberBox()
        [self.numberBox.addNumber(num) for num in numbersAll]
    def __run_test_iter(self, expected:list[int]) :
        actual: list[int] = sorted([num for num in self.numberBox] )  
        self.assertEqual(expected, actual)
    def test_iter(self):
        self.__run_test_iter(numbersAll)
    def test_remove_existing_number(self):
        self.assertEqual(100, self.numberBox.removeNumber(100))
        self.__run_test_iter(numbersNo100)
    def test_remove_non_existing_number(self):
        self.assertEqual(None, self.numberBox.removeNumber(1000))
        self.__run_test_iter(numbersAll)
    def test_remove_predicate(self):
        self.assertEqual(5, self.numberBox.removeNumbersPredicate(lambda n: n % 2 == 0))
        self.__run_test_iter(numbersOdd)
    def test_remove_greater_eq_2(self):
        self.assertEqual(6, self.numberBox.removeNumbersRange(min = 3, max = 1000)) 
        self.__run_test_iter(numbersLess3)
    def test_remove_less_eq_7(self):
        self.assertEqual(3, self.numberBox.removeNumbersRange(min = -100, max = 7))           
        self.__run_test_iter(numbersGreater7)
    def test_remove_range_7_20(self) :
        self.assertEqual(3, self.numberBox.removeNumbersRange(7, 20))
        self.__run_test_iter(numbersNo_7_20) 
    def test_distinct(self) :
        self.__addDuplicates()
        self.__run_test_iter(numbersDuplicates)
        self.assertEqual(5, self.numberBox.distinct())
        self.__run_test_iter(numbersAll)
                
    def __addDuplicates(self) :
        # for demo of multiplication on lists
        [self.numberBox.addNumber(num) for num in [10]*3] # [10, 10, 10]
        [self.numberBox.addNumber(num) for num in [100]*2] # [100, 100]    
        
            
        
        