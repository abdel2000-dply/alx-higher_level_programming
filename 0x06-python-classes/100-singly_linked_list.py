#!/usr/bin/python3
"""This is a Node"""


class Node:
    """class Node"""

    def __init__(self, data, next_node=None):
        """
        Init a Node

        Args:
            data (int): The data value to be stored in the node.
            next_node (Node, optional): The next node.
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns: data"""
        return self.__data

    @data.setter
    def data(self, n):
        """Set data"""
        if type(n) is not int:
            raise TypeError('data must be an integer')
        self.__data = n

    @property
    def next_node(self):
        """Get next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, n):
        """Set next_node"""
        if type(n) is not Node and n is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = n


class SinglyLinkedList:
    """Sinlgy Linked List"""

    def __init__(self):
        """Init empty list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a node"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            curr = self.__head
            while curr.next_node is not None and value > curr.next_node.data:
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        """Str representation"""
        curr = self.__head
        result = ""
        while curr is not None:
            result += str(curr.data)
            curr = curr.next_node
            if curr is not None:
                result += "\n"
        return result
