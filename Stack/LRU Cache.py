# LRU (Least Recently Used) Cache discards the least recently used items first.

# Can also be solved using Doubly LinkedList along with a Hashmap 

from collections import OrderedDict
 
class LRUCache:
 
    # initialising capacity
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
 
    # we return the value of the key that is queried in O(1) else return -1 
    # And also move the key to the end to show that it was recently used.
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
 
    # we add / update the key and move the key to the end.
    # also check whether the length of our cache has exceeded our capacity,
    # If so we remove the first key (least recently used)
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

c=LRUCache(2)
c.put(1,1)
c.put(2,2)
c.get(1)
c.put(3,3)
print(c.cache)