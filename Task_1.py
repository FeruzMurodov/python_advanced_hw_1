PIPE = '|'
DEFIS = '-'
SPACE = ' '

width = int(input('Enter the width of the frame: '))
height = int(input('Enter the height of the frame: '))
print(f'{PIPE}{DEFIS * width}{PIPE}')
for _ in range(height - 2):
    print(f'{PIPE}{SPACE * width}{PIPE}')
print(f'{PIPE}{DEFIS * width}{PIPE}')
