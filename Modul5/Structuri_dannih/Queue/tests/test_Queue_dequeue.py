import pytest
from Modul5.Structuri_dannih.Queue.src import Queue

@pytest.fixture
def queue():
    return Queue()

@pytest.mark.parametrize("test_input, expected", [
    ([1, 2, 3], 1),
    ([], None),
    (["a"], "a"),
])
def test_dequeue(queue, test_input, expected):
    for item in test_input:
        queue.enqueue(item)
    if expected is None:
        with pytest.raises(Exception):
            queue.dequeue()
    else:
        assert queue.dequeue() == expected

#Временная сложность О(1) так как мы всегда удаляем элементы из начала очереди