# A program which validates the input that a user provides for an application according to the applications criteria

# Required input:
# Name
# Age
# Location
# Email address
# Contact number
# Skills
# Preferred Job Type

form_complete = False

# while loop to show the form until the form has been completed

while not form_complete:
    name = input("Please input your name: ")
    if name.isalpha():
        print(f"Your name is {name}")
        break
    else:
        continue

    # Request input for users age
    try:
        age = int(input("Please input your age"))
    except ValueError:
        print("Your input isn't valid")

    # Request input for users current location

    # Request input for users email address

    # Request input for users contact number

    # Request input for users skills

    # Request input for users preferred job type

