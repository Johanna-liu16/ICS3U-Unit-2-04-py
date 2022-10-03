#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program calculates the cost of making a pizza

import constants


def main():
    # this function calculates the cost of making a pizza

    # input
    print("Welcome! Enter the diameter of your pizza to calculate the price.")
    diameter = int(input("Enter the diameter of the pizza: "))

    # process
    sub_total = constants.RENT + constants.LABOR + (constants.COST_PER_INCH * diameter)
    tax = sub_total * constants.HST
    total = sub_total + tax

    # output
    print("The cost of your pizza is ${0}.".format(round(total, 2)))

    print("\nDone.")


if __name__ == "__main__":
    main()
