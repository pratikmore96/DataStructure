class Tree:

    def __init__(self,data) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def create_child(self, child):
        child.parent = self
        self.children.append(child)

    def printtree(self):
        print(self.parent)
        print(self.data)
        print(self.children)
        

def create_hierarchy():
    
    root = Tree("electronic")

    laptop = Tree("laptop")
    laptop.create_child("hp")
    laptop.create_child("samsung")
    laptop.create_child("lenovo")

    tv = Tree("laptop")
    tv.create_child("hp")
    tv.create_child("samsung")
    tv.create_child("lenovo")

    root.create_child("laptop")
    root.create_child("tv")

    root.printtree()

if __name__ == '__main__':
    create_hierarchy()