#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the perimeter of a square
#     with inputted side length


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
            flt_side_length = float(str_side_length)
            if flt_side_length <= 0:
                print("Enter valid side length")
                continue
        except Exception:
            print("Enter valid side length")
            continue

        # process
        perimeter = perimeter_calculator(flt_side_length)
        break

    # output
    print("The perimeter of your square is {} cm.".format(perimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()
