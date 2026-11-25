from decorators.pack_result import add_numbers, greet, is_even
from main import result


def test_add_number():
    assert add_numbers(2, 5, 11) == {'result': 18, 'status': 'success'}

def test_greet():
    assert greet('Максим') == {'result' : 'Привіт!', 'status': 'success'}

def test_is_even():
    assert is_even(11) == {'result': False, 'status': 'success'}
    assert is_even(4) == {'result': True, 'status': 'success'}