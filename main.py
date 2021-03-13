password = "password"  #Stored password
tries = 0 #initial value of tries
keepgoing = True

while keepgoing: #while loop
    tries = tries +1 #Number of tries counting up to 3

    guess = input("Password: ")
    if guess == password: #If the password is correct, stop the while loop and print correct
        keepgoing = False
        print("That's correct!")

    if guess != password: #If the password isn't correct, keep going and print Wrong
        print('Wrong')
        keepgoing = True

    if tries >= 3: #If 3 tries are reached, stop the while loop and print Too many wrong tries
        keepgoing = False
        if guess != password:
            print("Too many wrong tries!")