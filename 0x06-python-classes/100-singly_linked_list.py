#!/usr/bin/python3
"""This module is about defining asingly linked
    using class
"""


class Node:
    def __init__(self, data, next_node=None):
        """
        Initiaze a Node class

        Args:
            data(int): data of node
            next_node: points to next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for data

        Returns: Value of data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter for next_node

        Returns: next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for next node
        Args:
            Value: value of next node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Class representing a singly linked list """

    def __str__(self):
        """Defines the object
        """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """
        Initiat the list attribute
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Sorts the list

        Args:
            value: value of sorted nodes
        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
