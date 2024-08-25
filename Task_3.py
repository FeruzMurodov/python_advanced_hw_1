count_of_numbers = int(input('Enter the count of numbers you are going to insert: '))
result = count_of_numbers
for _ in range(count_of_numbers):
    number = int(input('Enter number: '))
    dividers = 0
    for divider in range(2, number):
        if number % divider == 0 :
            result -= 1
            break
print('The count of the prime numbers is', result)