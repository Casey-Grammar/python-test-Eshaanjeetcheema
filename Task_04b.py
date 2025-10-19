#Task 4b King Letter
'''
Task 4b King Letter (2marks)

Add to the code from part 1 to change the output when a number is 
greater than 100 to show for example:

=========================
How old are you? 111
You already got your letter 11 years ago
========================= 

'''
#from matplotlib.dviread import Page


def main():
    x="Task4b"
    #===============================
    # Write your code here
    def main():
    # Ask the user for their age
     age = int(input("How old are you? "))
    
    # Check if age is over 100
    if Page > 100:
        years_since_letter = Page - 100
        print(f"You already got your letter {years_since_letter} years ago")
    else:
        years_until_letter = 100 - Page
        print("Years until your letter...")
        print(years_until_letter)

#if __name__ == '__main__':
#    main()


    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
