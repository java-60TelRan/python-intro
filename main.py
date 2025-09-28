import bisect
# used for lists/arrays with not frequent add/remove operaions
numbers:list[int] = []
# insort has complexity O[N]
bisect.insort(numbers,30)
bisect.insort(numbers,20)
bisect.insort(numbers,50)
bisect.insort(numbers,50)
bisect.insort(numbers,3)


def getNumbersSortedRange(lst: list[int], min: int, max: int) -> list[int]:
#    return part of list with closed range [min-max]
   left: int = bisect.bisect_left(lst, min)
   right: int = bisect.bisect_right(lst, max) 
   return lst[left:right] 
    
print(getNumbersSortedRange(numbers, 25, 50))   