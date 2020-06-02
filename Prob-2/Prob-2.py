# Module 7
#   Programming Assignment 10
#     Prob-2.py

# <Esther Pisano


def main():
    # f is the file read variable/label
    f = open("Prob-2-Input.txt", "r")
    # prints the whole file
    # print(f.read())

    # this will hold all the numbers
    all_num = []

    # prints file line by line
    for line in f:
        # get the numbers into another list
        line_nums = line.split()
        # append that list to the mother list

        #print("adding the list: ", line, " to all_num: ", all_num, "to get : ", all_num + line_nums, "\n\n")
        all_num = all_num + line_nums

    sum = 0

    for num in all_num:
        print(num)
        sum = sum + int(num)

    print("total sum: ", sum)


main()
