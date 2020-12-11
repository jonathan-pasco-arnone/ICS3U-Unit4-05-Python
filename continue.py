#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program adds multiple numbers together


def main():
    # This function takes an optional amount of numbers to be added together

    answer = 0
    print("")
    print("This program adds as many numbers as you want")
    print("")
    counter_str = input("How many numbers would you like to add: ")
    print("")

    try:
        counter = int(counter_str)
    except Exception:
        print("Invalid Input")
    else:

        while counter > 0:
            counter = counter - 1
            number_str = input("Enter a number to add: ")
            try:
                number = int(number_str)
            except Exception:
                continue
            else:
                if not number > 0:
                    continue
                else:
                    answer = answer + number
        print("")
        print("The sum is {}".format(answer))


if __name__ == "__main__":
    main()
