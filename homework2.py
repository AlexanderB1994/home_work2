tries = 0
while True:
    try:
        age = int(input("Age:"))
    except ValueError:
        tries += 1
        if tries == 3:
            print("Account locked for 3 wrong attempts")
            break
        print("Invalid number. Try again")
        continue

    if age >= 18:
        print("Log in successful")
    else:
        print("You are not 18 years old, restricted access!")
    break
