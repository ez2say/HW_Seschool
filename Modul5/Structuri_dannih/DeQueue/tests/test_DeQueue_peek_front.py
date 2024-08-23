import pytest
from Modul5.Structuri_dannih.DeQueue.src import DeQueue


@pytest.fixture
def de_queue():
    return DeQueue()


@pytest.mark.parametrize("initial_data, expected_result", [
    ([1, 2, 3], 1),
    ([4, 5, 6, 7], 4),
    ([8], 8),
    ([], None)
])
def test_peek_front(de_queue, initial_data, expected_result):
    for data in initial_data:
        de_queue.insert_front(data)
    if expected_result is not None:
        assert de_queue.peek_front() == expected_result
    else:
        with pytest.raises(AssertionError):
            de_queue.peek_front()

#Временная сложность O(1) так как посмотреть первый элемент это крайне быстро