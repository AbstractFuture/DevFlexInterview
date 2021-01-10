def minimum_points(threshold, points):
  
    # if sum of points between points[0] and current iterable is greater than threshold
    # store and return the number of elements summed as the answer

    # if there is only a single point
    # immediately return 1 because the student must solve all (1) questions
    if (len(points) == 1): 
        return 1
    
    # if points array has 2 element in it
    elif (len(points) == 2):
        return 2

    else: # only if points array has 3 or more elements in it
        # because only an array of at least 3 would satisfy the condition of
        # sum between points (sum between first element and nth element in arary)


        # initialize i+1 and i+2 variables
        # initialize empty lists to hold values of i+1 and i+2 in the iteration
        plus1 = 0
        plus1list = []
        plus2 = 0
        plus2list = []

        #for i in range(len(points)):
        #for i in range(len(points) -1):
        for i in points[::-1]:
        #for i in points:
            

            # calculate i + 1 and i + 2
            # add value at i with value of next element
            # sum(points[i:(i+2)]) actually sums i + i's next element, not i + i's second element
            # this is because list slicing is exlusive of the number used to show the stopping point
            #plus1 = sum(points[i:(i+2)]) # this actually sums i + i's next element, not i + i's second element
            
            #print(points[i])
            #plus1 = sum(points[i:(i+2)])
            plus1 = points[i] + points[i+1]
            print(plus1)
            plus1list.append(plus1)
            #plus2 = points[i] + points[i-2] # list index out of range...
            # plus2 = sum(points[i:(i+3)]) # this is i + 2, but the notation is confusing. Don't use it.
            #plus2list.append(plus2)

            # now I think I need to compare current diff values (in the plus1list and plus2 list) to the threshold
            #if 

        print(plus1list)
        #print(plus2list)

#if __name__ == "__main__":

#    pass

print(minimum_points(2, [1, 2, 3]))
