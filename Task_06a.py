#Task 6a New Words
'''
Task 6a New Words (4marks)

Write a program to read in a message and give it more emphasis!

Repeat the last letter of the word 5 times, and end with an exclamation 
mark.

You want to ADD THE REPEATS TO THE ORIGINAL WORD, so the last letter will 
appear 6 times in total. Like this, which is typo plus ooooo:

=========================
Say: Oh no, typo
Oh no, typoooooo!
========================= 

Here's another example:
=========================
Say: lol
lollllll!
=========================

If the word ends in a double letter, don't do anything special; you'll 
just end up with 7 of the last letters. For example:
=========================
Say: Yass
Yasssssss!
=========================

'''
def main():
    x="Task6a"
    #===============================
    # Write your code here
    def main():
    # Read the input message
     message = input("Say: ")
    
    # Find the last letter of the word
    last_letter = message[-1] # type: ignore
    
    # Add 5 more repeats of the last letter to the original word
    # So total last letters = original 1 + 5 repeats = 6 in total
    new_message = message + last_letter * 5 + "!" # type: ignore
    
    # Print the emphasized message
    print(new_message)

if __name__ == '__main__':
    main()


    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
