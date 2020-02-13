import hashlib, functools,random,string
from KeyVal import KeyVal

class HashTable:
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
            return None
            # raise KeyError(key)
        
        if self.storage[index].key == key:
            return self.storage[index].value
        else:
            node = self.linked_list_search(index,key)
            if node.value == None:
                raise KeyError(key)
                return None
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
        print('in linked list insert')
        node = self.storage[i]
        print(node)
        
        while node:
            print(node.key,kv.key)
            if node.key == kv.key:
                node.value = kv.value
                break
            if node.next == None:
                node.next = kv
                break
            node = node.next

    def linked_list_search(self,i,key):
        node = self.storage[i]
        while node:
            if node.key == key:
                return node
            node = node.next
        return None

    def __repr__(self):
        return str(self.storage)


if __name__ == '__main__':

    def amir_test():
        obj = HashTable(10)
        keys = ['amir','sofia','sheena','nadia','ibby','yusuf']
        for n in keys:
            # key = ''.join(random.choices(string.ascii_letters, k=4))
            key = n
            val = ''.join(random.choices(string.digits,k=2))
            print(key,val)
            obj.insert(key,int(val))

        print(obj,'\n')
        # x = obj.retrieve('yusuf')
        obj.remove('nadia')
        obj.remove('ibby')
        obj.remove('amir')
        print(len(obj.storage))
        print(obj,'\n')

        obj.resize()

        print(len(obj.storage))
        print(obj, '\n')

        obj.insert('amir', 'bonafide')
        obj.retrieve('amir')
    # amir_test()

    ht = HashTable(8)
    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    ht.insert("key-6", "val-6")
    ht.insert("key-7", "val-7")
    ht.insert("key-8", "val-8")
    ht.insert("key-9", "val-9")

    ht.insert("key-0", "new-val-0")
    ht.insert("key-1", "new-val-1")
    ht.insert("key-2", "new-val-2")
    ht.insert("key-3", "new-val-3")
    ht.insert("key-4", "new-val-4")
    ht.insert("key-5", "new-val-5")
    ht.insert("key-6", "new-val-6")
    ht.insert("key-7", "new-val-7")
    ht.insert("key-8", "new-val-8")
    ht.insert("key-9", "new-val-9")

    a = ht.retrieve('key-0')
    b = ht.retrieve('key-1')
    c = ht.retrieve('key-2')
    d = ht.retrieve('key-3')
    e = ht.retrieve('key-4')
    f = ht.retrieve('key-5')
    g = ht.retrieve('key-6')
    h = ht.retrieve('key-7')
    i = ht.retrieve('key-8')
    # print(a,b,c,d,e,f,g,h,i)
    print(ht)
    ht.remove('key-0')
    print(ht)



# def linked_list_display(self,i):
    #     node = self.storage[i]
    #     while node:
    #         print(node)
    #         node = node.next

    
