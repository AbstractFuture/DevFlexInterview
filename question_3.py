def minimum_points(threshold, points):
  
    # if sum of points between points[0] and current iterable is greater than threshold
    # store and return the number of elements summed as the answer
    # since it is possible to solve i + 1 or i + 2, i can use modulus to determine min points


    # if there is only a single point
    # immediately return 1 because the student must solve all (1) questions
    if (len(points) == 1): 
        return 1
    
    # if points array has more than one element in it
    elif (len(points) == 2):
        return 2

    else: # if points array has 3 or more elements in it
        # initialize variable to keep track of loop count
        loop_count = 0
        # initialize variable to keep track of current sum
        current_sum = 0

        # initialize i+1 and i+2 variables
        plus1 = 0
        plus1list = []
        plus2 = 0
        plus2list = []
        # below statements sums all elements in 3 element long list
        #print(sum(points[0:(0+3)]))

        # compare current sum to threshold
        for i in range(len(points) -1):
            
            loop_count += 1
            current_sum += i

            # calculate i + 1 and i + 2
            # add value at i with value of next element
            # sum(points[i:(i+2)]) actually sums i + i's next element, not i + i's second element
            # this is because list slicing is exlusive of the number used to show the stopping point
            #plus1 = sum(points[i:(i+2)]) # this actually sums i + i's next element, not i + i's second element
            plus1 = points[i] + points[i+1]
            plus1list.append(plus1)
            plus2 = sum(points[i:(i+3)]) # this is i + 2
            plus2list.append(plus2)

            # now I think I need to compare current diff values (in the plus1list and plus2 list) to the threshold
            #if 

        print(plus1list)
        print(plus2list)

#if __name__ == "__main__":

#    pass

print(minimum_points(2, [1, 2, 3]))
