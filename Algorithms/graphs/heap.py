import random
from typing import List

from binary_tree import BST, TreeNode


class HeapMax(BST):
    def __init__(self):
        super().__init__()

    def heapify_bst(self, descending: bool = True) -> None:
        """
        Converts a Binary Search Tree (BST) into a max or min heap based on the specified order.
        """

        list_of_nodes = self.traverse_level_ordering()
        last_internal_parent_idx = len(list_of_nodes) // 2 - 1

        if descending:
            for parent_index in range(last_internal_parent_idx, -1, -1):
                self.__heapify_max(list_of_nodes, parent_index)

        else:
            for parent_index in range(last_internal_parent_idx, -1, -1):
                self.__heapify_min(list_of_nodes, parent_index)

    def __heapify_min(self, list_of_nodes: List[TreeNode], parent_node_idx: int) -> None:
        """
        Rearranges the values of tree nodes to apply the properties of a min heap
        """

        if parent_node_idx >= len(list_of_nodes):
            return

        parent_node = list_of_nodes[parent_node_idx]
        left_node_idx = 2 * parent_node_idx + 1
        right_node_idx = 2 * parent_node_idx + 2

        if parent_node.left and parent_node.value > parent_node.left.value:
            parent_node.value, parent_node.left.value = parent_node.left.value, parent_node.value
            self.__heapify_min(list_of_nodes, left_node_idx)

        if parent_node.right and parent_node.value > parent_node.right.value:
            parent_node.value, parent_node.right.value = parent_node.right.value, parent_node.value
            self.__heapify_min(list_of_nodes, right_node_idx)

    def __heapify_max(self, list_of_nodes: List[TreeNode], parent_node_idx: int) -> None:
        """
        Rearranges the values of tree nodes to apply the properties of a max heap
        """

        if parent_node_idx >= len(list_of_nodes):
            return

        parent_node = list_of_nodes[parent_node_idx]
        left_node_idx = 2 * parent_node_idx + 1
        right_node_idx = 2 * parent_node_idx + 2

        if parent_node.left and parent_node.value < parent_node.left.value:
            parent_node.value, parent_node.left.value = parent_node.left.value, parent_node.value
            self.__heapify_max(list_of_nodes, left_node_idx)

        if parent_node.right and parent_node.value < parent_node.right.value:
            parent_node.value, parent_node.right.value = parent_node.right.value, parent_node.value
            self.__heapify_max(list_of_nodes, right_node_idx)


def main():
    arr_list = [random.randint(0, 101) for _ in range(1, 16)]

    tree = HeapMax()
    tree.create_bst_from_array(arr_list)

    tree.heapify_bst(descending=False)
    tree.display_tree(tree.root)


if __name__ == "__main__":
    main()
