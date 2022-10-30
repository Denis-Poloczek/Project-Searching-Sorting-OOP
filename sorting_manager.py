from class_data import *
from random import randrange
from manager import Manager


class SortingManager(Manager):

    def __init__(self):
        super().__init__()
        self.methods = sorting_methods_dict
        self.methods_details = sorting_methods_details_dict

    def insertion_sort(self, list_of_elements):
        """1 argument: a list of elements that needs to be sorted"""

        for i in range(1, len(list_of_elements)):
            j = i
            checked_element = list_of_elements[j]

            while (j > 0) & (list_of_elements[j - 1] > checked_element):
                list_of_elements[j] = list_of_elements[j - 1]

                j -= 1

            list_of_elements[j] = checked_element

           
    def selection_sort(self, list_of_elements):
        """1 argument: a list of elements that needs to be sorted"""

        for i in range(len(list_of_elements)):
            min_index = i

            for k in range(i + 1, len(list_of_elements)):
                if list_of_elements[k] < list_of_elements[min_index]:
                    min_index = k

            (list_of_elements[i], list_of_elements[min_index]) = (list_of_elements[min_index], list_of_elements[i])

    def shell_sort(self, list_of_elements):
        """ 1 argument: a list of elements that needs to be sorted"""

        gap = len(list_of_elements) // 2

        while gap > 0:

            for i in range(gap, len(list_of_elements)):
                temp = list_of_elements[i]
                j = i

                while j >= gap and list_of_elements[j - gap] > temp:
                    list_of_elements[j] = list_of_elements[j - gap]
                    j -= gap

                list_of_elements[j] = temp
            gap //= 2

    def bubble_sort(self, list_of_elements):
        """1 argument: a list of elements that needs to be sorted"""

        for i in range(len(list_of_elements)):

            for j in range(0, len(list_of_elements) - i - 1):

                if list_of_elements[j] > list_of_elements[j + 1]:
                    list_of_elements[j], list_of_elements[j + 1] = list_of_elements[j + 1], list_of_elements[j]

    def merge_sort(self, list_of_elements):
        """1 argument: a list of elements that needs to be sorted"""

        if len(list_of_elements) > 1:

            split_point = len(list_of_elements) // 2
            L = list_of_elements[:split_point]
            R = list_of_elements[split_point:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = 0
            j = 0
            k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    list_of_elements[k] = L[i]
                    i += 1
                else:
                    list_of_elements[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                list_of_elements[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                list_of_elements[k] = R[j]
                j += 1
                k += 1

    def quicksort(self, list_of_elements, beginning, end):
        """3 arguments: list that needs to be sorted, start index and last index of the list"""

        if beginning >= end:
            return
        pivot_index = randrange(beginning, end + 1)
        pivot_element = list_of_elements[pivot_index]

        list_of_elements[end], list_of_elements[pivot_index] = list_of_elements[pivot_index], list_of_elements[end]

        less_than_pointer = beginning

        for i in range(beginning, end):

            if list_of_elements[i] < pivot_element:
                list_of_elements[i], list_of_elements[less_than_pointer] = list_of_elements[less_than_pointer], \
                                                                           list_of_elements[i]
                less_than_pointer += 1
        list_of_elements[end], list_of_elements[less_than_pointer] = list_of_elements[less_than_pointer], \
                                                                     list_of_elements[end]

        self.quicksort(list_of_elements, beginning, less_than_pointer - 1)
        self.quicksort(list_of_elements, less_than_pointer + 1, end)

    def bucket_sort(self, list_of_elements):
        """1 argument: a list of elements that needs to be sorted,
        elements should be in the range of (0,1)"""

        def sorting_helper(bucket_to_be_sorted):
            for i in range(1, len(bucket_to_be_sorted)):
                up = bucket_to_be_sorted[i]
                j = i - 1
                while j >= 0 and bucket_to_be_sorted[j] > up:
                    bucket_to_be_sorted[j + 1] = bucket_to_be_sorted[j]
                    j -= 1
                bucket_to_be_sorted[j + 1] = up
            return bucket_to_be_sorted

        buckets = []
        buckets_number = 10  # 10 means 10 slots, each
        # slot's size is 0.1
        for i in range(buckets_number):
            buckets.append([])

        for j in list_of_elements:
            index_b = int(buckets_number * j)
            buckets[index_b].append(j)

        for i in range(buckets_number):
            buckets[i] = sorting_helper(buckets[i])

        k = 0
        for i in range(buckets_number):
            for j in range(len(buckets[i])):
                list_of_elements[k] = buckets[i][j]
                k += 1
        return list_of_elements



