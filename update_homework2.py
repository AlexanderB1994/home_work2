for tries in range(3):
    try:
        age = int(input("Age:"))
    except ValueError:
        if tries == 2:
            print("Account locked for 3 wrong attempts")
            break
        print("Invalid number. Try again")
        continue

    if age >= 18:
        print("Log in successful")
        break
    else:
        print("You are not 18 years old, restricted access!")
