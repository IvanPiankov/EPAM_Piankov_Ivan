from typing import Union

import pytest

from homework7.task1.find_occurrences import find_occurrences, search_elem

empty_tree = {}

example_tree = {
    "first": ["RED", False],
    "second": {
        "simple_key": ["simple", 2, "of", "RED", "valued"],
    },
    "third": {
        "abc": False,
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", 2, {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


@pytest.mark.parametrize(
    ["tree", "element", "expected_result"],
    [
        (empty_tree, "RED", 0),
        (example_tree, "RED", 6),
        (empty_tree, False, 0),
        (example_tree, False, 2),
        (empty_tree, 2, 0),
        (example_tree, 2, 2),
    ],
)
def test_for_element_search_empty_and_not_empty_tree(
    tree: dict, element: Union[str, bool, int], expected_result: int
):
    assert find_occurrences(tree, element) == expected_result
