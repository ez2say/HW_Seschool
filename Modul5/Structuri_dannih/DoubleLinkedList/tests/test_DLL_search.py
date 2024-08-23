import pytest
from Modul5.Structuri_dannih.DoubleLinkedList.src.DoubleLinkedList import DoubleLinkedList

@pytest.fixture
def dll():
    return DoubleLinkedList()


@pytest.mark.parametrize("test_input, search_input, expected", [
    ([1, 2, 3], 2, True),
    ([1, 2, 3], 4, False),
    ([], 1, False),
])
def test_search(dll, test_input, search_input, expected):
    for item in test_input:
        dll.add_at_tail(item)
    assert dll.search(search_input) == expected


#Временная сложность О(n) так как мы осуществляем поиск элемента после добавления всех элементов