from __future__ import annotations

from copy import deepcopy
from typing import Any, Optional, List


class TreeNode:
    def __init__(self, root_value: Any) -> None:
        self._value = root_value
        self._left: Optional[TreeNode] = None
        self._right: Optional[TreeNode] = None

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, new_value: Any) -> None:
        self._value = new_value

    @property
    def left(self) -> TreeNode:
        return self._left

    @property
    def right(self) -> TreeNode:
        return self._right

    @left.setter
    def left(self, new_value: TreeNode) -> None:
        self._left = new_value

    @right.setter
    def right(self, new_value: TreeNode) -> None:
        self._right = new_value

    def str(self) -> str:
        return f"Node: {self._value}"


class BST:
    def __init__(self) -> None:
        self._root = None
        self.__queue: List[TreeNode] = []

    @property
    def root(self) -> TreeNode:
        return self._root

    def create_bst_from_array(self, arr_values: List[Any]) -> TreeNode:
        nodes_values = deepcopy(arr_values)

        self._root = TreeNode(nodes_values.pop(0))
        self.__queue.append(self.root)

        while self.__queue:
            curr_node = self.__queue.pop(0)

            if not curr_node.left and nodes_values:
                child_node = TreeNode(nodes_values.pop(0))
                curr_node.left = child_node
                self.__queue.append(curr_node.left)

            if curr_node.right is None and nodes_values:
                child_node = TreeNode(nodes_values.pop(0))
                curr_node.right = child_node
                self.__queue.append(curr_node.right)
        return self.root

    def display_tree(self, node: Optional[TreeNode], tree_level=0) -> None:
        if node:
            self.display_tree(node.right, tree_level + 1)
            print(' ' * 4 * tree_level + '-> ' + str(node.value))
            self.display_tree(node.left, tree_level + 1)

    def reverse_tree(self, curr_node: Optional[TreeNode]):
        if curr_node:
            curr_node.left, curr_node.right = curr_node.right, curr_node.left

            self.reverse_tree(curr_node.left)
            self.reverse_tree(curr_node.right)

    def traverse_preorder(self, node: Optional[TreeNode], result: List[TreeNode] = None) -> List[TreeNode]:
        if node:
            result.append(node)
            self.traverse_preorder(node.left, result)
            self.traverse_preorder(node.right, result)
        return result

    def traverse_inorder(self, node: Optional[TreeNode], result: List[TreeNode] = None) -> List[TreeNode]:
        if node:
            self.traverse_inorder(node.left, result)
            result.append(node)
            self.traverse_inorder(node.right, result)
        return result

    def traverse_postorder(self, node: Optional[TreeNode], result: List[TreeNode] = None) -> List[TreeNode]:
        if node:
            self.traverse_postorder(node.left, result)
            self.traverse_postorder(node.right, result)
            result.append(node)
        return result

    def traverse_level_ordering(self) -> List[TreeNode]:
        result = []

        if self.root:
            self.__queue.append(self.root)

            while self.__queue:
                curr_node = self.__queue.pop(0)

                if curr_node:
                    result.append(curr_node)

                    if curr_node.left:
                        self.__queue.append(curr_node.left)

                    if curr_node.right:
                        self.__queue.append(curr_node.right)
        return result


def main():
    arr_list = [value for value in range(1, 16)]

    tree = BST()
    tree.create_bst_from_array(arr_list)
    tree.display_tree(tree.root)

    print(tree.traverse_preorder(node=tree.root, result=[]))
    print(tree.traverse_inorder(node=tree.root, result=[]))
    print(tree.traverse_postorder(node=tree.root, result=[]))
    print(tree.traverse_level_ordering())


if __name__ == "__main__":
    main()
