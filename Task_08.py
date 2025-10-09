#Task 8 Band Welcome !
'''
Task 8 Band Welcome ! (7 marks)

Your band has its very first gig! What songs are you going to play?

Write a program that asks for your band name, and then for a 
list of space-separated song titles.

Note: Your band only sings songs with one=word titles!

The output should look like this:
=========================
Band: The One Word Wonders
Songs: Song Lyric Ballad
Please welcome to the stage, The One Word Wonders!
They will be playing...
! Song
! Lyric
! Ballad
Give it up for The One Word Wonders!
========================= 

Here's another example:
=========================
Band: Lady Gaga
Songs: Paparazzi Applause Shallow
Please welcome to the stage, Lady Gaga!
They will be playing...
! Paparazzi
! Applause
! Shallow
Give it up for Lady Gaga!
=========================

HINT: Use "!" as the symbol in front of the songs!

'''

from pkg_resources import safe_name


def main():
    x="Task8"
    #===============================
    # Write your code here
    def main():
    # Ask for the band name
     band_name = input("Band: ")
    
    # Ask for the space-separated song titles
    songs = input("Songs: ").split()
    
    # Print welcome message
    print(f"Please welcome to the stage, {band_name}!") # type: ignore
    print("They will be playing...")
    
    # Print each song with ! in front
    for song in songs:
        print(f"! {song}")
    
    # Final cheer for the band
    print(f"Give it up for {band_name}!") # type: ignore
    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
