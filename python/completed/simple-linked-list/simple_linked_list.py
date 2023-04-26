from __future__ import annotations
from typing import Iterable


class Node:
    """
    A class representing a node in a linked list.

    Attributes:
        _value (int): The integer value stored in the node.
        _next (Node): The reference to the next node in the list.
    """

    def __init__(self, value: int) -> None:
        """
        Initializes a new node object.

        Args:
            value (int): The integer value to be stored in the node.
        """
        self._value = value
        self._next = None

    def value(self) -> int:
        """
        Returns the integer value stored in the node.

        Returns:
            int: The integer value stored in the node.
        """
        return self._value

    def next(self) -> Node:
        """
        Returns the reference to the next node in the list.

        Returns:
            Node: The reference to the next node in the list.
        """
        return self._next


class LinkedList:
    """
    A class representing a linked list data structure.

    Attributes:
        _values (list[int]): The list of integer values to be stored in the linked list.
        _nodes (list[Node]): The list of node objects representing the linked list.
    """

    def __init__(self, values: list[int] = None) -> None:
        """
        Initializes a new linked list object.

        Args:
            values (list[int], optional): The list of integer values to be stored in the linked list. Defaults to None.
        """
        self._values = list(values) if values else []
        self._nodes: list[Node] = []
        for v in self._values:
            self.push(v)

    def __len__(self) -> int:
        """
        Returns the number of elements in the linked list.

        Returns:
            int: The number of elements in the linked list.
        """
        return len(self._nodes)

    def __iter__(self) -> Iterable[int]:
        """
        Returns an iterator over the elements in the linked list.

        Returns:
            Iterable[int]: An iterator over the elements in the linked list.
        """
        for v in self._nodes[::-1]:
            yield v.value()

    def head(self) -> Node:
        """
        Returns the first node in the linked list.

        Returns:
            Node: The first node in the linked list.

        Raises:
            EmptyListException: If the linked list is empty.
        """
        if len(self._nodes) < 1:
            raise EmptyListException("The list is empty.")
        return self._nodes[-1]

    def push(self, value: int) -> None:
        """
        Inserts a new node with the given integer value at the beginning of the linked list.

        Args:
            value (int): The integer value to be inserted.
        """
        current = self.head() if self._nodes else None
        node = Node(value)
        node._next = current
        self._nodes.append(node)

    def pop(self) -> int:
        """
        Removes and returns the integer value stored in the first node of the linked list.

        Returns:
            int: The integer value stored in the first node of the linked list.

        Raises:
            EmptyListException: If the linked list is empty.
        """
        if len(self._nodes) < 1:
            raise EmptyListException("The list is empty.")
        return self._nodes.pop().value()

    def reversed(self) -> list[int]:
        return [node.value() for node in self._nodes]


class EmptyListException(Exception):
    """Exception raised when an operation is performed on an empty linked list."""

    def __init__(self, message: str):
        """Initializes an EmptyListException with the given message.

        Args:
            message (str): An explanation of the error.
        """
        self.message = message
