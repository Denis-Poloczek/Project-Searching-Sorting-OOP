from sorting_manager import SortingManager
from searching_manager import SearchingManager
from class_data import *
import time

class ApplicationBrain():

    def __init__(self):
        self.choice_list = None
        self.state = 0

    def change_state(self, value):
        self.state = value
        self.choice_list = {1: "sort", 2: "search"}

    def get_state(self):
        return self.state

    def sorting_or_searching_choice(self):
        answear = input("Please type 1 if you want to sort or type 2 if you want to search, otherwise if you "
                            "want to quite the program press 3: \n\n")
        while not answear.isdigit():
            answear = input("You have used a non-digit sequence, please try one more time and specify "
                            "options you want to choose:\n")
        if int(answear) == 1:
            self.change_state(1)
        elif int(answear) == 2:
            self.change_state(2)
        elif int(answear) == 3:
            print("The app is shut down, thank you for using the searching and sorting app \n")
            print(ascii_art_2)
            self.change_state(3)
        else:
            print(f"Please try again the answear {answear} is not an allowed choice \n")

    def method_choice(self):
        if self.get_state() == 1:
            print(f"\nYou can use the following method for {self.choice_list[self.state]}ing:\n")
            for number, method in sorting_methods_dict.items():
                print(f"Choose {number} for {method}\n")
            while True:
                try:
                    answear = int(input(
                        f"Please provide the number corresponding to your chosen {self.choice_list[self.state]}ing method:\n"))
                    if not 1 <= int(answear) <= 7:
                        answear = int(input("Try one more time - you have chosen value outside of 1 to 7 range!\n"))
                except ValueError:
                    print("You have provided non-integer value !\n")
                    continue
                if not 1 <= int(answear) <= 7:
                    print("Try one more time - you have chosen value outside of 1 to 7 range!\n")
                    continue
                else:
                    break
            return answear
        elif self.get_state() == 2:
            print(f"\nYou can use the following method for {self.choice_list[self.state]}ing:\n")
            for number, method in searching_methods_dict.items():
                print(f"Choose {number} for {method}\n")
            while True:
                try:
                    answear = int(input(
                        f"Please provide the number corresponding to your chosen {self.choice_list[self.state]}ing method:\n"))
                    if not 1 <= int(answear) <= 5:
                        answear = int(input("Try one more time - you have chosen value outside of 1 to 5 range!\n"))
                except ValueError:
                    print("You have provided non-integer value!\n")
                    continue
                if not 1 <= int(answear) <= 5:
                    print("Try one more time - you have chosen value outside of 1 to 5 range!\n")
                    continue
                else:
                    break
            return answear
        else:
            return

            return answear

    def result(self, method_choice, user_list):
        if self.get_state() == 1:
            sorting_manager = SortingManager()
            match method_choice:
                case 1:
                    sorting_manager.selection_sort(user_list)
                case 2:
                    sorting_manager.insertion_sort(user_list)
                case 3:
                    sorting_manager.shell_sort(user_list)
                case 4:
                    sorting_manager.bubble_sort(user_list)
                case 5:
                    sorting_manager.merge_sort(user_list)
                case 6:
                    sorting_manager.quicksort(user_list, 0, len(user_list) - 1)
                case 7:
                    sorting_manager.bucket_sort(user_list)
        elif self.get_state() == 2:
            searching_manager = SearchingManager()
            user_target = int(input("please provide your target for the searching procedure: \n"))
            match method_choice:
                case 1:
                    print(f"The index of search is {searching_manager.linear_search(user_list, user_target)}\n")
                case 2:
                    print(f"The index of search is {searching_manager.jump_search(user_list, user_target)}\n")
                case 3:
                    return searching_manager.binary_search(user_list, 0, len(user_list), user_target)
                case 4:
                    print(f"The index of search is {searching_manager.interpolation_search(user_list, 0, len(user_list) - 1, user_target)}\n")
                case 5:
                    print(f"The index of search is {searching_manager.exponential_search(user_list, user_target)}\n")


    def list_choice(self):
        users_list = []
        answear = input("Please specify how many elements would you like to have in your list:\n")
        while not answear.isdigit():
            answear = input("You have used a non-digit sequence, please try one more time and specify "
                            "how many elements would you like to have in your list:\n")
        for i in range(int(answear)):
            answear_num = input(f"Please provide the element of index {i}: \n")
            while not answear_num.isdigit():
                answear_num = input(
                    "You have tried a non-digit sequence, please try one more time to provide number:  \n")
            users_list.append(int(answear_num))

        print(f"The list that you provided is: {users_list}\n")

        return users_list

    def sorted_list_choice(self):

        print("You have chosen a method of search that requires sorted list!\n")
        users_list = []

        while True:

            answear = input("Please specify how many elements would you like to have in your list:\n")
            while not answear.isdigit():
                answear = input("You have used a non-digit sequence, please try one more time and specify "
                            "how many elements would you like to have in your list:\n")
            for i in range(int(answear)):
                answear_num = input(f"Please provide the element of index {i}: \n")
                while not answear_num.isdigit():
                    answear_num = input(
                    "You have tried a non-digit sequence, please try one more time to provide number:  \n")
                users_list.append(int(answear_num))
            if sorted(users_list) == users_list:
                break
            print("You have provided an unsorted list of elements! Please try one more time")
            users_list = []

        print(f"The list that you provided is: {users_list}\n")

        return users_list


    def is_user_list_sorted(self, user_list):
        if user_list == user_list.sort():
            return True
        return False

    def bucket_sort_list_choice(self):
        users_list = []
        answear = input("Please specify how many numbers would you like to have in your list:\n")
        while not answear.isdigit():
            answear = input("You have used a non-digit sequence, please try one more time and specify "
                            "how many numbers would you like to have in your list:\n")
        for i in range(int(answear)):
            while True:
                try:
                    num = float(input(f"Please provide the float element between 0 and 1 of index {i} to your list:\n"))
                except ValueError:
                    print("You have entered a not valid sequence!")
                    continue
                if not 0 <= num <= 1:
                    print("Try one more time - you have chosen a float value outside of 0 to 1 range!\n")
                    continue
                else:
                    break
            users_list.append(float(num))

        print(f"The list that you provided is: {users_list}\n")

        return users_list


app = ApplicationBrain()
app.sorted_list_choice()