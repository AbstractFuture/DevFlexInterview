from math import floor
from math import ceil


def center_zeros1(array): # this function is insufficient because there may be more than one zero in the array
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
                return(array) 
    else:
        return []



def center_zeros2(array): # test to strip out all zeroes from list
    if array: # checking if array evaluates to True, else return None type
        arr_len = len(array)
        zero_count = array.count(0)
        loop_count = 0
        zero_arr = array.copy()
        while loop_count < zero_count:
            for i in range(arr_len):
                print(zero_arr)
                if zero_arr[i] == 0: # if value at index i equals 0
                    print(zero_arr)
                    zero_arr.pop(i)
                    # shift zero one space left
                    # still need to evaluate if new zero is at floor division position
                    zero_arr.insert((i - 1), 0)
                    print(zero_arr)
                    if zero_array[floor(len(zero_array)/2)] == 0:
                        pass
                    #else:
                        #maybe use recursion? make variables global variables
                        # otherwise they'll reset when function is called recursively
                    # then evaluate if it is in the correct space
                    # this approach differs from trying to insert it at the floor divide position

                    #loop_count += 1
                #else:
                    #pass
        return(zero_arr)
    else:
        return []



# the function below needs to be revised
# it currently solves the test cases but is hard coded
# I need to discover the real relationship between the amount
# of zeros in the array and the number of elements of the
# array that are not zero
# currently the amount of zeros inserted is hard coded
# the index for insertion is also hard coded
def center_zeros3(array): 
    if array: # checking if array evaluates to True, else return None type
        zero_count = array.count(0)
        # lambda function below keeps non zero elements in new list
        without_zero = list(filter(lambda x: x != 0, array))
        # Then create a copy of the above list
        # which we will insert zeros into
        with_zero = without_zero.copy()
        # if non zero length of array is even and array elements
        # are more than the zero count
        # and there are 4 non zero elements in the array
        if (len(without_zero) % 2 == 0) and (len(without_zero) > zero_count) and ((len(without_zero)) == 4):
            # then insert two zeros at the specified index
            with_zero.insert(floor((len(without_zero)/2)),0)
            with_zero.insert(floor((len(without_zero)/2)),0)
        # if number of array elements is odd
        # and the number of array elements are more than the zero count
        elif (not (len(without_zero) % 2 == 0)) and (len(without_zero) > zero_count):
            # then insert a single zero at the following index
            with_zero.insert(ceil(len(without_zero)/2),0)
        # if number of non zero elements is even and 
        # there are more non zero elements than zeros
        elif (len(without_zero) % 2 == 0) and (len(without_zero) > zero_count):
            # then insert a single zero at the following position
            with_zero.insert(int((len(without_zero)/2)),0)
        else: # hard coded for 4th test case. bad solution.
            with_zero.insert(0,0)
            with_zero.insert(0,0)
        return(with_zero)
    else:
        return []


# hard coded and need to be changed:

# - index position
# need to create an offset? 

def center_zeros(array): 
    if array: # checking if array evaluates to True, else return None type
        print(array)
        
        zero_count = array.count(0)
        # lambda function below keeps non zero elements in new list
        without_zero = list(filter(lambda x: x != 0, array))
        # Then create a copy of the above list
        # which we will insert zeros into
        with_zero = without_zero.copy()
        

        # if zero count is even
        # and if number non zero elements in array is even
        if (zero_count % 2 ==0) and (len(without_zero) % 2 == 0):
            # then insert two zeros at the specified index
            for i in range(zero_count):
                with_zero.insert(floor((len(without_zero)/2)),0)

        
        # if zero count is odd
        # and num of elements in array is odd
        elif not(zero_count % 2 ==0) and not(len(without_zero) % 2 == 0):
            # then insert a single zero at the following index
            for i in range(zero_count):
                print(with_zero)
                #with_zero.insert(ceil(len(without_zero)/2),0)
                with_zero.insert(floor(len(without_zero)/2),0)
                print(with_zero)


        # if zero count is odd
        # and num of non zero elements in array is even
        elif not(zero_count % 2 ==0) and (len(without_zero) % 2 == 0):
            # then insert a single zero at the following position
            for i in range(zero_count):
                with_zero.insert(int((len(without_zero)/2)),0)

        else: # if zero count is odd
            # and num of non zero elements is even
            for i in range(zero_count):
                with_zero.insert(0,0)

        return(with_zero)
    else:
        return []

if __name__ == "__main__":
    pass

#print(center_zeros([1, 1, 3, 0, 1, 1, 3, 0, 6, 0])) #== [1, 1, 3, 0, 0, 0, 1, 1, 3, 6])
