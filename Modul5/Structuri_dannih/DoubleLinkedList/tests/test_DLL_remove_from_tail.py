import pytest
from Modul5.Structuri_dannih.DoubleLinkedList.src.DoubleLinkedList import DoubleLinkedList

@pytest.fixture
def dll():
    return DoubleLinkedList()


@pytest.mark.parametrize("test_input, expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([], []),
    (["a"], ["a"]),
])
def test_remove_from_tail(dll, test_input, expected):
    for item in test_input:
        dll.add_at_tail(item)
    result = []
    while not dll.is_empty():
        result.append(dll.remove_from_tail())
    assert result == expected



#Временная сложность О(n) такая же фигня что и с головой