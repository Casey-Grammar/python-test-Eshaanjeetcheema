#Task 9b Snail Cup
'''
Task 9b Snail Cup (4 marks)

Modify the code from Part a to print out the snails in alphabetical order on separate lines. 

It should ask for the name of a racer who's gone to sleep and REMOVE their name in the list. If 
that name isn't in the list, it should leave the list unmodified and print a message 
saying all the racers are still awake.

Here's an example of how your program should look:
=========================
And the line up is: Dash, Speedy, Lighting, Flash, Sonic
Who's gone to sleep? Dash
Remaining racers:
Flash
Lighting
Sonic
Speedy
========================= 

'''



def main():
    x="Task9b"
    #===============================
    # Write your code here
    racers = ["Dash", "Speedy", "Lighting", "Flash", "Sonic"]
    
     # Print the initial lineup
    print("And the line up is: " + ", ".join(racers))
     
     # Ask for the name of the snail who went to sleep
    sleepy_snail = input("Who's gone to sleep? ")
    
     # Check if the snail is in the list
    if sleepy_snail in racers:
        # Replace their name with 'Disqualified'
        index = racers.index(sleepy_snail)
        racers[index] = "Disqualified"
        print(f"{sleepy_snail} has been disqualified!")
    else:
        print("All snails still awake.")
    
     # Print the remaining racers
     #  print("Remaining racers: " + ", ".join(racers))
    

    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
