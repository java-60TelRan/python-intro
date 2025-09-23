
import sys


def isSumTwo(numbers: list[int], sum: int):
    helper: set[int] = set()
    indx: int = 0
    res: bool = False
    length: int = len(numbers)
    while indx < length and not res: 
        if sum - numbers[indx] in helper:
            res = True
        else: 
            helper.add(numbers[indx])
            indx += 1
    return res

def maxNegativeRepr(numbers: list[int]): 
      res: int = 0 
      helper: set[int] = set()
      for num in numbers:
          if abs(num) > res and -num in helper  :
              res = abs(num)
          else: 
              helper.add(num)
      return res if res else -1   
        
 

