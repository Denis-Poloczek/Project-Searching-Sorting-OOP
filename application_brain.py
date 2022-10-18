
from class_data import *
from searching_manager import SearchingManager
from sorting_manager import SortingManager

class ApplicationBrain():

    def __init__(self) -> None:
        self.state= 0

    def change_state(self, value):
        self.state = value

    def sorting_or_searching(self):
        answear = int(input("Please type 1 if you want to sort or type 2 if you want to search:\n "))
        if answear == 1 or answear == 2:
            self.change_state(1)
            return answear
        else:
            print(f"Please try again the answear {answear} is not an allowed choice")
