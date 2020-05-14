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
        print('\t6. Exponentiation')
        print('-----------------')
        user_selection = input('Please make a selection: ')
        if user_selection in (str(x) for x in range(1,7)):
            input_ok = True
        else:
            print('Invalid Input (must be 1 - 6)')
    print('-----------------')
    return user_selection

finished = False
while not finished:
    result = 0
    menue_choice = get_operation_choice()
    # Get the numbers from the user
    # Select the operation
    print('Result:', result)
    print('=================')
    finished = check_if_user_has_finished()

print('Bye')
