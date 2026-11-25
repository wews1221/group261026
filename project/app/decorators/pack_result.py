def pack_result(function):
    def wrapper(*args):
        result = function(*args)
        return {'result': result, 'status': 'success'}
    return wrapper

@pack_result
def add_numbers(*args):
    return sum(args)

@pack_result
def greet(*names):
    if not names:
        return 'Привіт!'
    return f'Привіт!'

@pack_result
def is_even(number):
    return number % 2 ==0

print(add_numbers(2, 5, 11))
print(greet('Максим'))
print(is_even(11))
