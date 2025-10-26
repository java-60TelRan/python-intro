# HW#28 Definition
## Write class RandomNumbersStream with the following methods and use cases
### Methods
def __init__(self,min: int = -10 ** 20, max: int = 10 ** 20) implied the generation of endless random numbers in closed interval [min, max]<br>
def setFilter(self, predicate: Callable[[int], bool]) sets predicate for filtering generated random numbers<br>
def setLimit(self, limit: int) sets limit of generated random numbers<br>
def setDistinct(self) defines the generation of unique random numbers (by default numbers may repeat)<br>
def resetDistinct(self) cancel the generation of unique random numbers (sets default)<br>
def __iter__(self) -> Iterator[int] iterates generated random numbers 
### Use Cases
#### Endless Random Numbers Streaming: 
numbers = RandomNumbersStream(min=10, max=100)<br>
for num in numbers: print(num) - endless loop printing random numbers in the interval [10, 100]
### Endless Even Random Numbers Streaming:
numbers = RandomNumbersStream(min=10, max=100)<br>
numbers.setFilter(lambda n: n % 2 = 0)<br>
for num in numbers: print(num) - endless loop printing even random numbers in the interval [10, 100]
### Limitted Even Random Numbers Streaming
numbers = RandomNumbersStream(min=10, max=100)<br>
numbers.setFilter(lambda n: n % 2 = 0)<br>
numbers.setLimit(10)<br>
for num in numbers: print(num) - printing 10 even random numbers in the interval [10, 100]
### Sport Lotto 
numbers = RandomNumbersStream(min=1, max=49)<br>
numbers.setDistinct()<br>
numbers.setLimit(10)<br>
for num in numbers: print(num) - printing 10 unique random numbers in the interval [1, 49]