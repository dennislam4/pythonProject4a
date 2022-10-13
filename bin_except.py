# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-12-2022
# Description: Modified binary search function form the exploration so that it raises a TargetNotFound exception instead
# of returning -1.

class TargetNotFound(Exception):
    """Exception class"""
    pass


def binary_search(a_list, target):
    """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, returns -1, indicating the target value isn't in the list
  """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        elif a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound
