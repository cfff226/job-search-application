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
    new_name = name.replace(" ", "")
    if new_name.isalpha():
        print(f"Your name is {name}")
        break
    else:
        continue

while True:
    # Request input for users age
    try:
        age = int(input("Please input your age: "))
        if age < 16:
            raise Exception("The minimum age requirement is 16")
            break
        elif 16 <= age < 100:
            print(f"Your age is {age}")
            break
    except ValueError:
        print("Your input isn't valid")
        continue

    # Request input for users current location

    # Request input for users email address

    # Request input for users contact number

    # Request input for users skills

    # Request input for users preferred job type
