import pytest
from Algoritms.Primer_1.src.main_1 import summa_of_elem

sum = summa_of_elem

@pytest.mark.parametrize('value, extend_result',
                         [
                             ([2,4,6,8,10], 30),
                             ([2,4,6,8,10], 30),
                             ([-1, -2, -3, -4], 1)
                         ])
def test_sum(value,extend_result):
    assert sum(value) == extend_result


@pytest.mark.parametrize('value, extend_result',
                         [
                             ([2,4,6,8,"Десять"], pytest.raises(ValueError)),
                             ([2,4,6,8,10.0,"Десять"], pytest.raises(ValueError)),
                             ([-1, -2, -3, -4], 1)
                         ])
def test_wrong_value(value,extend_result):
    with extend_result:
        assert sum(value) == extend_result