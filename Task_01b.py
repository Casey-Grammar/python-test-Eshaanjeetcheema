
#Task 1b More Echos
'''
Task 1 More Echo (2marks)
Part b

Add to the code from part 1 to print out the echo on a separate line. Your program should work like this:
=========================
Shout: hello
hello hello hello

hello
hello
hello
=========================  
'''
def main():
    x="Task1b"
    #===============================
    # Write your code here
    # Ask user to shout something
    shout = input("Shout: ")
    
    # Print echo on the same line, repeated 3 times
    print(shout, shout, shout)
    
    # Print echo on separate lines, repeated 3 times
    print(shout)
    print(shout)
    print(shout)
        # End of your code here
    # #===============================

if __name__ == '__main__':
    main()
