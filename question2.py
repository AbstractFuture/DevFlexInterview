from math import floor


def center_zeros(array):
    # write your function here
    # center means the floor(x / 2) where floor means rounding a float (decimal number) down to the nearest integer
    # i.e. floor(1) = 1, floor(1.5) = 1, floor(1.75) = 1, floor(2) = 2
    arr_len = len(array)
    print(array)
    if array: # checking if array evaluates to True, else return None type
        for i in array:
            if (array[i] == 0): # if element in array is zero;
                print(array)
                array.pop(i)
                print(array)
                array.insert((floor(arr_len / 2)), 0)
                return(array)
    else:
        return []


if __name__ == "__main__":
    pass

print(center_zeros([1, 1, 3, 0, 6, 0]))
#[1, 1, 0, 0, 3, 6]