from dataclasses import dataclass, field
from typing import Generic, Hashable, TypeVar
K = TypeVar('K', bound=Hashable)
V = TypeVar("V")
@dataclass(order=True, frozen=True)
class Entry(Generic[K, V]):
    key: K
    value: V = field(compare=False, hash=False)
    def __str__(self):
        return f"'{self.key}': {self.value}"
    
class MyDict(Generic[K, V]):
    def __init__(self):
        self.__entries: set[Entry[K, V]] = set()
    def __getitem__(self, key: K) -> V :
        entry: Entry[K, V] = self.__getEntryByKey(key)
        if not entry:
            raise KeyError(key)
        return entry.value
    def __setitem__(self, key: K, value: V):
        probe: Entry[K, V] = Entry(key, value)
        self.__entries.discard(probe)
        self.__entries.add(probe)
    def __getEntryByKey(self, key: K) -> Entry[K, V]:
        # our implementation is O[N], but built-in implementation is O[1] 
        res: Entry[K, V] = None
        probe: Entry[K, V] = Entry(key, None)
        if probe in self.__entries:
            res = next((e for e in self.__entries if e == probe))
        return res
    def __str__(self) :
        return  '{' + ", ".join([str(e) for e in self.__entries]) + '}'
        
        
if __name__ == "__main__":
    map: dict[str, int] = dict()
    map['a'] = 1
    map['b'] = 1
    print('from buil-in dict ',map['a'])
    print('from buil-in dict ',map)
    myDict: MyDict[str, int] = MyDict()
    myDict['a'] = 1
    myDict['a'] = 20
    myDict['b'] = 40
    print('from MyDict ',myDict)
          