# Module 7
#   Programming Assignment 10
#     Prob-1.py

# Esther Pisano
# Inputs: user inputs numbers and when finished
# inputs a negative number as the sentinel.
# Processes: the computer with sum up all the numbers given before the sentinel
# Outputs: the sum of all the inputed numbers before sentinel.


def main():
    sum = 0.0
    x = float(input("Input next number (negative to quit): "))
    while x >= 0:
        sum = sum + x
        x = float(input("Input next number (negative to quit): "))
    print("The sum of all inputted numbers is", sum)


main()
