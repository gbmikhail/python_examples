def iterator_counter():
    counter = 0

    def wrapper():
        nonlocal counter
        counter += 1
        return counter
    return wrapper


def main():
    counter = iterator_counter()
    for _ in range(10):
        print(counter())


if __name__ == '__main__':
    main()
