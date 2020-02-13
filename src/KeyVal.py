import json

class KeyVal:
    def __init__(self,key,val):
        self.key = key
        self.value = val
        self.next = None
    
    def __repr__(self):
        kv = {self.key : self.value, 'next' : self.next}
        return str(kv)
