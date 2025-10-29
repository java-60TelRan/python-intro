from typing import Callable, Iterator
import random
import sys
class RandomNumbersStream:
    def __init__(self, min: int, max: int):
        if min >= max: min, max = max, min
        self.__min:int = min
        self.__max:int = max
        self.__predicate: Callable[[int], bool] = lambda n: bool(n)
        self.__limit: int = -1
        self.__open: bool = True
        self.__distinct: bool = False
        self.__helperSet: set[int] = set()
    def setLimit(self,limit: int) :
        self.__limit = limit 
    def setFilter(self, predicate:Callable[[int], bool]):
        self.__predicate = predicate 
    def setDistinct(self):
        self.__distinct = True 
    def resetDistinct(self) :
        self.__distinct = False 
    def __iter__(self)-> Iterator[int] :
        count: int = 0
        number: int
        if not self.__open : raise GeneratorExit()
        self.__open = False
        while True:
          if count == self.__limit: break
          number = self.__getRandomNumber()
          if number not in self.__helperSet:
              if self.__distinct: self.__helperSet.add(number)
              count += 1
              yield number
                       
    def __getRandomNumber(self) -> int:
        number: int = None
        while  not self.__predicate(number):
            number = random.randint(self.__min, self.__max) 
        return number;    
if __name__ == '__main__':
    s1Min: int = 10
    s1Max: int = 100
    
    lottoMin: int = 1
    lottoMax: int = 49
    limit3: int = 10
    def printUsageMessage():
        print(f"\t\targ: 1 - endless stream of random numbers [{s1Min},{s1Max}]\n\
                arg: 2 - endless stream even random numbers [{s1Min},{s1Max}]\n\
                arg: 3 - stream of {limit3} even random numbers [{s1Min},{s1Max}]\n\
                arg: 4 - stream of SportLotto")
    def scenario1():
        numbers = RandomNumbersStream(s1Min, s1Max) 
        for num in numbers: print(num)
    def scenario2():
        numbers = RandomNumbersStream(s1Min, s1Max)
        numbers.setFilter(lambda n: n and n % 2 == 0)
        for num in numbers: print(num) 
    def scenario3():
        numbers = RandomNumbersStream(s1Min, s1Max)
        numbers.setFilter(lambda n: n  and n % 2 == 0)
        numbers.setLimit(limit3)
        for num in numbers: print(num)
      
    def scenario4():
        numbers =  RandomNumbersStream(lottoMin, lottoMax)
        numbers.setDistinct()
        numbers.setLimit(limit3)          
        for num in numbers: print(num)
   
    scenarios = {
    '1': scenario1,
    '2': scenario2,
    '3': scenario3,
    '4': scenario4,
     
    
}        
    
    if (len(sys.argv) < 2): printUsageMessage()
    else:
        scenarios.get(sys.argv[1], lambda : printUsageMessage())() 
      



    
                            