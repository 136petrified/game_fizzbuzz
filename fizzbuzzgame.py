# Global variables 
count = 0
score = 0

# Define fizzbuzz
def fizzbuzz():
    global count
    global score
    answer = input("Enter number: ")
    count = count + 1
    print(count)
    for i in range(1,101):
        if count % 5 == 0 and count % 3 == 0:
            if answer == "fizzbuzz":
                score = score + 1
                print("Correct!")
                return score
            else:
                print("Incorrect!")
                return score
        elif count % 3 == 0:
            if answer == "fizz":
                score = score + 1
                print("Correct!")
                return score
            else:
                print("Incorrect!")
                return score
        elif count % 5 == 0:
            if answer == "buzz":
                score = score + 1
                print("Correct!")
                return score
            else:
                print("Incorrect!")
                return score
        elif count % 3 != 0 or count % 5 != 0:
            if answer == str(count):
                score = score + 1
                print("Correct!")
                return score
            else:
                print("Incorrect!")
                return score
        else:
            return score
 
# Introduction
print("Welcome to the fizzbuzz game!")
print("To begin, type the first number, which is the number 1,")
print("and keep counting until you get to 100!")
print("If you want to know how to play the game, see the README in the repository!")

# Run fizzbuzz game (repeat until 100th number)
while count < 99:
    fizzbuzz()

# Conclusion
print("Score: " + str(fizzbuzz()) + "/100")

# Note: There is no restart function. It will be added later.
