import pytest
from Modul5.Structuri_dannih.Queue.src import Queue

@pytest.fixture
def queue():
    return Queue()


@pytest.mark.parametrize("test_input, expected_result", [
    ([1, 2, 3], [1, 2, 3]),
    ([], []),
    (["a"], ["a"]),
])
def test_enqueue(queue, test_input, expected_result):
    for item in test_input:
        queue.enqueue(item)

    result = []
    while not queue.is_empty():
        result.append(queue.dequeue())

    assert result == expected_result

# Временная сложность O(1) так как мы всегда добавляем элементы в конец очереди