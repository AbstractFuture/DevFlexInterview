from math import floor
# from math import ceil


def center_zeros(array): 
    if array: # checking if array evaluates to True, else return None type
    
        zero_count = array.count(0)
        # lambda function below keeps non zero elements in new list
        without_zero = list(filter(lambda x: x != 0, array))
        # Then create a copy of the above list
        # which we will insert zeros into
        with_zero = without_zero.copy()
        

        # if zero count is even
        # and num of non zero elements in array is even
        if (zero_count % 2 ==0) and (len(without_zero) % 2 == 0):
            # then insert zeros at the specified index
            for i in range(zero_count):
                index = floor(len(with_zero)/2)
                with_zero.insert(index,0)
            return(with_zero)

        
        # if zero count is odd
        # and num of non zero elements in array is odd
        elif not(zero_count % 2 ==0) and not(len(without_zero) % 2 == 0):
            # then insert zeros at the following index
            for i in range(zero_count):
                index = floor(len(with_zero)/2)
                offset = 1
                with_zero.insert((index + 1),0)
            return(with_zero)


        # if zero count is odd
        # and num of non zero elements in array is even
        elif not(zero_count % 2 ==0) and (len(without_zero) % 2 == 0):
            # then insert zeros at the following position
            for i in range(zero_count):
                index = floor(len(with_zero)/2)
                with_zero.insert(index,0)
            return(with_zero)

        else: # if zero count is even
            # and num of non zero elements is odd
            # then insert zeros at the following position
            for i in range(zero_count):
                index = floor(len(with_zero)/2)
                with_zero.insert(index,0)
            return(with_zero)
    else:
        return []

if __name__ == "__main__":
    pass
