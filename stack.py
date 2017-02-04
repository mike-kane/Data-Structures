#!python


class Node(object):

    def __init__(self, cargo):
        self.next = None
        self.cargo = cargo


class Stack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # TODO: initialize instance variables
        self.counter = 0
        self.head = None
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({})'.format(self.length())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        return (self.counter == 0)

    def length(self):
        """Return the number of items in this stack"""
        return self.counter

    def peek(self):
        """Return the top item on this stack without removing it,
        or None if this stack is empty"""
        if self.counter != 0:
            return self.head.cargo
        else:
            return None

    def push(self, item):
        """Push the given item onto this stack"""
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.counter = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.counter += 1


    def pop(self):
        """Return the top item and remove it from this stack,
        or raise ValueError if this stack is empty"""
        if self.is_empty():
            raise ValueError("The Stack is empty!")
        else:
            # set aside cargo from head
            # set head.next as head
            # remove pointer from current head
            #return cargo
            old_head = self.head
            new_head = old_head.next
            self.head = new_head
            old_head.next = None
            self.counter -= 1
            return old_head.cargo
