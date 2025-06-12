#!/usr/bin/env python3
"""
Contains a simple implementation of the Foward chaining algorithm
"""

database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
knowbase = ["Frog", "Canary", "Green", "Yellow"]

def display_facts():
    """
    displays available facts for selection
    """
    print("\n X is: \n1.Croaks \n2. Eat Flies \n3. Shrimps \n4. Sings")
    print("Select an option:", end='')

def main():
    """
    Main function that implements the foward chaining
    """
    print("*-------------Foward Chaining--------*", end='')
    display_facts()
    try:
        x = int(input())
    except ValueError:
        print("\n --invalid input please select a valid option between 1 and 4.")
        return

    if x == 1 or x == 2:
        print("Chance of Frog", end='')
    elif x == 3 or x == 4:
        print("Chance of Canary", end='')
    else:
        print("\n---Invalid Option! Please select a valid option between 1 and 4.")
        return

    if 1 <= x <= 4:
        print("\n x is:", database[x-1])
        print("\nColor is: 1. Green  2. Yellow", end='')
        print("\nSelect color option:", end='')
    
        try:
            k = int(input())
        except ValueError:
            print("\n---Invalid input! Please select either option 1 or 2 for color.")
            return

        if k == 1 and (x == 1 or x == 2):
            print("Yes, it is", knowbase[0], "And Color is", knowbase[2])
        elif k == 2 and (x == 3 or x == 4):
            print("Yes, it is", knowbase[1], "And Color is", knowbase[3])
        else:
            print("\n---Invalid Knowledge Database! Please select valid options.")

if __name__ == "__main__":
	main()

