from ordinal import fgr


def factorial(num):
    """Factorial of a number"""
    print(f"{num} * ", end="")
    if num == 1:
        return 1
    return num * factorial(num - 1)


def print_no_loop(text: str, times: int):
    """Print text multiple times without a loop"""
    count = 1

    def p():
        nonlocal count
        nonlocal text
        if count > times:
            return None
        print(f"{fgr(count)} => ", text)
        count += 1
        p()
    p()


def add_no_loop(num: int, times: int = 10):
    """Add num multiple times without a loop"""
    count = 1

    def add():
        nonlocal count
        nonlocal num
        if count > times:
            return 0
        print(f"{num} + ", end="")
        count += 1
        return num + add()
    print(add())


print("\n=>", factorial(5))

print_no_loop('Hello', 5)

add_no_loop(5)
