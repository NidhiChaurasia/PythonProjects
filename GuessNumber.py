import random
# to create a range of random numbers between 1-20
n = random.randrange(1, 20)
guess_value = int(input("Enter any number : "))
while n != guess_value:
    # if guess is smaller than n
    if guess_value < n:
        # ask user for input
        print("Too much low")
        guess_value = int(input("Enter a number: "))
    #if guess_value is greater than n
    elif guess_value > n:
        print("Too much far")
        # ask user for input
        guess_value = int(input("Enter any other number:"))

    # if guess_value and n value are equal to each other
    else:
        break

print("Hurray !! You guessed the correct value")
