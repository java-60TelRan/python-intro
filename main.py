# stack defines access to only last element LIFO
# regular list / array workd fine for stack
# adding / removing last element is performed with complexity O[1]
# stack: list[int] = [1, 2, 10, -5]
# stack.append(10) #adds at ene of stack
# stack.pop() #removes last element
# print(stack)
################################################
# queue define access for adding at end and for removing from beginning, FIFO (First In First Out) 
# queue: list[int]= [1, 2, 10, -5] not good choice - because removing first item is performed with complexity O[N]
# from collections import deque
# queue: deque[int] = deque([1, 2, 10, -5]) # right choice for queue because removing first item is performed with complexity O[1]
# queue.append(10)
# queue.popleft() # complexity O[1]
# print(queue)

