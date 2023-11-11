from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Union, List


@dataclass
class Node:
    value: Any
    next: Node = None

    def __str__(self):
        return f"{self.value}"


@dataclass
class LinkedList:
    head: Union[Node, None] = None
    tail: Union[Node, None] = None

    def __len__(self) -> int:
        counter = 0
        node = self.head

        if self.head is None:
            return counter

        while node is not None:
            counter += 1
            node = node.next

        return counter

    def __str__(self) -> str:
        output = ""
        node = self.head

        if self.head is None:
            return ""

        while node.next is not None:
            output += f'{node.value} -> '
            node = node.next

        output += f'{node.value}'
        return output

    def add_node(self, value: Any) -> None:
        """
        Adds Node at the beginning of the Linked List
        """
        new_head = Node(value)
        new_head.next = self.head

        if self.head is None and self.tail is None:
            self.tail = new_head
        self.head = new_head

    def add_end_node(self, value: Any) -> None:
        """
        Adds Node at the end of the Linked List
        """
        new_tail = Node(value)
        if len(self) == 0:
            self.head = new_tail
        else:
            self.tail.next = new_tail
        self.tail = new_tail

    def find_by_idx(self, idx: int) -> Node:
        """
        Finds Node in the Linked List by given index
        """
        counter = 0
        node = self.head

        if len(self) <= idx:
            raise IndexError(f'Choose index from 0 to {len(self) - 1}')

        while counter != idx:
            counter += 1
            node = node.next

        return node

    def remove_end_node(self) -> None:
        """
        Removes the Node from the end of the Linked List
        """
        if self.head is self.tail:
            self.head, self.tail = None, None

        else:
            new_tail = self.find_by_idx(len(self) - 2)

            self.tail = new_tail
            self.tail.next = None

    def remove_head_node(self) -> None:
        """
        Removes the Node from the beginning of the Linked List
        """
        if self.head is self.tail:
            self.head, self.tail = None, None

        else:
            self.head = self.head.next

    def remove_middle_node(self, idx: int) -> None:
        """
        Removes the Node at the given index in the Linked List
        """
        if 1 > idx > len(self) - 2:
            raise IndexError(f"Choose index from range 1 to {len(self) - 2}")

        else:
            node = self.find_by_idx(idx - 1)
            node.next = node.next.next

    def create_from_array(self, values_array: List[Any]) -> None:
        """
        Creates Linked List from the array of values
        """
        for value in values_array[::-1]:
            self.add_node(value)

    def remove_duplicates(self) -> None:
        """
        Removes all value duplicates from Linked List
        """
        counter = 0
        values = set()
        node = self.head

        while node is not None:
            if node.value in values:
                if node is self.tail:
                    self.remove_end_node()
                else:
                    self.remove_middle_node(counter)
            else:
                values.add(node.value)
                counter += 1

            node = node.next
