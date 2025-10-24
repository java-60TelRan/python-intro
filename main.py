from collections import OrderedDict
from typing import  Hashable, Generic, Iterator, TypeVar
from sortedcontainers import SortedDict
K = TypeVar('K', bound=Hashable)
V = TypeVar("V")

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
        
class  LfuDictCache(Generic[K, V]):
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.cache: dict[K, tuple[V, int]] = {} #dictionary with key as K and value as tuple (V, <frequency as number of accesses>)
        self.frequency_key:SortedDict[int, DictCache[K, None]] = SortedDict() #sorted dictionary with key as frequency and value as LRU cache (DictCache[K, V])
    def __getitem__(self, key: K) -> V:
        value, frequency = self.cache[key] # unpacking of tuple with value and frequency
        self.__update_cache(key, value, frequency)
        return value

    def __update_cache(self, key, value, frequency):
        # removing from lru_cache as value of dictionary frequency-DictCache association with a given key for frequency
        # and adding the key to another lru_cache for the incremented frequency (frequency + 1)
        new_frequency = frequency + 1
        self.cache[key] = (value, new_frequency)
        if frequency >= 0:
            lru_cache: DictCache[K, None] = self.frequency_key[frequency]
            lru_cache.pop(key)
            if not lru_cache:
                # remooving association from sorted dictionary if LRU cache is empty
                self.frequency_key.pop(frequency)
        self.frequency_key.setdefault(new_frequency, DictCache(self.max_size))[key] = None
        
    def __setitem__(self, key: K, new_value: V):
        frequency: int = -1
        if key in self.cache:
            # no adding new association 
           frequency = self.cache[key][1]
        elif len(self.cache) == self.max_size:
            # no room for new association - deleting LFU
            self.__lfu_delete()
        self.cache[key] = (new_value, frequency + 1)
        self.__update_cache(key, new_value, frequency)
    def __lfu_delete(self):
        frequency: int
        lru_cache: DictCache[K, None]
        frequency, lru_cache = self.frequency_key.peekitem(0)
        key_to_delete: K = lru_cache.popitem(last = False)[0] #remooving LRU 
        if not lru_cache:
            # remooving association from sorted dictionary if LRU cache is empty
            self.frequency_key.pop(frequency)
        self.cache.pop(key_to_delete) # removing from cache dictionary   
                  
           
    def __delitem__(self, key: K):
        frequency = self.cache.pop(key)[1] # removing from cache dictionary
        lru_cache: DictCache[K, None] = self.frequency_key[frequency] 
        del lru_cache[key] #removing from LRU
        if not lru_cache:
            del self.frequency_key[frequency] # remooving association from sorted dictionary if LRU cache is empty
        
    def __iter__(self) -> Iterator[K]:
        return iter(self.cache)
    def __len__(self)->int:
       return len(self.cache)
