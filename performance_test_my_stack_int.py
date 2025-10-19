from time import time
from main import MyStackInt
import random

N_ITEMS: int = 100000
N_RUNS: int = 10000
if __name__ == "__main__":
    '''Creating and filling stack and list'''
    stack: MyStackInt = MyStackInt()
    numbers: list[int] = []
    for i in range(N_ITEMS):
        num: int = random.randint(1, 1000)
        stack.push(num)
        numbers.append(num)
########################################################################
    '''finding maximal value with O[1]'''  
    start_time = time()
    max_stack: int = 0
    for i in range(N_RUNS):
        max_stack = stack.max()
    run_time = time() - start_time
    print(f"MyStackInt:  maximal value is {max_stack}; running time is {run_time:.6f}") 
############################################################################################       
    '''finding maximal value with O[N]'''  
    start_time = time()
    max_list: int = 0
    for i in range(N_RUNS):
        max_list = max(numbers)
    run_time = time() - start_time
    print(f"list with numbers:  maximal value is {max_list}; running time is {run_time:.6f}")             