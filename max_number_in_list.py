numbers=[]
for i in range(0,5):
    print("Enter the number to be added to the list: ")
    numbers.append(int(input("Enter the number ")))

max=numbers[0]
for i in range(0,5):
    if(numbers[i]>max):
        max=numbers[i]

print("The maximum in the list is: {}".format(max))