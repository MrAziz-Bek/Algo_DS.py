from linked_list import Node, LinkedList

llist = LinkedList()
llist.head = Node('Mon')
tue = Node('Tue')
wed = Node('Wed')
thu = Node('Thu')

llist.head.next = tue
tue.next = wed
wed.next = thu

llist.push('Sun')
llist.insert_after(llist.head.next, 'Mon evening')
llist.append('Fri')
llist.delete_node('Sun')
llist.delete_node('Mon evening')
llist.print_list()