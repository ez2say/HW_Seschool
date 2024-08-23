import pytest
from Modul5.Structuri_dannih.Stack.src import Stack


@pytest.fixture
def stack():
    return Stack()

@pytest.mark.parametrize("test_input, expected", [
    ([1, 2, 3], [3, 2, 1]),
    ([], []),
    (["a"], ["a"]),
])
def test_push(stack, test_input, expected):
    for item in test_input:
        stack.push(item)

    result = []
    while not stack.is_empty():
        result.append(stack.pop())

    assert result == expected

#Временная сложность O(1) так как мы просто добавляем элемент в начало стека