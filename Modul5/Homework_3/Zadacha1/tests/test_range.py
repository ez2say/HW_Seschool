import pytest
from Modul5.Homework_3.Zadacha1.src.main_1 import max_in_range

range = max_in_range

@pytest.mark.parametrize('value1, value2, value3, extend_result',
                         [
                             ([1,2,3,4], 1, 3,)
                         ])
# Начал но не закончил тесты
