def get_square(val):
    """The callback"""
    return val ** 2

def caller(func, val):
    return func(val)

assert caller(get_square, 5) == 25
