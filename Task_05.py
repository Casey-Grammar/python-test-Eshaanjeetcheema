#Task 5 Counting Sheep
'''
Task 5 Counting Sheep (4marks)

It's late and you should sleep, but you're not tired!

You've heard counting sheep can help, but you get distracted while 
counting, so you decide to write a program to help.

Your program should work like this:

=========================
How many sheep: 4
1 sheep
2 sheep
3 sheep
4 sheep
========================= 

Here's another example:
=========================
How many sheep: 9
1 sheep
2 sheep
3 sheep
4 sheep
5 sheep
6 sheep
7 sheep
8 sheep
9 sheep
=========================

'''
def main():
    x="Task5"
    #===============================
    # Write your code here
    def main():
    # Ask the user how many sheep to count
     number_of_sheep = int(input("How many sheep: "))
    
    # Count from 1 up to number_of_sheep, printing each number with "sheep"
    for i in range(1, number_of_sheep + 1): # type: ignore
        print(f"{i} sheep")

if __name__ == '__main__':
    main()

    

    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
