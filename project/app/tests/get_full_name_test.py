from utils.get_full_name import get_full_name

def test_get_full_name_1():
    first_name = 'Степан  '
    last_name = 'Лящук  '
    expect = 'Степан Лящук'
    actual = get_full_name(first_name, last_name)
    assert expect == actual

def test_get_full_name_2():
    first_name = 'Ян  '
    last_name = '  '
    expect = 'Ян '
    actual = get_full_name(first_name, last_name)
    assert expect == actual

def test_get_full_name_3():
    first_name = 'Афанасій  '
    last_name = '  '
    expect = 'Афанасій '
    actual = get_full_name(first_name, last_name)
    assert expect == actual

def test_get_full_name_4():
    first_name = 'А  '
    last_name = 'П  '
    expect = 'А П'
    actual = get_full_name(first_name, last_name)
    assert expect == actual


def test_get_full_name_5():
    first_name = 'Афанасій  '
    last_name = 'Петров  '
    expect = 'Афанасій Петров'
    actual = get_full_name(first_name, last_name)
    assert expect == actual
