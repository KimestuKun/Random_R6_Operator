# We import random to allow randomization of a given range of 0-40 (because arrays start at 0)
import random
import operators

#*This program focuses on: 
# - Importing modules
# - Loops
# - Input Validation
# - Lists and indexing
# - Randomization
# - Printing and Formatting
# - Event Driven logic
# - Defensive programming
#*#

#initialize choice to activate our while loop
choice = 0
#while choice is not 3 run loop
while choice != 3:
    
    # Print title
    print("\n" + "="*40)
    print("      🎮 R6 Random Operator Generator 🎮      ")
    print("="*40 + "\n")

    while True:
        # Menu Choice
        try:
            choice = int(input("Choose an option:\n"
                        "  1. Attacking\n"
                        "  2. Defending\n"
                        "  3. Quit\n"
                        "Enter choice: "))
            #If choice is an integer then break try loop
            if choice > 0 and choice <= 3:
                break
            else:
                print('There is only 3 options.....🤦‍♂️ 🤦‍♀️Try again..')

        # Else print skill issue            
        except ValueError:
            print('Invalid input. Please enter an Integer provided on the menu.')
            print('R6 plAyeRS hAvE tHE AverAGe iQ oF 🤓☝️')
    
    if choice == 1:
        # Random.randint(start, stop + 1) is how its structured
        # random range is 0 to the length of operators.py within array operatorA
        def attackerChoice():
            num = random.randint(0 , len(operators.operatorA))
            print("\n" + "-"*45)
            print(f"🔫 Attack Operator Picked: {operators.operatorA[num]}")
            print(f"🎲 Random Index: {num}")
            print("-"*45 + "\n")

            # Prints operator and number
            print(operators.operatorA[num])
    
    elif choice == 2:
        # Random.randint(start, stop + 1) is how its structured
        # random range is 0 to the length of operators.py within array operatorD
        def defenderChoice():
            num = random.randint(0 , len(operators.operatorD))
            print("\n" + "-"*40)
            print(f"🛡️ Defend Operator Picked: {operators.operatorD[num]}")
            print(f"🎲 Random Index: {num}")
            print("-"*40 + "\n")
        
            # Prints operator and number
            print(operators.operatorD[num])
    
    elif choice == 3:
        #break out of loop
        print("\nExiting... Thanks for using the R6 Operator Generator! 🎮\n")
        break
