class Tree:

    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
 
    def __str__(self):
        print("dddd")
    def __repr__(self): 
        pass
    def __
    def printtree(self):
        # # print(self.parent)
        # print(self.data)
        # # print(self.children)
        # if self.children:
        #     for child in self.children:
        #         child.print_tree()
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printtree()

    def create_child(self, child):
        child.parent = self
        self.children.append(child)        

def create_hierarchy():
    
    root = Tree("electronic")

    laptop = Tree("Laptop")
    laptop.create_child(Tree("hp"))
    laptop.create_child(Tree("samsung"))
    laptop.create_child(Tree("lenovo"))

    tv = Tree("TV")
    tv.create_child(Tree("sonata"))
    tv.create_child(Tree("samsung"))
    tv.create_child(Tree("rocky"))

    root.create_child(laptop)
    root.create_child(tv)

    root.printtree()
    print(root)

if __name__ == '__main__':
    create_hierarchy()