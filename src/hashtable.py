# '''
# Linked List hash table key/value pair
# '''
import hashlib
import random
import string
from functools import reduce


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

    def primes(self,num):
        # span = [*range(num,2,-1)]
        span = [num for num in range(num-1,1,-1)]
        print(span)
        print(range(span[0],1,-1))
        for elem in span:
            for i in range(elem-1,1,-1):
                print('elem',elem,'i',i)
                if (elem % i) == 0:
                    break
            else:
                return elem
    def algorithm(self):
        return '''Algorithm:
1.Create a Linked Pair passing in key and val\n
2.If key is string:
    -Sum all the ascii values of the string together.
If the key is an int:
    - add a random # to the int\n
3. Calculate Index using the division method: Integer % Storage Capacity\n
4. Check if there is a key at the index calculated.  If there is, traverse till no key.next\n
5. Store the val of the key at the end of the linked list of the index position calculated\n
'''
            
    def _hash(self, pair):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
       
        # largeprime = self.primes(self.capacity)

        if type(pair.key) is str:
            summed = reduce(lambda acc,i: acc + ord(i),pair.key,0)
            # index = summed % largeprime
            return summed

        # index = key.key % largeprime
        return pair.key + random.randint(1,1000)

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


    def _hash_mod(self, pair):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(pair) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        pair = LinkedPair(key,value)
        index = self._hash_mod(pair)

        print('index',index)
        print(pair.key)
        print(pair.value)
        print(self.storage)

        if self.storage[index] is None:
            self.storage[index] = pair
        else: #key already exists at the hashed index:
            while self.storage[index].next:
                self.storage[index] = self.storage[index].next
                self.storage[index].next = pair
    
        return (pair.key,pair.value)
        # else:
        #     index = key.key % self.capacity
        #     if self.storage[index] is None:
        #         self.storage[index] = key
        #     else:
        #         while self.storage[index].next:
        #             self.storage[index] = self.storage[index].next
        #         self.storage[index].next = key
        # return key



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
# x = ht._hash(pair)
# x = ht._hash_mod(pair)
# print(x)
# a = ht.algorithm()
# print(a)
x = ht.insert('hello','world')
print(x)


hashed_indexes = []

#hashed strings***************
for s in range(6):
    key = random.randint(1,2000)
    # val = ''.join(random.choice(string.ascii_letters) for s in range(key))
    val = ''.join(random.sample(string.ascii_letters,10))
    pair = LinkedPair(key,val)
    x = ht._hash_mod(pair)
    hashed_indexes.append(x)

#hashed integers***************
for n in range(8):
    key = random.randint(1,2000)
    val = random.randint(1,2000)
    pair = LinkedPair(key,val)
    x = ht._hash_mod(pair)
    hashed_indexes.append(x)

# print(hashed_indexes)
# indexes = []
# for v in hashed_ints:
#     indexes.append((v % 10))

# print(indexes)






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
