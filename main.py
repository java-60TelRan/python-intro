numbers:list[int] = []
numbers.append(30)
numbers.append(20)
numbers.append(50)
numbers.append(3)

def getNumbersRange(lst: list[int], min: int, max: int) -> list[int]:
    res: list[int] = []
    for num in lst:
        if min <= num <= max:
            res.append(num)
    return res        
    
print(getNumbersRange(numbers, 25, 40))   