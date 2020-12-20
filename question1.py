def select_max(array):
    my_max = 0
    if array: # checking if array has any values or is null
        my_max = array[0] # using first element of array as our starting point
        for i in array:
            if i >= my_max:
                my_max = i
    else:
        my_max = None
    return my_max


if __name__ == "__main__":
    # write your debug code here
    pass
