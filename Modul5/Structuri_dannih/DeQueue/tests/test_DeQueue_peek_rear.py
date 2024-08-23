import pytest
from Modul5.Structuri_dannih.DeQueue.src import DeQueue


@pytest.fixture
def de_queue():
    return DeQueue()


@pytest.mark.parametrize("initial_data, expected_result", [
    ([1, 2, 3], 3),
    ([4, 5, 6, 7], 7),
    ([8], 8),
    ([], None)
])
def test_peek_rear(de_queue, initial_data, expected_result):
    for data in initial_data:
        de_queue.insert_rear(data)
    if expected_result is not None:
        assert de_queue.peek_rear() == expected_result
    else:
        with pytest.raises(AssertionError):
            de_queue.peek_rear()

#Временная сложность O(n) А если много элементов? Это надо через все пройти,эт долго