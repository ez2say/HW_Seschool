import pytest
from Modul5.Structuri_dannih.LinkedList.src import LinkedList

@pytest.fixture
def linked_list():
    return LinkedList()

@pytest.mark.parametrize("values, expected_result", [
    ([1, 2, 3], 3),  # Positive test
    ([], None),  # Negative test
    ([10], 10)  # Boundary test
])
def test_insert_at_end(linked_list, values, expected_result):
    for value in values:
        linked_list.insert_at_end(value)
    current = linked_list.head
    while current.next:
        current = current.next
    assert current.data == expected_result

# Временная сложность О(n) - потому что в худшем случае нужно пройти весь список чтобы добавить элементы в конец