import pytest
from Modul5.Structuri_dannih.DeQueue.src import DeQueue

@pytest.fixture
def de_queue():
    return DeQueue()


@pytest.mark.parametrize("data, expected_result", [
    (5, 5),
    (None, None),
    (0, 0)
])
def test_insert_front(de_queue, data, expected_result):
    de_queue.insert_front(data)
    assert de_queue.peek_front() == expected_result

# Временная сложность O(1)- операция вставки в начало очереди не зависит от размера очереди
