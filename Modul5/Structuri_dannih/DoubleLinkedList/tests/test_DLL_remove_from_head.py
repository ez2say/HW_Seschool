import pytest
from Modul5.Structuri_dannih.DoubleLinkedList.src.DoubleLinkedList import DoubleLinkedList

@pytest.fixture
def dll():
    return DoubleLinkedList()


@pytest.mark.parametrize("test_input, expected", [
    ([1, 2, 3], [3, 2, 1]),
    ([], []),
    (["a"], ["a"]),
])
def test_remove_from_head(dll, test_input, expected):
    for item in test_input:
        dll.add_at_head(item)
    result = []
    while not dll.is_empty():
        result.append(dll.remove_from_head())
    assert result == expected


#Временная сложность O(1) если прям с головы,если последовательно удалять то О(n)