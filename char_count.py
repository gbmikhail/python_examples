def get_char_count(line: str):
    counter = {}
    for i in line:
        counter[i] = counter.get(i, 0) + 1
    return counter


def main():
    s = 'hello world'
    chars = get_char_count(s)
    print(chars)

    # v2
    m = map(lambda x: (x, s.count(x)), set(s))
    print({x[0]: x[1] for x in m})

    # v3
    d = {x: s.count(x) for x in set(s)}
    print(d)


if __name__ == '__main__':
    main()
