import hashlib, functools,random,string
from KeyVal import KeyVal

class Hashtable:
    def __init__(self,capacity):
        self.capacity = capacity
        self.storage = [None]*capacity
    
    def insert(self,key,val):
        #hash the key to an index
        #insert the value at the hashed index
        # kv_pair = KeyVal(key,val)
        kv = KeyVal(key,val)
        index = self.__hash_modulo__(kv.key)
        if self.storage[index] == None:
            self.storage[index] = kv
        else:
            self.linked_list_insert(index, kv)

    def linked_list_display(self,i):
        node = self.storage[i]
        while node:
            print(node)
            node = node.next
    
    def linked_list_insert(self,i,kv):
        node = self.storage[i]
        while node.next:
            node = node.next
        node.next = kv

    def linked_list_search(self,i,key):
        node = self.storage[i]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def retrieve(self,key):
        index = self.__hash_modulo__(key)

        if self.storage[index] == None:
            raise KeyError(key)
            return
        
        if self.storage[index].key == key:
            return self.storage[index].value
        else:
            val = self.linked_list_search(index,key)
            if val == None:
                raise KeyError(key)
            return val

    def delete(self,val):
        pass

    def resize(self):
        pass

    def __hash_modulo__(self,key):
        key_list = [ord(c) for c in key]
        # print(key_list)
        integer = functools.reduce(lambda acc,num: acc + num, key_list)
        return integer % self.capacity
    
    def __str__(self):
        return str(self.storage)


obj = Hashtable(3)

keys = ['amir','sofia','sheena','nadia','ibby','yusuf']

for n in keys:
    # key = ''.join(random.choices(string.ascii_letters, k=4))
    key = n
    val = ''.join(random.choices(string.digits,k=2))
    print(key,val)
    obj.insert(key,int(val))


print(obj)

x = obj.retrieve('ibby')
print(x)




    
