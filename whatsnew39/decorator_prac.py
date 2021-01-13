def make_decorators():
    def decorator0(func):
        def inner_func0(*args):
            print('decorator 0')
            return func(*args)
        return inner_func0

    def decorator1(func):
        def inner_func1(*args):
            print('decorator 1')
            return func(*args)
        return inner_func1
    return [decorator0, decorator1]


decorators = make_decorators()


@decorators[0]
def hello():
    print('hello')


@decorators[1]
def goodbye():
    print('goodbye')


hello()
goodbye()
