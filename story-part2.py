# Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.
# Change the program so that the loop ends also if the user types in the same word twice in a row.

words = ""
prev_word = ""
while True:
    word = input("Please type in a word:")
    if word != "end" and word != prev_word:
        prev_word = word
        words += word + " "

    else:
        break

print(words)