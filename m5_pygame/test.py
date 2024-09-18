def do_something(a, b):
    info = input('Умножить или сложить числа? 1/2')
    if info == '1':
        return a * b
    return a + b


result = do_something(5, 2)
print(result)
