
numbers = []
with open('input.txt', 'r') as file:
    for line in file:
        numbers.append(int(line))

for number in numbers:
    for number2 in numbers:
        if (number + number2) == 2020:
            print(f"number1: {number}\nnumber2: {number2}")
            print(number * number2)

for number in numbers:
    for number2 in numbers:
        for number3 in numbers:
            if (number + number2 + number3) == 2020:
                print(number * number2 * number3)
