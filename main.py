from typing import Callable, Iterator


class NumberBox:
    #TODO constructor defining most effective data structure
    def addNumber(self,num: int): 
        #TODO adds number
        raise NotImplementedError()
    
    def removeNumber(self,num: int)->int:
        #TODO removes first occurrence of number and returns removed number or None if number missing
        raise NotImplementedError()
    
    def removeNumbersPredicate(self,pred: Callable[[int], bool])->int:
        #TODO removes all numbers matching a given predicate
        #predicate - function taking integer and returning True if the integer matches the predicate otherwise False
        #returns count of the removed numbers
        raise NotImplementedError()
    def removeNumbersRange(self, min: int, max: int)->int:
        #TODO removes all numbers that >=min and <=max
        #returns count of removed numbers
        raise NotImplementedError()
    def __iter__(self) -> Iterator[int]:
        #TODO code for ierating all numbers from NumberBox instance
        raise NotImplementedError()
    def distinct(self)->int:
        #TODO removing repeated numbers
        raise NotImplementedError()
        
          