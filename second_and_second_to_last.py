# word = input("Please type in a string:")
# length = len(word)
# i = 0
# same = False
# while i < length:
#     if word[1] == word[length - 2]:
#         same = True
#     i += 1
    
# if same:
#     print("The second and the second to last characters are",word[1])
# else:
#     print("The second and the second to last characters are different")
    


# Or



word = input("Please type in a strring:")

if len(word) > 1 and word[1] == word[-2]:
    print("The second and the second to last characters are", word[1])
else:
    print("The second and the second to last characters are different")
