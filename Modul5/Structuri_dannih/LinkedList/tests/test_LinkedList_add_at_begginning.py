import pytest
from Modul5.Structuri_dannih.LinkedList.src import LinkedList

@pytest.fixture
def linked_list():
    return LinkedList()


@pytest.mark.parametrize("value, expected_result", [
    (5, 5),
    ("test", None),
    (0, 0)
])
def test_insert_at_beginning(linked_list, value, expected_result):
    linked_list.insert_at_beginning(value)
    assert linked_list.head.data == expected_result

# Временная сложность О(1) - потому что операция происходит только в начало списка,ничего искать не нужно
# - тупо воткнуть первым
