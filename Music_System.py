from Main import Music_Theory
import os
def Music_System(user_input, helper):
    if user_input == 1 :
        helper.Print_Scale()
    elif user_input == 2 :
        helper.Print_Major_Scales()
    elif user_input == 3 :
        helper.Print_Minor_Scales()
    elif user_input == 4 :
        helper.Print_Chord_Family()
    elif user_input == 5 :
        helper.Print_Chord()
    else:
        print("Enter valid input...!!!")

def Start_Music_System():
    os.system("cls")
    helper = Music_Theory("By Daniel")
    print(
        """
        1. Enter 1 to print a scale.
        2. Enter 2 to print all the major scales.
        3. Enter 3 to print all the minor scales.
        4. Enter 4 to print chord family.
        5. Enter 5 to print the chord.
        """
        )
    user_input = int(input("Enter your choice :"))
    Music_System(user_input, helper)

# Start the Music system..............!!!!!!!!!!!!!
Start_Music_System()
    

