
def bSearchSortedList(lst: list[int], num: int) -> int:
    # takes sorted list and a number
    # returns index of the number if exists, otherwise -1
    left: int = 0
    right: int = len(lst) - 1
    middle: int = -1
    while left <= right :
        middle = (right + left) // 2
        if num > lst[middle] : 
            left = middle + 1
        else :
            right = middle - 1
        
    return left if len(lst) > left and lst[left] == num  else -(left + 1)     
    

numbers: list[int] = [1, 1, 5, 20, 20, 20, 20, 20, 30, 100]
print (bSearchSortedList(numbers, 20)) # output 3 (first occurrence)
print (bSearchSortedList(numbers, 1)) # output 0 (first occurrence)
print (bSearchSortedList(numbers, 200)) # output -11 (isertion position after last number)
print (bSearchSortedList(numbers, -10)) # output -1 (isertion position before first number)
print (bSearchSortedList(numbers, 10)) # output -4 (isertion position before to keep sorted)