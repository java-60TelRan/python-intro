class MyStackInt:
    def __init__(self):
        self.__numbers: list[int] = [] # all numbers
        self.__max_values: list[int] = [] # all maximal values
    def push(self, num: int):
        self.__numbers.append(num)
        if not self.__max_values or num >= self.__max_values[-1]:
            self.__max_values.append(num)
    def pop(self):
        num:int = self.__numbers.pop()
        if num == self.__max_values[-1]: self.__max_values.pop()
        return num
    def max(self) :
        return self.__max_values[-1]  
                
            
            

