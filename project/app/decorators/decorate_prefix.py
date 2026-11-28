def add_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f'{prefix} {func(*args, **kwargs)}'
        return wrapper
    return decorator

@add_prefix('[INFO]')
def get_message():
    return 'Application started'

print(get_message())
