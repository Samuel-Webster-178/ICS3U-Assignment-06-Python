#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


def perimeter_calculator(side_length):
    # I calculate the perimeter of a square
    perimeter = side_length * 4
    return perimeter


def main():
    # I am main, I manage input and output

    # input
    while True:
        # I repeat until valid input is given
        str_side_length = input("Enter the side length of your square (cm): ")

        # input can neither be negative, nor a string
        try:
            int_side_length = float(str_side_length)
            if int_side_length <= 0:
                continue
        except Exception:
            continue

        # process
        perimeter = perimeter_calculator(int_side_length)
        break

    # output
    print("The perimeter of your square is {} cm.".format(perimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()
