
s1: set[int] = set([10, 80, 16, 3, 32, -10, -80])
s2: set[int] = set([10, 20, 80, 32])
# print (s1 & s2, "intersection") # intersection
# print (s1 | s2, "union") # union
# print (s1 ^ s2, "exlusion") # excluding common items
# print (s1 - s2, "subtraction") # subtraction
print (100 in s1) # O[1]
print (10 in [10, 80, 16, 3, 32, -10, -80]) # O[N]
