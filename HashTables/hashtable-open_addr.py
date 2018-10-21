class dictKeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def get_key(self):
        return self.key
    
    def set_key(self, key):
        self.key = key
        
    def __str__(self):
        return str(self.key) + ":" + self.value
    
#node for each singly linked list
class Node:
    def __init__(self, value):
        #info will store the address of dictKeyValue instance
        self.info = value
        #link will store the address of next node
        self.link = None
    
#class for singly linked list
class singlyLinkedList:
    def __init__(self):
        #store the address of first node
        self.start = None
        
    def display_list(self):
        if self.start is None:
            print("___")
            return
        p = self.start
        while p is not None:
            print(p.info, " ", end="")
            p = p.link
        print()
        
    def search(self, x):
        p = self.start
        while p is not None:
            if p.info.get_key() == x:
                return p.info
            p = p.link
        else:
            return None
            
    def insert_in_begin(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp
        
    def delete_node(self, x):
        if self.start is None:
            return
        
        #Deletion of first Node
        if self.start.info.get_key() == x:
            self.start = self.start.link
            return
        
        #deletion in between or end
        p = self.start
        while p.link is not None:
            if p.link.info.get_key() == x:
                break
            p = p.link
            
        if p.link is None:
            print("elem not in list")
        else:
            p.link = p.link.link
            

#class for the hash table array/list
class Hash:
    
    def __init__(self, size):
        self.tablesize = size
        self.hashtable = [None]*self.tablesize
        self.filled_slots = 0
        
    def hash1(self, key):
        if type(key) == str:
                sum1 = self.SumofAsciiCode(key)
                hf = sum1 % self.tablesize
                return hf
        else:
            return key % self.tablesize
        
    def SumofAsciiCode(self, key):
        #only fpr inserting strings
        sum1 = 0
        n = len(key)
        for j in range(0, n):
            sum1 = sum1 + ord(key[j])  
        return sum1
    
        
    def display_table(self):     
        print()
        for i in range(self.tablesize):
            print("[", i, "] -->  ", end="")
            if self.hashtable[i] != None:
                self.hashtable[i].display_list()
            else:
                print("___")

    def search(self, key):
        pos = self.hash1(key)
        if self.hashtable[pos] != None:
           return self.hashtable[pos].search(key)           
        return None
    
    def insert(self, newItem):
        
        key = newItem.get_key()
        pos = self.hash1(key)
        
        if self.hashtable[pos] is None:
            self.hashtable[pos] = singlyLinkedList()
        self.hashtable[pos].insert_in_begin(newItem)
        self.filled_slots +=1


    def delete(self, key):
        pos = self.hash1(key)
        
        if self.hashtable[pos] != None:
            self.hashtable[pos].delete_node(key)
            self.filled_slots -= 1
        else:
            print("Value not present")

#create an instance of Hash class with 11 items in the list
htable = Hash(11)

#create 10 instances of key value pair and store their address
#in each linked list nodes. 
anewItem =   dictKeyValue(1, "John Doe")
anewItem2 =  dictKeyValue(2, "Sally Smith")
anewItem3 =  dictKeyValue('Mic', "Mickey")
anewItem4 =  dictKeyValue('Nig', "Nightingale")
anewItem5=   dictKeyValue('Avi', "Aviator")
anewItem6 =  dictKeyValue('Beb', "Beboing")
anewItem7 =  dictKeyValue(5, "AV")
anewItem8 =  dictKeyValue(55, "Sam")
anewItem9 =  dictKeyValue(77, "Victoria")
anewItem10 =  dictKeyValue(65, "Sallie Mae")


#store the address of each node of the linked list in HashTable list postiion
#Store the address of info column of each linked list node
htable.insert(anewItem)
htable.insert(anewItem2)
htable.insert(anewItem3)
htable.insert(anewItem4)
htable.insert(anewItem5)
htable.insert(anewItem6)
htable.insert(anewItem7)
htable.insert(anewItem8)
htable.insert(anewItem9)
htable.insert(anewItem10)

print()
htable.display_table()

#search
print()
item_found = htable.search(anewItem3.get_key())
print(item_found)
item_found = htable.search(anewItem2.get_key())
print(item_found)
#delete
htable.delete('Nig')
#htable.display_table()
print()
htable.display_table()


"""
[ 0 ] -->  77:Victoria  55:Sam  Nig:Nightingale  
[ 1 ] -->  Beb:Beboing  1:John Doe  
[ 2 ] -->  Avi:Aviator  2:Sally Smith  
[ 3 ] -->  ___
[ 4 ] -->  ___
[ 5 ] -->  5:AV  
[ 6 ] -->  Mic:Mickey  
[ 7 ] -->  ___
[ 8 ] -->  ___
[ 9 ] -->  ___
[ 10 ] -->  65:Sallie Mae  

Mic:Mickey
2:Sally Smith


[ 0 ] -->  77:Victoria  55:Sam  
[ 1 ] -->  Beb:Beboing  1:John Doe  
[ 2 ] -->  Avi:Aviator  2:Sally Smith  
[ 3 ] -->  ___
[ 4 ] -->  ___
[ 5 ] -->  5:AV  
[ 6 ] -->  Mic:Mickey  
[ 7 ] -->  ___
[ 8 ] -->  ___
[ 9 ] -->  ___
[ 10 ] -->  65:Sallie Mae  
"""

        
    