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

    def retrieve(self,key):
        index = self.__hash_modulo__(key)

        if self.storage[index] == None:
            raise KeyError(key)
            return
        
        if self.storage[index].key == key:
            return self.storage[index].value
        else:
            node = self.linked_list_search(index,key)
            if node.value == None:
                raise KeyError(key)
            return node.value

    def remove(self,key):
        index = self.__hash_modulo__(key)

        node = self.storage[index]
        prev = None

        if node.key == key:
            self.storage[index] = self.storage[index].next
            return -1

        while node:
            if node.key == key:
                prev.next = node.next
                return -1
            prev = node
            node = node.next

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        keyvals = [*filter(lambda kv: kv, self.storage)]
        print('keyvals', keyvals)

        self.capacity += self.capacity
        self.storage = [None]*self.capacity

        for kv in keyvals:
            # index = self.__hash_modulo__(kv.key)
            if kv.next == None:
                self.insert(kv.key,kv.value)
            else:
                node = kv
                while node:
                    self.insert(node.key,node.value)  
                    node = node.next

    def __hash_modulo__(self,key):
        key_list = [ord(c) for c in key]
        # print(key_list)
        integer = functools.reduce(lambda acc,num: acc + num, key_list)
        return integer % self.capacity
    
    def linked_list_insert(self,i,kv):
        node = self.storage[i]
        while node.next:
            node = node.next
        node.next = kv

    def linked_list_search(self,i,key):
        node = self.storage[i]
        while node:
            if node.key == key:
                return node
            node = node.next
        return None

    def __repr__(self):
        return str(self.storage)


obj = Hashtable(10)

keys = ['amir','sofia','sheena','nadia','ibby','yusuf']

for n in keys:
    # key = ''.join(random.choices(string.ascii_letters, k=4))
    key = n
    val = ''.join(random.choices(string.digits,k=2))
    print(key,val)
    obj.insert(key,int(val))


# print(obj)
# x = obj.retrieve('yusuf')
# obj.remove('nadia')
# obj.remove('ibby')
# obj.remove('amir')
print(len(obj.storage))
print(obj,'\n')

obj.resize()

print(len(obj.storage))
print(obj, '\n')




# def linked_list_display(self,i):
    #     node = self.storage[i]
    #     while node:
    #         print(node)
    #         node = node.next

    
