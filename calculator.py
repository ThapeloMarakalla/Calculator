def add(x, y):
    """" Adds two numbers """
    return x + y


def subtract(x, y):
    """ Subtracts two numbers """
    return x - y


def multiply(x, y):
    """ Multiples two numbers """
    return x * y


def divide(x, y):
    """Divides two numbers"""
    return x / y


def modulus(x, y):
    """Return the remainder of two numbers, after division"""
    return x % y


def check_if_user_has_finished():
    """
    Checks that the user wants to finish or not.
    Performs some verification of the input."""
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Do you want to finish (y/n): ').lower()
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Response must be (y/n), please try again')
    return ok_to_finish


def get_operation_choice():
    input_ok = False
    while not input_ok:
        print('Menu Options are:')
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3. Multiply')
        print('\t4. Divide')
        print('\t5. Modulus')
        print('-----------------')
        user_selection = input('Please make a selection: ')
        if user_selection in (str(x) for x in range(1, 6)):
            input_ok = True
        else:
            print('Invalid Input (must be 1 - 6)')
    print('-----------------')
    return user_selection


def get_numbers_from_user():
    num1 = get_integer_input('Input the first number: ')
    num2 = get_integer_input('Input the second number: ')
    return num1, num2


def get_integer_input(message):
    value_as_string = input(message)
    while not value_as_string.lstrip('-').isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)
    return int(value_as_string)


operation = {'1': add, '2': subtract, '3': multiply,
             '4': divide, '5': modulus}
finished = False
while not finished:
    result = 0
    menue_choice = get_operation_choice()
    n1, n2 = get_numbers_from_user()
    result = operation[menue_choice](n1, n2)
    print('Result:', result)
    print('=================')
    finished = check_if_user_has_finished()

print('Bye')
