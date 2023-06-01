#!/usr/bin/python3
"""Node Module"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a node of a singly linked list

        Args:
            data (int): node data
            next_node: address of the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrive data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Setter for data"""

        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieve address of next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set address of next node"""

        if (
                not isinstance(value, Node)
                and value is not None
                ):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines singly linked list"""

    def __init__(self):
        """Initializes the head of the singly linked list"""

        self.__head = None

    def __str__(self):
        """String representation of singly linked list"""

        result = ""
        current = self.__head
        while current:
            result += "{:d}".format(current.data)
            if current.next_node:
                result += "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """Inserts a new node into the correct sorted position in list"""

        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = self.__head
            self.__head = new_node
        elif self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
