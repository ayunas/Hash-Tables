import hashlib, functools
from KeyVal import KeyVal

class Hashtable:
    def __init__(self,capacity):
        self.capacity = capacity
        self.storage = [None]*capacity
    
    def insert(self,key,val):
        #hash the key to an index
        #insert the value at the hashed index
        # kv_pair = KeyVal(key,val)
        index = self.__hash_modulo__(key)
        # print(index)
        self.storage[index] = val

    def retrieve(self,key):
       index = self.__hash_modulo__(key)
       return self.storage[index]

    def delete(self,val):
        pass

    def resize(self):
        pass

    def __hash_modulo__(self,key):
        key_list = [ord(c) for c in key]
        # print(key_list)
        integer = functools.reduce(lambda acc,num: acc + num, key_list)
        return integer % self.capacity


obj = Hashtable(10)

obj.insert('amir',38)

val = obj.retrieve('amir')

obj.insert('nancy',22)

v = obj.retrieve('nancy')
print(v)

x = obj.retrieve('amir')
print(x)


    
