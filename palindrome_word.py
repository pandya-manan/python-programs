word=input("Enter a word: ")
length=len(word)
reverse=""
for i in range(length-1,-1,-1):
    reverse=reverse+word[i]

if(reverse==word):
    print("{} is a palindrome word".format(word))
else:
    print("{} is not a palindrome word".format(word))
    


