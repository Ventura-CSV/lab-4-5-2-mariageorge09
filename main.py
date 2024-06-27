import random
def main():
    id = 0
    total = 0
    numbers = []
    while ( total < 100):
        num = random.randint(0,100)
        numbers.append(num)
        total += numbers[id]
        id = id + 1
    print('Output ')
    print(numbers)
    print(f'The total sum is {total-num}')
    


    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
