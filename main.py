def sortMax(listNumber: list):
    listNumber.sort(reverse=True)
    return int(''.join(listNumber))

def sortMin(listNumber: list):
    listNumber.sort()
    return int(''.join(listNumber))

def calcul(listNumber: list):
    result = sortMax(listNumber) - sortMin(listNumber)
    essay = 1
    while result != 6174:
        essay += 1
        listNumber.clear()
        for i in str(result):
            listNumber.append(i)
        result = sortMax(listNumber) - sortMin(listNumber)
    return essay

try:
    userInput = int(input("Enter 4 numbers: "))
    while len(str(userInput)) != 4:
        userInput = int(input("Enter 4 numbers: "))
    numbers = []

    for i in str(userInput):
        numbers.append(i)
    result = calcul(numbers)
    print(f"The kaprekar's constant will be displayed after {result} essay")
except Exception as e:
    print(e)