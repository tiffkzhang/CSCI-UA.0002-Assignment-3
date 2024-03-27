sticks = int(input('How many sticks to start with (10-100)? '))

while True:
    if sticks < 10:
        print("Sorry, that's too few sticks. Try again.\n")   
        sticks = int(input('How many sticks to start with (10-100)? '))
    elif sticks > 100:
        print("Sorry, that's too many sticks. Try again.\n")
        sticks = int(input('How many sticks to start with (10-100)? '))
    else:
        print("Great, let's play...\n")
        break

num_stick = 0
player = 1

while sticks > 0:
    print('Turn: Player', player)

    if sticks == 1:
        print('There is', sticks, 'stick on the table.')
    else:
        print('There are', sticks, 'sticks on the table.')
    
    num_stick = int(input('How many sticks do you want to take (1, 2 or 3)? '))

    if num_stick != 1 and num_stick != 2 and num_stick != 3:
        print("Sorry, that's not a valid number.\n")
    else:
        print()
        sticks = sticks - num_stick 
        if player == 1:
            player = 2
        else:
            player = 1

print('There are no sticks left on the table. Game over.')
print('Player', player, 'wins!')


         

