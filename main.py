from abc import ABC, abstractmethod
from collections import OrderedDict
from dataclasses import dataclass, field
from typing import Any, Generic, Hashable, Self, TypeVar

from sortedcontainers import SortedSet
K = TypeVar('K', bound=Hashable)
V = TypeVar("V")
_sentinel = object()

@dataclass(order=True, frozen=True)
class Entry(Generic[K, V]):
    key: K
    value: V = field(compare=False, hash=False)
    def __str__(self):
        return f"'{self.key}': {self.value}"
class MyDictAbstract(ABC, Generic[K, V]) :
    def __init__(self, set: Any):
        self._entries: Any = set
    def __getitem__(self, key: K) -> V :
        entry: Entry[K, V] = self._getEntryByKey(key)
        if not entry:
            raise KeyError(key)
        return entry.value 
    def __setitem__(self, key: K, value: V):
        probe: Entry[K, V] = Entry(key, value)
        self._entries.discard(probe)
        self._entries.add(probe)  
    @abstractmethod
    def _getEntryByKey(self, key: K): pass
    def __str__(self) :
        return  '{' + ", ".join([str(e) for e in self._entries]) + '}'     
     # HW #24
    def __len__(self):
        # returns count of the entries
        # this is a magic method allowing using the function len of Python
        raise len(self._entries)
    def setdefault(self, key: K, default: V = None):
        #  If key missing, insert key: default; return the default.
        #  If key exists, no insert, no update; return the value
        res: V = default
        if Entry(key, None) in self._entries:
            res = self._getEntryByKey(key).value
        else:
            self[key] = default
        return res
    def get(self, key: K, default: V = None):
        #  returns value for key or any default if key missing
        
        return default if Entry(key, None) not in self._entries else self._getEntryByKey(key).value
    
    def items(self) -> list[(K,  V)]:
        # returns list of tuples (key, value)
        # tuple is an immutable list 
        # [1, 2] - list, (1, 2) - tuple
        # assume that e is Entry, then to create tuple from Entry e - (e.key, e.value)
        # try to write one code line using so called comprehension expresson
        # [<expression with item> for <item> in <items>] 
       return [(e.key, e.value) for e in self._entries]
    
    def keys(self) -> list[K]:
        #  returns list of keys
        return [e.key for e in self._entries]
    
    def values(self) -> list[V]:
        # returns list of values
        return [e.value for e in self._entries]    
    def update(self, key: K, value: V):
        #  if key exists, updates value for the key
        # if key missing, inserts key: value entry
        self[key] = value
    def pop(self, key: K, default=_sentinel)->V:
        #  removes key if the key exists, return the associated value
        # line 72 with default value is intended for differentiating optional parameter. As None may be value passed by a caller 
        # if default is _sentinel, a caller has not passed default value.
        # Operator "is" implies the same reference. It differs from '==' (equility) 
        # if key missing and default value having been passed that value will be returned
        # if key missing and default value not passed KeyError should be raised
        probe = Entry(key, None)
        if probe in self._entries:
            res: V = self._getEntryByKey(key).value
            self._entries.remove(probe)
        else:
            if default is _sentinel:
                raise KeyError(key)
            res = default
        return res       
class MyDict(MyDictAbstract[K, V]):
    def __init__(self):
        super().__init__( set())
    
   
    def _getEntryByKey(self, key: K) -> Entry[K, V]:
        # our implementation is O[N], but built-in implementation is O[1] 
        res: Entry[K, V] = None
        probe: Entry[K, V] = Entry(key, None)
        if probe in self._entries:
            res = next((e for e in self._entries if e == probe))
        return res
    
       
    
    
    
        
 ###########################################################################################
class MySortedDict(MyDictAbstract[K, V]):
    def __init__(self) :
       super().__init__(SortedSet())       
    
    
    def _getEntryByKey(self, key: K) -> Entry[K, V]:
        res: Entry[K, V] = None
        probe: Entry[K, V] = Entry(key, None)
        leftInd = self._entries.bisect_left(probe)
        if leftInd < len(self._entries) and self._entries[leftInd] == probe:
            res = self._entries[leftInd]
        return res
    
    def bisect_left(self, key:K)->int:
        #  returns first index of key that >= a given key
        return self._entries.bisect_left(Entry(key, None))
    def bisect_right(self, key:K)->int:
        #  returns first index of key that > a given key
        return self._entries.bisect_right(Entry(key, None))
    def peekitem(self, ind: int)->tuple[K,V] :
        #  returns received from Entry tuple at a specified index
        # may take a negative index with meaning the indexing from the end (index -1 designates the kast key
        # raises error for an index out of a possible range (index < -len(self) or index >= len(self))
        entry: Entry[K, V] = self._entries[ind]
        return (entry.key, entry.value)
  ####################################################################################
  
class DictCache(OrderedDict[K, V]) :
    def __init__(self, maxsize=128):
        super().__init__() # calls constructor of OrderedDict that has all methods for keeping insertion order
        self.maxsize = maxsize
    # The  methods __getitem__ and __setitem__ should be overriden
    # Assumption: only following methods should be overriden for making tests from test_dict_cache.py passed
    # Hints as follows: 
    # super().__getitem__(key) calls method __getitem__ of OrderedDict
    # super().__setitem__(key, value) calls method __setitem__ of OrderedDict
    # consider using self.move_to_end(key) of OrderedDict for making item with the given key as most recent
    # consider using self.popitem(last=False) for removing least recent (eldest item)
    
    def __getitem__(self, key)->V:
       res =  super().__getitem__(key)
       self.move_to_end(key)
       return res

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
        if len(self) > self.maxsize:
            self.popitem(last = False)
        
   
