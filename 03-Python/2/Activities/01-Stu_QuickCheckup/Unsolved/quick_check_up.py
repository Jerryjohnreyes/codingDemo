# Print Hello User!
print('Hello User!')
repeat = "y"
# Take in User Input
while repeat == "y":
    user_name = input('What is your name? ')

    # Respond Back with User Input
    print(f"Hello {user_name}")

    # Take in the User Age
    user_age = int(input(f'{user_name}, how old are you? '))

    # Respond Back with a statement based on age
    if user_age < 22:
        print("Awww... you're just a baby!")
    else:
        print("Ah... A well traveled soul are ye.")
    repeat = input("Do you want me to repeat the message? Type 'y' if yes ")
