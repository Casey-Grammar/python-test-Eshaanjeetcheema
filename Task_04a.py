#Task 4a King Letter
'''
Task 4a King Letter (4marks)

In Commonwealth countries, like Australia and New Zealand, the King send 
you an anniversary letter when you turn 100.

Write a program that ask the user for their age, then prints how many 
years until they get their letter (by taking it from 100).

Here's how it should work:
=========================
How old are you? 15
Years until your letter...
85
========================= 

Here's another example:
=========================
How old are you? 90
Years until your letter...
10
=========================
Your program should still subtract from 100, even if you're older than that:
=========================
How old are you? 111
Years until your letter...
-11
=========================

'''
from matplotlib.dviread import Page


def main():
    x="Task4a"
    #===============================
    # Write your code here
    def main():
    # Ask the user for their age
     age = int(input("How old are you? "))
    
    # Calculate years until the letter (100 - age)
    years_until_letter = 100 - Page
    
    # Print the result
    print("Years until your letter...")
    print(years_until_letter)

if __name__ == '__main__':
    main()

    

    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
