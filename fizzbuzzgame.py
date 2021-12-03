count = 0
score = 0
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
 
while count < 99:
    fizzbuzz()
print("Score: " + str(fizzbuzz()) + "/100")