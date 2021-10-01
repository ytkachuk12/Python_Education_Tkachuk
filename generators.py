import types


# fill in this function
def fib():
    fib1 = 1
    fib2 = 1

    for i in range(10):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib2


# testing code
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
