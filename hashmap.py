class hashMap:
    def __init__(self) -> None:
        self.MAX = 100
        self.hashTable = [None for i in range(self.MAX)]

    def gethash(self, item):
        hash = 0
        for char in item:
            hash += ord(char)
        hash %= self.MAX
        return hash

    def __setitem__(self, key, value):
        hash = self.gethash(key)
        self.hashTable[hash] = value
        return

    def __getitem__(self, key):
        hash = self.gethash(key)
        value = self.hashTable[hash]
        return value
    
    def print(self):
        for ele in self.hashTable:
            print(ele)

if __name__ == '__main__':
    HM = hashMap()
    HM['Rahul'] = 25
    HM['pratik'] = 21
    HM['akshay'] = 13
    print(HM['Rahul'])
    print(HM['pratik'])
    print(HM['akshay'])

    HM.print()