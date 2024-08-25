DOT = '.'
count = int(input('Enter count: '))
for line in range(count):
    for left_number in range(count, count - line - 1, -1):
        print(left_number, end="")
    dot_count = 2 * (count - line - 1)
    print(DOT * dot_count, end="")
    for right_number in range(count - line, count + 1):
        print(right_number, end="")
    print()
