from dataclasses import dataclass, field
from sortedcontainers import SortedSet, SortedKeyList
# in real development these classes should be in the separate modules
@dataclass(order=True, unsafe_hash=True)
class Person:
    id: int
    age: int = field(compare = False)
    

class Club: 
    def __init__(self):
        self.__sortedSet = SortedSet()
        self.__sortedKeyList = SortedKeyList(key=lambda p: (p.age, p.id))
    def addPerson(self, person: Person):
        # adds person
        # raises ValueError if person already exists
        if person in self.__sortedSet:
            raise ValueError(f"person with id {person.id} already exists")
        self.__sortedSet.add(person)
        self.__sortedKeyList.add(person)
    def getAllSortedId(self)-> list[Person]:
        return list(self.__sortedSet)
    def getAllSortedAgeId(self)->list[Person]:
        return list(self.__sortedKeyList)
    
    # HW #23 function 
    def getPersonsByAge(self, minAge:int, maxAge:int) -> list[Person]:
        leftInd: int = self.__sortedKeyList.bisect_key_left((minAge, 0))
        rightInd: int = self.__sortedKeyList.bisect_key_left((maxAge+1, 0))
        return list(self.__sortedKeyList[leftInd:rightInd])
################################################################################ 
class Dictionary: 
    def __init__(self):
        self.__words_sorted:list[str] = SortedKeyList(key = str.casefold)
        
    def addWord(self, word: str): 
        ind: int = self.__words_sorted.bisect_left(word)
        if ind < len(self.__words_sorted) and self.__words_sorted[ind].casefold() == word.casefold(): 
            raise ValueError(f"word {word} already exists")
        self.__words_sorted.add(word)
    
    def getWordsByPrefix(self, prefix: str) -> list[str]:
        leftInd: int = self.__words_sorted.bisect_left(prefix)
        rightInd: int = self.__words_sorted.bisect_left(prefix + "\uffff")
        return list(self.__words_sorted[leftInd:rightInd])
        


