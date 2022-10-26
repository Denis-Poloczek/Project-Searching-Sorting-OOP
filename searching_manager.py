from manager import Manager
from class_data import *
import math


class SearchingManager(Manager):

    def __init__(self):
        super().__init__()
        self.methods = searching_methods_dict
        self.methods_details = searching_methods_details_dict

    def linear_search(self, list_of_elements, target):
        """Please provide 2 arguments: a list of elements and the target you are looking for"""

        for element in list_of_elements:
            if element == target:
                return list_of_elements.index(element)
        return "element has not been found!"

    def jump_search(self, list_of_elements, target):
        """Please provide 2 arguments: a list of sorted** elements and the target you are looking for"""

        jump_size = math.sqrt(len(list_of_elements))

        block = 0
        while list_of_elements[int(min(jump_size, len(list_of_elements)) - 1)] < target:
            block = int(jump_size)
            jump_size += math.sqrt(len(list_of_elements))
            if block >= len(list_of_elements):
                return "Element has not been found"

        while list_of_elements[int(block)] < target:
            block += 1

            if block == min(jump_size, len(list_of_elements)):
                return "Element has not been found"

        if list_of_elements[int(block)] == target:
            return block

        return "Element has not been found"

    def is_sorted_helper(self, list_of_elements):
        if list_of_elements == sorted(list_of_elements):
            return True
        return False

    def binary_search(self, list_of_elements, start_idx, end_idx, target):
        """Please provide 2 arguments: a list of sorted elements and the target you are looking for"""

        if not self.is_sorted_helper(list_of_elements):
            return "Please provide a sorted list for this search method"

        while start_idx <= end_idx:

            mid = start_idx + (end_idx - start_idx) // 2

            if list_of_elements[mid] == target:
                return mid
            elif list_of_elements[mid] < target:
                start_idx = mid + 1
            else:
                end_idx = mid - 1

        return "element has not been found!"

    def interpolation_search(self, list_of_elements, low_idx, up_idx, target):
        """Please provide 4 arguments: a list of sorted elements, the target you are looking for,
        lower and upper indexes of your searched list"""

        if not self.is_sorted_helper(list_of_elements):
            return "Please provide a sorted list for this search method"

        if low_idx <= up_idx and list_of_elements[low_idx] <= target <= list_of_elements[up_idx]:

            pivot = low_idx + ((up_idx - low_idx) // (list_of_elements[up_idx] - list_of_elements[low_idx])) * \
                    (target - list_of_elements[low_idx])

            if list_of_elements[pivot] == target:
                return pivot

            if list_of_elements[pivot] < target:
                return self.interpolation_search(list_of_elements, pivot + 1, up_idx, target)

            if list_of_elements[pivot] > target:
                return self.interpolation_search(list_of_elements, low_idx, up_idx - 1, target)

        return "Element has not been found!"

    def exponential_search(self, list_of_elements, target):
        """Please provide 2 arguments: a list of sorted elements and the target you are looking for"""

        if not self.is_sorted_helper(list_of_elements):
            return "Please provide a sorted list for this search method"

        if list_of_elements[0] == target:
            return 0

        i = 1
        while i < len(list_of_elements) and list_of_elements[i] <= target:
            i = i * 2
        return self.binary_search(list_of_elements, i // 2, min(i, len(list_of_elements) - 1), target)


# s = SearchingManager()
# print(s.binary_search([2, 5, 7, 9],0, 4,  7))