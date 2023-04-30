numbers=[]
size=int(input("Enter the size of the list of numbers: "))
sum=0
for i in range(0,size):
    numbers.append(int(input("Enter a number: ")))
    sum+=numbers[i]

print("The sum of the elements in the list is {}".format(sum))