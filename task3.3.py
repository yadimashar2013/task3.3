def test(*args):
    print(test)
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('Позиционный параметр:', i, arg)


test(11, 'spiel', [3, 2], )


def factorial(n):
    if n == 3:
        return 3
    test = factorial(n=n - 1)
    return n * test


print(factorial(9))
