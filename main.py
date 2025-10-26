from itertools import count, islice
from sys import getsizeof
from typing import Iterator, Iterable

def printIterable(iterable: Iterable[int]) : 
    for num in iterable:
        print(num)
class NumbersStream:
    def __init__(self, start: int = 0):
        self.start = start
    def __iter__(self) -> Iterator[int]:
        for num in  count(self.start):
            yield(num) 
    def limit(self, lim: int)->Iterable[int] :
        return islice(self, lim)       

stream = NumbersStream(10) 
stream1 = stream.limit(200)
stream2 = stream.limit(200)
filteredList = [num for num in stream1 if num % 2] 
filteredGenerator = (n for n in stream2 if n % 2)
for x in filteredGenerator:
    print(x)
print(f"size of generator object is {getsizeof(filteredGenerator)}; sizeof list object is {getsizeof(filteredList)}") 
