import pytest
from Modul5.Structuri_dannih.LinkedList.src import LinkedList

@pytest.fixture
def linked_list():
    return LinkedList()


@pytest.mark.parametrize("initial_values, value_to_delete, expected_result", [
    ([1, 2, 3], 2, 3),  # Positive test
    ([4, 5, 6, 7], 8, None),  # Negative test
    ([8], 8, None)  # Boundary test
])
def test_delete(linked_list, initial_values, value_to_delete, expected_result):
    for value in initial_values:
        linked_list.insert_at_end(value)
    linked_list.delete(value_to_delete)
    current = linked_list.head
    while current and current.next:
        current = current.next
    if current:
        assert current.data == expected_result
    else:
        assert current == expected_result

# Временная сложность О(n) - потому что в худшем случае нужно пройти весь список чтобы удалить элемент