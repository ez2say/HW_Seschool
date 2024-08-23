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
def test_peek(queue, test_input, expected):
    for item in test_input:
        queue.enqueue(item)
    if expected is None:
        with pytest.raises(Exception):
            queue.peek()
    else:
        assert queue.peek() == expected

#Временная сложность O(1) так как мы просто возвращаем данные из первого узла без его удаления