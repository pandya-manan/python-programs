numbers=[]
size=int(input("Enter the size of the list: "))
for i in range(0,size):
    numbers.append(int(input("Enter a number: ")))

numbersDict={num:"Integer" for num in numbers}

print(numbersDict)
print(numbersDict.get(1))