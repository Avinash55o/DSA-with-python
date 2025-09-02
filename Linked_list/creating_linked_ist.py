class node:
    def __init__(self,value):
        self.data=value
        self.next=None;
#
# a=node(1)
# print(a.data)

class linked_list:
    # TO CREATE ANN EMPTY HEAD
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
        # print(f'type of result is {type(result)}')
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
    
    # Insert in the middle
    def insert_after(self,after,value):
        # create node
        new_node=node(value)

        #Run the while loop 
        curr=self.head
        while curr != None:
            if curr.data == after:
                break
            curr=curr.next
        
        # case 1 if loop find the after value and it break then give the result
        # case 2 if loop run totally when no is not fined then we have a else case

        if curr != None:
            new_node.next= curr.next
            curr.next = new_node
        else:
            return 'after value not found!'
        
    # FOR EMPTY LINKED LIST
    def clear(self):
        self.head=None
        self.n=0
   
    # TO DELETE THE HEAD
    def delete_head(self):
        if self.head == None:
            print("linked list is empty")
        else:
            self.head= self.head.next
            self.n= self.n -1
    
    # POP FUNCTION OR DELETE FROM THE END
    def pop(self):

        # if linked list is empty:
        if self.head == None:
            print('empty list')

        curr=self.head

        # what if only one item is their
        if curr.next == None:
            # use the delete head function
            self.delete_head()

        while curr.next.next != None:
            curr= curr.next
        # while will give the second last node in the linked list
        curr.next= None
        self.n= self.n -1
    
    # REMOVE BY VALUE
    def remove(self, value):
        # if the linked list is empty
        if self.head== None:
            return 'empty linkedlist'
        # if head is the value the user give which has no before node
        if self.head == value:
            return self.delete_head()
        curr=self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr=curr+1

        # now there are two case --> WE GET THE NO or  WE DIDN'T GET THE NO
        if curr.next == None:
            return 'not found'
        else:
            curr.next= curr.next.next



l=linked_list()

l.insert_head(4)
l.insert_head(3)
l.insert_head(2)
l.insert_head(1)

l.append(8)

print(len(l))
l.insert_after(4,12)
print(l)
l.delete_head()
print(l)