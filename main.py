# from sorting_manager import SortingManager
# from searching_manager import SearchingManager
#
#
# termination_flag = False
#
# while not termination_flag:
#
#     sorting_manager = SortingManager()
#     searching_manager = SearchingManager()
#
#
#     print("Please choose either 1 for sorting your list or 2 for searching your list ")
#     answer = int(input("Please enter your choice: "))
#
#     if answer == 1:
#         print("Availble soritng methods are as follows")
#         sorting_manager.get_available_methods()
#         answer = int(input("Please choose the number next to a method you would like to use: "))
#         method_choosen = sorting_manager.methods_details[answer]
#         sorting_manager.method_choosen([3,7,3,4])

from application_brain import ApplicationBrain

application_brain = ApplicationBrain()

while application_brain.state == 0:
    choice_1 = application_brain.sorting_or_searching()







