#!/usr/bin/python3
"""a class Node that defines a node of a singly linked list"""


class Node:
    """initializing class with private instance attributes data & next_node"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
        """instantiating the private instance

        Args:
            data (int): value of data for a singly linked list
            next_node: address of the next node in the list
        """

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""a class SinglyLinkedList that defines a singly linked list"""


class SinglyLinkedList:
    """initiatlizing the private instance attribute head"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        newnode = Node(value)
        if self.__head is None:
            newnode.next_node = None
            self.__head = newnode
        elif self.__head.data > value:
            newnode.next_node = self.__head
            self.__head = newnode
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            newnode.next_node = temp.next_node
            temp.next_node = newnode

    def __str__(self):
        """Defining the print() representation of a SinglyLinkedList"""
        sort_list = []
        temp = self.__head
        while temp is not None:
            sort_list.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(sort_list))
