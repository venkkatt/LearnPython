import random


def guesstheno():
    print(__name__)

# When we want to run the code directly then we have use like below
    if __name__ == '__main__':
        print("You are running this directly")
    random_no = random.randint(1, 20)
    print(random_no)
    guess_no = 0
    attempt = 1

    print("Attempts allowed - 5")

    while guess_no != random_no:
        if attempt > 5:
            print("You Loose")
            break
        print("Attempt no - " + str(attempt))
        guess_no = int(input("Guess the no"))
        if guess_no == random_no:
            print("You Won")
            break
        elif guess_no > random_no:
            print("More than guessing no")
        else:
            print("Less than Guessing no")
        attempt += 1
