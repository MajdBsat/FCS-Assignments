numbers = [-12, 4, 12, 25, 67]

num = 0

while num != -99:
    num = int(input("Enter a number: "))

    if num == -99:
        numbers.append(-99)
        numbers.sort()
        print(numbers)
        break

    else:
        numbers.append(num)
        numbers.sort()
        print(numbers)  