class hashMap:
    def __init__(self) -> None:
        self.MAX = 10
        self.hashTable = [[] for i in range(self.MAX)]

    def gethash(self, item):
        hash = 0
        for char in item:
            hash += ord(char)
        hash %= self.MAX
        return hash

    def __setitem__(self, key, value):
        hash = self.gethash(key)
        found = False
        for idx, element in enumerate(self.hashTable[hash]):
            if len(element) == 2 and element[0] == key:
                found = True
                self.hashTable[hash][idx] = (key,value)
        if not found:
            self.hashTable[hash].append((key,value))

    def __getitem__(self, key):
        hash = self.gethash(key)
        for element in self.hashTable[hash]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, Key):
        print('entered')
        hash = self.gethash(Key)
        for itr, element in enumerate(self.hashTable[hash]):
            if element[0] == Key:
                del self.hashTable[hash][itr]
    
    def print(self):
        for ele in self.hashTable:
            print(ele)

if __name__ == '__main__':
    HM = hashMap()
    HM['Rahul'] = 25
    HM['pratik'] = 21
    HM['akshay'] = 13

    HM["march 6"] = 310
    HM["march 7"] = 420
    HM["march 8"] = 67
    HM["march 8"] = 2
    HM["march 17"] = 63457
    print(HM['Rahul'])
    print(HM['pratik'])
    HM['sad']
    print(HM['akshay'])

    HM.print()
    del HM['pratik']
    HM.print()