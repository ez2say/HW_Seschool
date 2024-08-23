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
def test_add_at_tail(dll, test_input, expected):
    dll.add_at_tail(test_input)
    assert (dll.tail.data == test_input) == expected


#Временная сложность О(1) вставка происходит по тому же принципу что и в голову - сложность одинаковая
