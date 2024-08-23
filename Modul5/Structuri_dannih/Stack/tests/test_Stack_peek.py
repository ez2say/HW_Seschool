import pytest
from Modul5.Structuri_dannih.Stack.src import Stack


@pytest.fixture
def stack():
    return Stack()


@pytest.mark.parametrize("test_input, expected", [
    ([1, 2, 3], 3),
    ([], None),
    (["a"], "a"),
])
def test_peek(stack, test_input, expected):
    for item in test_input:
        stack.push(item)
    if expected is None:
        with pytest.raises(Exception):
            stack.peek()
    else:
        assert stack.peek() == expected


#Временная сложность O(1) так как мы просто возвращаем данные с вершины стека без его удаления.