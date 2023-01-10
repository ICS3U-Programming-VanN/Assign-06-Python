#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: December 20, 2022
# This program asks the user if they want to multiply/divide a
# list by a multiplier/divisor OR if the user wants to find the
# common/uncommon elements of two lists


# This function finds the uncommon elements in two lists and returns them in a list
def uncommon_elements(list_of_elements, list_of_elements2):
    # Initializes uncommon elements list
    uncommon_elements_list = []

    # Iterates through each element of the first list
    for index in list_of_elements:
        # IF the index of the first list if not in the second list
        if index not in list_of_elements2:
            # Adds the element to the uncommon elements list
            uncommon_elements_list.append(index)

    # Iterates through each element in the second list
    for index in list_of_elements2:
        # IF the index of the second list is not in the first list
        if index not in list_of_elements:
            # Adds the element to the uncommon elements list
            uncommon_elements_list.append(index)

    # Returns the uncommon elements list to function call
    return uncommon_elements_list


# This function finds the common elements of two lists and returns them in a list
def common_elements(list_of_elements, list_of_elements2):
    # Initializes the common elements list
    common_elements_list = []

    # Iterates through each index of the first list
    for index in list_of_elements:
        # IF the index if present in the second list
        if index in list_of_elements2:
            # Adds the element to common elements list
            common_elements_list.append(index)

    # Returns the list of common elements to function call
    return common_elements_list


# This function multiplies each integer in a list by a multiplier and returns a list of every element multiplied
def list_multiplier(list_ints, multiplier):
    # Loops for the length of the list to multiply each index
    for index in range(len(list_ints)):
        # Multiplies index by the multiplier
        list_ints[index] *= multiplier

    # Returns the multiplied list to function call
    return list_ints


# This function divides each integer in a list by a divisor and returns a list of every element divided
def list_divisor(list_ints, divisor):
    # Loops for the length of the list to divide each index by the divisor
    for index in range(len(list_ints)):
        # Divides each index of the list by the divisor
        list_ints[index] /= divisor

    # Returns the divided list to function call
    return list_ints


def main():
    # Loops the program until user states otherwise
    while True:
        # Initializes and resets variables
        yes_or_no = ""
        multiplier_or_common = ""
        multiply_or_divide = ""
        common_or_uncommon = ""
        second_user_list = []
        user_list = []

        # Displays to user how they should input a list
        print("\nExample on how to input a list:\nInput a list: 2 5 3 5\n")

        # Ensures that the user inputs either 1 or 2
        while multiplier_or_common != "1" or multiplier_or_common != "2":
            # Asks user if they want have the program do problem #1 (multiply each element in a list) or problem #2 (common elements of two lists)
            multiplier_or_common = input(
                "Do you want to multiply/divide a list of integers (Option 1)?\nOR\nDo you want to find the common/uncommon elements of two lists (Option 2)?\n\nEnter '1' for the first option or '2' for the second option: "
            )

            # Breaks out of the loop if the user enters valid input
            if multiplier_or_common == "1" or multiplier_or_common == "2":
                # Exits loop
                break

        # IF the user wants to multiply/divide each element in a list
        if multiplier_or_common == "1":
            # Ensures that the user inputs either 1 or 2
            while multiply_or_divide != "1" or multiply_or_divide != "2":
                # Asks user if they want to multiply or divide each element in a list
                multiply_or_divide = input(
                    "Do you want to multiply or divide the list of integers? (Enter '1' to multiply or '2' to divide): "
                )

                # Exits loops if the user enters valid input
                if multiply_or_divide == "1" or multiply_or_divide == "2":
                    # Breaks out of loop
                    break

            # Asks user for their list of integers (splits string into list)
            user_list = input("Enter a list of integers separated by spaces: ").split()

            # Initializes list to hold the integers
            user_list_int = []

            # Checks for exceptions
            try:
                # Iterates through each index of the user's list
                for index in user_list:
                    # Casts user's number/index into an integer and adds it to the integer list
                    user_list_int.append(int(index))

            # In the event of an exception occurring
            except Exception:
                print("You must enter a list of integers separated by spaces!")

            # In the event of valid integers
            else:
                # Checks for exceptions
                try:
                    # IF the user wishes to multiply the numbers in the list
                    if multiply_or_divide == "1":
                        # Asks user for the number they want to multiply with
                        user_multiplier = float(input("Enter a multiplier: "))
                    # IF the user wants to divide the numbers in the list
                    else:
                        # Asks the user for the number they want to divide with
                        user_divisor = float(input("Enter a divisor: "))

                        # IF the user tries to divide with 0
                        if user_divisor == 0:
                            # Displays to user error message
                            print(
                                "You cannot have 0 as the divisor. Please try the program again.\n"
                            )

                            # Repeats the program
                            continue

                # In the event of an exception with the multiplier/divisor
                except Exception:
                    print(
                        "You must enter a number for the multiplier/divisor! (0 is not allowed for the divisor)\n"
                    )

                # IF all input was valid
                else:
                    # IF the user wants to multiply the elements of the list
                    if multiply_or_divide == "1":
                        # Calls function to multiply each element of the list by multiplier
                        list_multiplied = list_multiplier(
                            user_list_int, user_multiplier
                        )

                        # Displays to user the multiplied elements in the list
                        print(
                            f"The product of each element with the multiplier is: {list_multiplied}"
                        )
                    # IF the user wants to divide each element in the list
                    else:
                        # Calls function to divide each element in the list by the divisor
                        list_divided = list_divisor(user_list_int, user_divisor)

                        # Displays the elements of the list divided
                        print(
                            f"The quotient of each element with the divisor is: {list_divided}"
                        )

        # IF the user wanted to find the common/uncommon elements in 2 lists
        elif multiplier_or_common == "2":
            # Ensures that that the user either enters 1 or 2
            while common_or_uncommon != "1" or common_or_uncommon != "2":
                # Asks user if they want to list the common or uncommon elements of 2 lists
                common_or_uncommon = input(
                    "\nDo you want to find the common or uncommon elements of two lists?\n(Enter '1' for the common elements or enter '2' for the uncommon elements): "
                )

                # IF the user inputs valid input (1 or 2)
                if common_or_uncommon == "1" or common_or_uncommon == "2":
                    # Exits repeating loop
                    break

            # Asks user for their first list
            user_list = input("Enter a list of elements separated by spaces: ").split()

            # Asks user for their second list of elements
            second_user_list = input(
                "Enter another list of elements separated by spaces: "
            ).split()

            # IF the user wants to find the common elements
            if common_or_uncommon == "1":
                # Calls function to find the common elements of the two lists
                user_common_elements = common_elements(user_list, second_user_list)

                # IF the there are no common elements/the list returned empty
                if user_common_elements == []:
                    # Displays to user that there were no common elements
                    print("\nThese two lists have no common elements!")
                # IF there was common element(s) in two lists
                else:
                    # Displays to the user the common elements
                    print(f"\nThe common elements are: {user_common_elements}")
            # IF the user wants to find the uncommon elements of the two lists
            else:
                # Calls function to find the uncommon elements of the two lists
                user_uncommon_elements = uncommon_elements(user_list, second_user_list)

                # IF there were not any uncommon elements/function returned empty list
                if user_uncommon_elements == []:
                    # Displays to user that there were no uncommon elements
                    print("\nThese two lists have no uncommon elements!")
                # IF there were any uncommon element(s)
                else:
                    # Displays to the user the uncommon elements
                    print(f"\nThe uncommon elements are: {user_uncommon_elements}")

        # Asks user if they want to run the program again
        yes_or_no = input(
            "Do you want to repeat the program? (Enter anything to repeat or '2' to end the program): "
        )

        # IF the user want to end the program
        if yes_or_no == "2":
            # Exits loop and program ends
            break


if __name__ == "__main__":
    main()
