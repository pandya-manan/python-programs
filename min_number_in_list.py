numbers=[]
size=int(input("Enter the length of the list: "))

for i in range(0,size):
    numbers.append(int(input("Enter the number to be added to the list: ")))

min=numbers[0]
for i in range(0,size):
    if(numbers[i]<min):
        min=numbers[i]

print("The smallest element in the list is {}".format(min))

