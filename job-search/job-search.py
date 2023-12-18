# A program which validates the input that a user provides for an application according to the applications criteria

# Required input:
# Name
# Age
# Location
# Email address
# Contact number
# Skills
# Preferred Job Type


tech_skills = [
    "Python",
    "HTML",
    "CSS",
    "Javascript",
    "React",
    "Angular",
    "Vue.js",
    "Node.js",
    "Ruby",
    "Lavarel",
    "Django",
    "Springboot" "SQL (Structured Query Language",
    "MySQL",
    "MongoDB",
    "Version Control",
    "Microsoft Azure",
    "Cloud Computing" "Server Management",
    "Docker",
    "Kubernetes",
    "Flask",
    "GraphQL",
    "Jest",
    "Mocha",
    "Jasmine",
    "pytest",
    "OAuth" "JSON",
    "Github",
    "Gitpod",
]

users_skills_list = []

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
        if age < 18:
            raise Exception("The minimum age requirement is 16")
            break
        elif 18 <= age < 160:
            print(f"Your age is {age}")
            break
    except ValueError:
        print("Your input isn't valid")
        continue

    # Request input for users current location

while True:
    location = input("Please input your location: ")
    new_location = location.replace(" ", "")
    if not new_location.isalpha():
        print("Your input isn't valid")
        continue
    else:
        print(f"You have chosen {location} as your location")
        break


while True:
    # Request input for users email address
    user_email = input("Please input your email address: ")
    if "@" in user_email and "." in user_email:
        print(f"Your email address is {user_email}")
        break
    else:
        continue

while True:
    # Request input for confirmation of users email address
    user_email_confirmation = input("Please confirm your email address: ")
    if user_email != user_email_confirmation:
        print("The email address's that you have entered do not match")
        continue
    else:
        break

    # Extend email input to check if email already exists

while True:
    # Request input for users contact number
    user_phone_number = str(input("Please input your contact number: +"))
    new_user_phone_number = user_phone_number.replace(" ", "")
    if new_user_phone_number.isdigit():
        if len(new_user_phone_number) < 13:
            break
        else:
            print("Please enter a valid contact number")
            continue

skills_listed = False

while skills_listed is False:
    # Output a menu of list of skills to choose from and the user can add these to a list

    for i in range(len(tech_skills)):
        print(str(i + 1) + ". " + tech_skills[i])
        idx = tech_skills.index(tech_skills[i])
        skills_listed = True

    while True:
        # Request input for users skills
        input_skills = int(input("Please type in the number of each of your skills: "))
        input_skills2 = input_skills - 1
        length = len(tech_skills) + 1

        if input_skills2 in range(1, length):
            result = tech_skills[input_skills2]

            if result not in users_skills_list:
                users_skills_list.append(result)
                print(users_skills_list)
                continue
