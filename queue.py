#!python
from stack import Node

class Queue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        # TODO: initialize instance variables
        self.head = None
        self.tail = None
        self.counter = 0
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({})'.format(self.length())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        return self.counter == 0

    def length(self):
        """Return the number of items in this queue"""
        return self.counter

    def peek(self):
        """Return the next item in this queue without removing it,
        or None if this queue is empty"""
        if self.head is None:
            return None
        else:
            return self.head.cargo

    def enqueue(self, item):
        """Enqueue the given item into this queue"""
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.counter = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.counter += 1


    def dequeue(self):
        """Return the next item and remove it from this queue,
        or raise ValueError if this queue is empty"""
        if self.head is None:
            raise ValueError("The Queue is empty!")
        else:
            old_head = self.head
            self.head = self.head.next
            old_head.next = None
            self.counter -= 1
            return old_head.cargo
