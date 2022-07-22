import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def side_order():
    return random.choice(['mac and cheese', 'green beans', 'mashed '
                          'potatoes', 'french fries'])


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, that's not a valid option.")
    return response


def intro():
    print_pause("Hi! Welcome to 'We Pick, You Pick'!")
    print_pause("Here our customers pick their entree and we pick the side.")
    print_pause("The first entree is smothered chicken breasts.")
    print_pause("The second is a fan favorite: surf and turf.")


def get_order():
    response = valid_input("Please select your entree. "
                           "Would you like chicken or surf and turf?\n",
                           "chicken", "surf and turf")
    if "chicken" in response:
        print_pause("Nice! Can't go wrong with chicken!")
    elif "surf and turf" in response:
        print_pause("Excellent choice! We love this entree!")
    print_pause("Your entree today will come with:")
    print(side_order())
    print_pause("Your order will be ready shortly.")
    order_again()


def order_again():
    response = valid_input("Would you like to place another order? "
                           "Please say 'yes' or 'no'.\n",
                           "yes", "no")
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("Ok! Order again.")
        get_order()


def order_food():
    intro()
    get_order()


order_food()
