import pytest
from Algoritms.Primer_2.src.main_2 import povtoryashka

povt = povtoryashka

@pytest.mark.parametrize('value, extend_result',
                         [

                         ])
def test_function_positive(value,extend_result):
    global povt
    assert povt(value) == extend_result


@pytest.mark.parametrize('value, extend_result',
                         [

                         ])
def test_wrong_value(value,extend_result):
    global povt
    with extend_result:
        assert povt(value) == extend_result