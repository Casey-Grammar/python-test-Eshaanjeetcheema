#Task 6b New Words
'''
Task 6b New Words - Part2 (4marks)

Add to the code from part 1 to create another new word. 
The new word should replace 'o' in the word with a 'y'. 
Use a for loop to print out each letter of this new word on a new line. 
Then print this new word on 1 line at the end.

For example:
=========================
Say: typo
New word!
t
y
p
y
y
y
y
y
y
typyyyyyy!
========================= 

'''
def main():
    x="Task6b"
    #===============================
    # Write your code here
    def main():
    # Read the input message
     message = input("Say: ")
    
    # Part 1: Repeat the last letter 5 times and add exclamation mark
    last_letter = message[-1] # type: ignore
    new_message = message + last_letter * 5 + "!" # type: ignore
    print(new_message)
    
    # Part 2: Create another new word by replacing 'o' with 'y'
    replaced_word = message.replace('o', 'y') # type: ignore
    
    # Repeat the last letter of replaced_word 5 times and add exclamation mark
    last_letter_replaced = replaced_word[-1]
    replaced_word_with_repeats = replaced_word + last_letter_replaced * 5 + "!"
    
    # Print "New word!"
    print("New word!")
    
    # Print each letter of replaced_word_with_repeats on its own line
    for letter in replaced_word_with_repeats[:-1]:  # all except the exclamation mark
        print(letter)
    
    # Print the full replaced_word_with_repeats with exclamation mark
    print(replaced_word_with_repeats)

if __name__ == '__main__':
    main()


    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
