@lambda f: lambda *args: print(f(*args))
def f():
    return "hello"

f()


b = lambda func: lambda *args, **kwargs: (print("a"), func(*args, **kwargs), print("c"))

@b
def a():
    print("b")

a()