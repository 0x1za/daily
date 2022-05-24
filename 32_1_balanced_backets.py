OPENING = '('

def is_balanced(s: str) -> bool:
    stack = []

    for item in s:
        if item == OPENING:
            stack.append(OPENING)
        else:
            try:
                stack.pop()
            except IndexError:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    print(is_balanced('((()))'))  # => True
    print(is_balanced('(()'))  # => False
    print(is_balanced('())'))  # => False
