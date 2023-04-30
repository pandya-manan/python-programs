numbers=[]
size=int(input("Enter the size of the list: "))
for i in range(0,size):
    numbers.append(int(input("Enter the number: ")))

print("The numbers in the reverse order")
for i in range(size-1,-1,-1):
    print(numbers[i])
    

