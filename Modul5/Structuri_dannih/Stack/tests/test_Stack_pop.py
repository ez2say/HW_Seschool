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
def test_pop(stack, test_input, expected):
    for item in test_input:
        stack.push(item)
    if expected is None:
        with pytest.raises(Exception):
            stack.pop()
    else:
        assert stack.pop() == expected

#Временная сложность O(1) так как мы просто удаляем элемент с вершины стека