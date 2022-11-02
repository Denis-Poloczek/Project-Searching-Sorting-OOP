from application_brain import ApplicationBrain
from class_data import *

app_brain = ApplicationBrain()
print(ascii_art_welcome)

while app_brain.get_state() != 3:
    app_brain.sorting_or_searching_choice()

    if app_brain.get_state() == 3:
        break

    method = app_brain.method_choice()

    if app_brain.get_state() == 1 and method == 7:
        user_list = app_brain.bucket_sort_list_choice()
    elif app_brain.get_state() == 2 and method != 1:
        user_list = app_brain.sorted_list_choice()
    else:
        user_list = app_brain.list_choice()

    result = app_brain.result(method, user_list)

    print(ascii_art_result)
    if app_brain.get_state() == 1:
        print(f"You have used the {sorting_methods_dict[method].lower()} method for sorting. "
              f"The sorted list is: {user_list}")
    else:
        if result != "Element has not been found!":
            print(f"You have used the {searching_methods_dict[method].lower()} method for searching. The target of "
                  f"the search is at index: {result}")
        else:
            print("The element has not been found in the provided list!")
    print(ascii_art_result)
    print("*** Procedure ended with success ***\n")









