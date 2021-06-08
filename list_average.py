#!/usr/bin/env python3

# Created by: Jenoe Balote
# Created on June 2021
# This program determines the average of a 2D list
#    with limitations inputted by the user

import random


def calculate_average(number_list, rows, columns):
    # This function calculates the average

    # sum of numbers in list
    total = 0

    for row_counter in number_list:
        for column_counter in row_counter:
            total += column_counter
    average = total / (rows * columns)

    return average


def main():
    # this function generates the random numbers in the list

    list_of_numbers = []

    # input
    print("Let's average out some lists!")
    rows_string = str(input("How many rows would you like?: "))
    columns_string = str(input("How many columns would you like?: "))
    print("\nGenerating numbers...")
    print("")

    # process and output
    try:
        rows = int(rows_string)
        columns = int(columns_string)
        for loop_counter in range(0, rows):
            temp = []
            for loop_counter in range(0, columns):
                random_number = random.randint(1, 50)
                temp.append(random_number)
                print("{0} ".format(random_number), end="")
            list_of_numbers.append(temp)
            print("")
            # call function(s)
        average = calculate_average(list_of_numbers, rows, columns)
        print("\nThe average is {}.".format(average))
    except Exception:
        print("Invalid.")
    print("\nThanks for participating!")


if __name__ == "__main__":
    main()
