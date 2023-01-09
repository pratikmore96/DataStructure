class Node:
    
    def __init__(self, data, next) -> None:

        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self) -> None:
        
        self.head = None

    def add_at_beginning(self, data):

        if self.head == None:
            node = Node(data,None)
            self.head = node
            return

        node = Node(data, self.head)
        self.head = node
    
    def add_at_end(self, data):
        
        if self.head == None:
            node = Node(data,None)
            self.head = node
            return
        
        itr = self.head

        while itr:
            if itr.next == None:
                node = Node(data,None)
                itr.next = node
                return
            itr = itr.next

    def create_linklist(self, Data):
        
        if self.head != None:
            raise Exception('The list have some elements')
        else:    
            for data in Data:
                self.add_at_end(data)
            
    def remove_first_element(self):
        if self.head==None:
            raise Exception ("the list is empty cannot be removed")

        self.head = self.head.next
        
    def remove_last_element(self):
        if self.head==None:
            raise Exception("the list is empty cannot be removed")

        itr = self.head
        if itr.next == None:
            self.head = None
            return

        while itr:
            if itr.next.next == None:
                itr.next = None
            itr = itr.next


    def add_at_index(self, index, data):

        if(index < 0 or index > (self.find_length_of_list())):
            raise Exception("Please enter correct index")

        counter = 0
        itr = self.head
        if counter == index:
            node = Node(data, itr)
            self.head =node
            return

        while itr:
            if counter == index-1:
                node = Node(data, itr.next)
                itr.next = node
                return
            itr = itr.next
            counter += 1

    def remove_at_index(self, index):

        if(index < 0 or index > (self.find_length_of_list())):
            raise Exception("Please enter correct index")

        counter = 0
        itr = self.head
        if counter == index:
            if itr.next != None:
                self.head = itr.next
            else:
                self.head = None    
            return


        while itr:
            if counter == index-1:
                if itr.next.next == None:
                    itr.next = None
                else:
                    itr.next = itr.next.next
                return
            counter += 1
            itr = itr.next


    def find_length_of_list(self):
        length = 1
        if self.head == None:
            return 0
        itr = self.head
        while itr:
            if itr.next == None:
                return length
            length += 1
            itr = itr.next
    
    def print(self):

        if self.head == None:
            raise Exception ("Empty list")
        
        itr = self.head
        list = ""
        while itr:
            list += str(itr.data) + "--->" if itr.next != None else str(itr.data)
            itr = itr.next
        print(list)

if __name__ == '__main__':

    ll = LinkedList()
    print(ll.find_length_of_list())

    ll.add_at_beginning(12)
    # ll.add_at_beginning(33)
    # ll.add_at_end(8)
    # ll.add_at_end(89)
    print(ll.find_length_of_list())
    ll.remove_first_element()
    print(ll.find_length_of_list())
    ll.create_linklist([10,20,30,40])
    ll.print()
    # ll.remove_first_element()
    # ll.print()
    # ll.remove_last_element()
    ll.add_at_index(0,22)
    ll.print()
    ll.add_at_index(1,33)
    ll.print()
    ll.add_at_index(3,44)
    ll.print()
    ll.add_at_index(7,44)
    ll.print()
    ll.add_at_index(5,44)
    ll.print()
    ll.remove_at_index(0)
    ll.print()
    ll.remove_at_index(7)
    ll.print()
    ll.remove_at_index(3)
    ll.print()
    