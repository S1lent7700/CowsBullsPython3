import os, sys, random, re
from collections import Counter

class MainLoop:
    # Empty construct
    def __init__(self):
        pass

    # Main loop entry
    def cow_bull_main(self, num):
        cow = 0
        # of digits guessed correctly which will be appended to the "cows".
        bullvar = 0
        x = MainLoop()

        try:
            prompt = str(input("Enter 4-Digit guess: "))
            # Check for duplicate integers here
            while not x.check_duplicate_integers(prompt):
                prompt = str(input("Enter 4-Digit guess: "))

            # Check for values less then 0
            while not x._check_value_lt0(int(prompt)):
                prompt = str(input("Enter 4-Digit guess: "))

            # Check if the digit is ALL numbers
            while not x._check_for_char(prompt):
                prompt = str(input("Enter 4-Digit guess: "))

            # Check if the prompt entry length is greater than or less than 4
            while not x._check_input_length(prompt):
                prompt = str(input("Enter 4-Digit guess: "))

            for i in range(0, 4):
                if num[i] == prompt[i]:
                    cow += 1
            for i in num:
                if i in prompt:
                    bullvar += 1
            bull = (bullvar - cow)
            print("you have {} bull(s) and {} cow(s)".format(cow, bull))
        #except Exception as e:
        #    print("\nInput may be invalid, please use integers instead of strings and characters.\n")

        except KeyboardInterrupt:
            print("\n\nIt looks like you have given up, sad, please try again later\n")
            exit(1) #...

        # Return the cow
        return cow


    def check_duplicate_integers(self, input):
        check = Counter(input)
        if any(value > 1 for value in check.values()):
            print("\nIncorrect value, make sure that the integer is not repeating\n")
            return False
        return True

    def check_duplicate_integers2(self, input):
        check = Counter(input)
        if any(value > 1 for value in check.values()):
            return False
        return True

    def _check_value_lt0(self, input):
        num = int(input)

        if num <= 0:
            print("\nInvalid digit, please ensure that the number is greater than 0.\n")
            return False
        return True

    def _check_for_char(self, input):
        if not str(input).isalpha():
            return True
        print("\nInvalid integer, please enter digits only, no strings or characters.\n")
        return False

    def _check_input_length(self, input):
        if len(input) < 4:
            print("\nThe guess must have an integer value of 4 digits, please try again.\n")
            return False

        if len(input) > 4:
            print("The guess must have an integer value of 4 digits (you entered " + str(len(input)) + "), please try again")
            return False
        return True

def main():
    override = sys.argv[1]
    bulls = 0
    count = 0
    guesses = 1
    num = str(random.randrange(0, 9999))
    test_num = override

    # Init main object loop
    main_loop = MainLoop()

    # While the randomly generated number contains duplicate values, continue
    # to generate a random number until the randomly generated integer value
    # does NOT contain a duplicate integer value.
    while not main_loop.check_duplicate_integers2(num):
        # print("Random Integer contains repeating digits, re-generating random number")
        num = str(random.randrange(0, 9999))

    # Debug purposes...
    # print(num)

    while bulls != 4 and guesses != 10:
        count += 1
        if override == "normal":
            bulls = main_loop.cow_bull_main(num)
            guesses += 1

            if bulls == 4:
                print("\nCorrect! The random number is: " + str(num) + "\n")
                exit(0)

            if guesses == 10:
                print("\nYou have reached the maximum number of tries (10), please try again later.\n")
                exit(0)
        else:
            print("\nOverridden 4-digit value is: " + str(test_num) + "\n")
            bulls = main_loop.cow_bull_main(test_num)
            guesses += 1

            if bulls == 4:
                print("\nCorrect! The random number is: " + str(test_num) + "\n")
                exit(0)

            if guesses == 10:
                print("\nYou have reached the maximum number of tries (10), please try again later.\n")
                exit(0)

if __name__=='__main__':
    main()
