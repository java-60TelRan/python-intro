from typing import Callable, Iterator

from sortedcontainers import SortedList

#############################################################################################################
class NumberBox:
    # constructor defining most effective data structure
    def __init__(self):
        self.__numbers = SortedList[int]()
    def addNumber(self,num: int): 
        # adds number
        self.__numbers.add(num)
    
    def removeNumber(self,num: int)->int:
        # removes first occurrence of number and returns removed number or None if number missing
        res: int = None
        try:
            self.__numbers.remove(num)
            res = num
        except ValueError:
            pass
        return res   
    
    def removeNumbersPredicate(self,pred: Callable[[int], bool])->int:
        # removes all numbers matching a given predicate
        #predicate - function taking integer and returning True if the integer matches the predicate otherwise False
        #returns count of the removed numbers
        lengthBefore: int = len(self.__numbers)
        filteredNumbers = [n for n in self.__numbers if not pred(n)]
        self.__update(filteredNumbers)
        return lengthBefore - len(self.__numbers)
    def removeNumbersRange(self, min: int, max: int)->int:
        # removes all numbers that >=min and <=max
        #returns count of removed numbers
        if min > max: min, max = max, min
        left: int = self.__numbers.bisect_left(min)
        right: int = self.__numbers.bisect_right(max)
        if left < len(self.__numbers): del self.__numbers[left:right]
        return right - left
        
    def __iter__(self) -> Iterator[int]:
       return iter(self.__numbers)
    def distinct(self)->int:
       lengthBefore:int = len(self.__numbers)
       filteredNumbers = [n for i, n in enumerate(self.__numbers) if i == 0 or self.__numbers[i] != self.__numbers[i - 1]]
       self.__update(filteredNumbers)
       return lengthBefore - len(self.__numbers)
    def __update(self, filteredNumbers: list[int]):
       self.__numbers = SortedList(filteredNumbers)
        
