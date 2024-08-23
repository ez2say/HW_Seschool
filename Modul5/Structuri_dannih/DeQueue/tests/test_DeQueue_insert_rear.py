import pytest
from Modul5.Structuri_dannih.DeQueue.src import DeQueue

@pytest.fixture
def de_queue():
    return DeQueue()


@pytest.mark.parametrize("data_list, expected_result", [
    ([1, 2, 3], 3),
    ([], None),
    ([10], 10)
])
def test_insert_rear(de_queue, data_list, expected_result):
    for data in data_list:
        de_queue.insert_rear(data)
    assert de_queue.peek_rear() == expected_result

# Временная сложность O(1) поскольку добавление элемента в конец очереди не зависит от размера очереди