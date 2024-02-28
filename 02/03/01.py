def decorator(func):
    def wrapper(a, b):
        if a < 0 or b < 0:
            print('YES')
        return func(a, b)
    return wrapper


# Your decorator code

# Connect decorator please
@decorator
def main(a, b):
    return a + b


x, y = [int(x) for x in input().split()]
print(main(x, y))
