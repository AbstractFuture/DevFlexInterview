from math import floor


def center_zeros1(array):
    # write your function here
    # center means the floor(x / 2) where floor means rounding a float (decimal number) down to the nearest integer
    # i.e. floor(1) = 1, floor(1.5) = 1, floor(1.75) = 1, floor(2) = 2
    arr_len = len(array)
    print(array)
    if array: # checking if array evaluates to True, else return None type
        for i in array:
            if (array[i] == 0): # if element in array is zero;
                array.pop(i)
                array.insert((floor(arr_len / 2)), 0)
                return(array) # this is insufficient because there may be more than one zero in the array
    else:
        return []



def center_zeros(array): # test to strip out all zeroes from list
    if array: # checking if array evaluates to True, else return None type
        arr_len = len(array)
        zero_count = array.count(0)
        loop_count = 0
        zero_arr = array.copy()
        while loop_count < zero_count:
            for i in range(arr_len):
                #print(zero_arr)
                if zero_arr[i] == 0:
                    #print(zero_arr)
                    zero_arr.pop(i)
                    #print(zero_arr)
                    if (arr_len % 2 == 0):
                        #print(zero_arr)
                        zero_arr.insert(floor(((arr_len)/2)-1), 0)
                        #print(zero_arr)
                    else: # if elements in array are odd
                        #print(zero_arr)
                        zero_arr.insert(floor(arr_len/2), 0)
                        #print(zero_arr)
                    loop_count += 1
                else:
                    pass
        return(zero_arr)
    else:
        return []

if __name__ == "__main__":
    pass

print(center_zeros([1, 1, 3, 0, 6, 0]))
#[1, 1, 0, 0, 3, 6]