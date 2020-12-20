from math import floor


def center_zeros(array):
    # write your function here
    # center means the floor(x / 2) where floor means rounding a float (decimal number) down to the nearest integer
    # i.e. floor(1) = 1, floor(1.5) = 1, floor(1.75) = 1, floor(2) = 2
    arr_len = len(array)
    if array: # checking if array is empty
        for i in array:
            if (i == 0) and (array[:i] == floor(arr_len / 2)): # not sure if array[:i] returns an int or the value of the element
                pass
    else:
        return []


if __name__ == "__main__":
    # write your debug code here
    pass