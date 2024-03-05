#Yevhenii Stavytskiy Practice5
word = input("Please write your palindrome word: ")
print()
if(word == word[::-1]):
    print("Yes, your word is palindrome!")
else:
    print("No, your word is not palindrome!")
