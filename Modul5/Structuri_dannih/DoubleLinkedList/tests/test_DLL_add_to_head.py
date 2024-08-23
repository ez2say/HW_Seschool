import pytest
from Modul5.Structuri_dannih.DoubleLinkedList.src.DoubleLinkedList import DoubleLinkedList

@pytest.fixture
def dll():
    return DoubleLinkedList()

@pytest.mark.parametrize("test_input, expected", [
    (1, True),
    ("a", False),
    (None, False),
])
def test_add_at_head(dll, test_input, expected):
    dll.add_at_head(test_input)
    assert (dll.head.data == test_input) == expected


#Временная сложность O(1), так как мы просто создаем новый узел и меняем ссылки