from sortedcontainers import SortedList
# used for lists/arrays with  frequent add/remove operaions

# method add has complexity O[LogN]
sortedList: SortedList[int] = SortedList()
sortedList.add(30)
sortedList.add(20)
sortedList.add(50)
sortedList.add(50)
sortedList.add(3)


def getNumbersSortedRange(lst: list[int], min: int, max: int) -> list[int]:
#    return part of list with closed range [min-max]
   left: int = sortedList.bisect_left(min)
   right: int = sortedList.bisect_right( max) 
   return lst[left:right] 
    
print(getNumbersSortedRange(sortedList, 25, 50))   