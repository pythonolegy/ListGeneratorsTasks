import decimal


def generator_to_list(f):  # Decorator's function
    def wrapper():
        start = 2
        stop = 5.5
        step = 0.5
        return list(f(start, stop, step))

    return wrapper()


@generator_to_list  # decorator
def decimal_generator(start, stop, step):
    while start <= stop:
        yield float(start)
        start += decimal.Decimal(step)


print(decimal_generator)

# --------------------------------------------------------------------------------------------------#

start = 2
stop = 5.5  # without decorator
step = 0.5


def decimal_generator(start, stop, step):
    while start <= stop:
        yield float(start)
        start += decimal.Decimal(step)


print(list(decimal_generator(start, stop, step)))  # without decorator
