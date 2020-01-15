# '''
# Linked List hash table key/value pair
# '''
import hashlib
import random
import string
from functools import reduce


class LinkedPair:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next = None
    def __repr__(self):
        return str({'key': self.key, 'value': self.value, 'next':self.next})

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
        if type(pair.key) is str:
            summed = reduce(lambda acc,i: acc + ord(i),pair.key,0)
            return summed

        return pair.key + random.randint(1,1000)


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

        pair = LinkedPair(key,value)
        index = self._hash_mod(pair)

        # print('self.storage[index]',self.storage[index])
        if self.storage[index] is None:
            self.storage[index] = pair
        else: #key already exists at the hashed index:
            pointer = self.storage[index]
            while pointer.next:
                pointer = pointer.next
            pointer.next = pair
        return (pair.key,pair.value)
    
    def display(self,po,pr,mes):
        print('pointer' + mes, po.key)
        print('prev' + mes, pr.key)
        print('\n')
        return

    def remove(self, key):

        pair = LinkedPair(key,None)
        index = self._hash_mod(pair)

        # if self.storage[index] is None:
        #     raise Exception('Key not found in the Hash Table')

        pointer = self.storage[index]
        prev = None
        while pointer:
            # self.display(pointer,prev, ' preshifting of pointer')
            if pointer.key == pair.key:
                if prev is None:  #at the beginning of the linked list, set the head to equal the next value
                    print(self.storage[index] == pointer)
                    self.storage[index] = self.storage[index].next #this modifies the value
                    # pointer = pointer.next  #this one doesn't
                    break
                # self.display(pointer,prev,' pointer == pair')
                prev.next = pointer.next
                del pointer
                break
            else:
                prev = pointer
                pointer = pointer.next
            
            # self.display(pointer,prev,' post shifting')
            # self.storage[index] = self.storage[index].next
        return -1

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        pair = LinkedPair(key,None)
        index = self._hash_mod(pair)
        if self.storage[index] is None:
            raise KeyError(key)
            return
        pointer = self.storage[index]
        while pointer.next:
            pointer = pointer.next
        return pointer.value
        # return self.storage[index].value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass

ht = HashTable(1)
pair = LinkedPair('hello','world')
# x = ht._hash(pair)
# x = ht._hash_mod(pair)
# print(x)
# a = ht.algorithm()
# print(a)

t = ht.insert('zero', 'abe')

u = ht.insert('one','amir')

w = ht.insert('two','sofia')

x = ht.insert('three','sheena')

y = ht.insert('four','nadia')

z = ht.insert('five','ibby')

# print(ht.storage[0].next.next.next.next.next)
# print(ht.storage[0])

# point = ht.storage[0]

# while point:
#     print(point)
#     print('\n')
#     point = point.next

print(ht.storage[0])
print('\n')

ht.remove('zero')
ht.remove('three')


print('after remove', ht.storage[0])

# point = ht.storage[0].next
# point = ht.storage[0]
# while point:
#     print(point)
#     print('\n')
#     point = point.next




# y = ht.remove('two')
# print(ht.storage[0])



# z = ht.retrieve('hello')
# print(z)







# hashed_indexes = []

#hashed strings***************
# for s in range(6):
#     key = random.randint(1,2000)
#     # val = ''.join(random.choice(string.ascii_letters) for s in range(key))
#     val = ''.join(random.sample(string.ascii_letters,10))
#     pair = LinkedPair(key,val)
#     x = ht._hash_mod(pair)
#     hashed_indexes.append(x)

#hashed integers***************
# for n in range(8):
#     key = random.randint(1,2000)
#     val = random.randint(1,2000)
#     pair = LinkedPair(key,val)
#     x = ht._hash_mod(pair)
#     hashed_indexes.append(x)

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
