# '''
# Linked List hash table key/value pair
# '''
import hashlib
from functools import reduce
import random, string


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def __repr__(self):
        return str(self.storage)

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        '''
        Algorithm:
            Create a Linked Pair passing in key and val
            add all the ascii values of the string together. or take the int at face value
            % capacity. store in the index.  
            check if there is a next
        '''
        if type(key.key) is str:
            summed = reduce(lambda acc,i: acc + ord(i),key.key,0)
            index = summed % self.capacity
            return index
        #key.key is int
        index = key.key % self.capacity
        return index

        # if type(key.key) is str:
        #     # for s in key:
        #     #     asciis.append(ord(s))
        #     summed = reduce(lambda acc,i: acc + ord(i),key.key,0)

        #     index = summed % self.capacity

        #     if self.storage[index] is None:
        #         self.storage[index] = key
        #     else: #key already exists at the hashed index:
        #         while self.storage[index].next:
        #             self.storage[index] = self.storage[index].next
        #         self.storage[index].next = key
        # else:
        #     index = key.key % self.capacity
        #     if self.storage[index] is None:
        #         self.storage[index] = key
        #     else:
        #         while self.storage[index].next:
        #             self.storage[index] = self.storage[index].next
        #         self.storage[index].next = key
        # return key


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        pass



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        pass


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass

ht = HashTable(10)

pair = LinkedPair('hello','world')
x = ht._hash(pair)

# print([key.value for key in ht.storage if key][0])
# pair2 = LinkedPair(50,'testing')
# x = ht._hash(pair2)

# for x in range(6):
#     key = random.randint(1,2000)
#     random.choice(string.ascii_letters)
#     # val = ''.join(random.choice(string.ascii_letters) for s in range(key))
#     val = ''.join(random.sample(string.ascii_letters,10))
#     pair = LinkedPair(key,val)
#     ht._hash(pair)

# print(ht)










# print([key.value for key in ht.storage if key])



# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
