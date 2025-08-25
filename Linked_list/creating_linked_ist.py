class node:
    def __init__(self,value):
        self.data=value
        self.next=None;
#
# a=node(1)
# print(a.data)

class linked_list:
    def __init__(self):
        # empty linked list
        self.head=None
        # no of nodes in linked list
        self.n=0

    # dunder method for the len
    def __len__(self):
        return self.n
    # dunder method for the print
    def __str__(self):
        curr=self.head
        result=''
        while curr != None:
            result=result + str(curr.data) + '->'
            curr=curr.next
        return result[:-2]
    
    # creating nodes and there connection
    def insert_head(self,value):     
        # new node
        new_node=node(value)
        # create connection
        new_node.next=self.head
        # reassign head
        self.head=new_node
        # increment n
        self.n=self.n + 1

   
    # append at tail
    def append(self,value):
        # set the new node
        new_node=node(value)
        
        # if linked list is empty
        if self.head == None:
            self.head=new_node
            self.n= self.n + 1
            return

        curr=self.head

        while curr.next != None:
            curr=curr.next

        # you are at the last node
        curr.next= new_node
        self.n= self.n + 1


l=linked_list()

l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)

l.append(8)

print(len(l))

print(l)