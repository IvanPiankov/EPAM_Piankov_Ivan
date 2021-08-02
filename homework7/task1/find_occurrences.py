"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Generator, Union


def search_elem(
    tree_leaf: Union[str, list, tuple, dict, set, int, bool]
) -> Generator[Union[str, int, bool], None, None]:
    """
    Function return elements which type ste, bool or int
    :param tree_leaf: dictionary tree
    :return: element of dictionary tree
    """
    for leaf in tree_leaf:
        if isinstance(leaf, (str, bool, int)):
            yield leaf
        elif isinstance(leaf, dict):
            for micro_leaf in search_elem(leaf.values()):
                yield micro_leaf
        else:
            for nano_leaf in search_elem(leaf):
                yield nano_leaf


def find_occurrences(tree: dict, element: Any) -> int:
    """
    Function which start process for search element in dictionary tree
    :param tree: dictionary tree
    :param element: element which will be found
    :return: number of element in tree
    """
    counter = 0
    for value in search_elem(tree.values()):
        if value == element:
            counter += 1
    return counter
