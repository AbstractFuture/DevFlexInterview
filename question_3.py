def minimum_points(threshold, points):

    current_sum = 0
    # if sum of points between points[0] and current iterable is greater than threshold
    # store and return the number of elements summed as the answer
    # since it is possible to solve i + 1 or i + 2, i can use modulus to determine min points


    # if there is only a single point
    # immediately return that student must solve all (1) questions
    if (len(points) == 1): 
        return 1
    
    # if points array has more than one element in it
    elif (len(points) == 2):
        return 2

    else: # if points array has 3 or more elements in it
        # print(points[1:])
        # initialize variable to keep track of loop count
        loop_count = 0
        # initialize variable to keep track of current sum
        # compare current sum to threshold
        current_sum = 0

        for i in points:
            
            loop_count += 1
            current_sum += i

            #print("Current sum is: ", current_sum)
            #print("Threshold is: ", threshold, ". Continuing another loop")
            
            # if current sum is greater than threshold
            # and if num of elements summed are odd
            if (current_sum > threshold):# and (not(loop_count % 2 == 0)):
                print("Current sum is: ", current_sum, ". Threshold reached.")
                return loop_count #-1
                # need to determine min points now
                # count elements between points[0] and i
            #elif (current_sum > threshold):
            #    print("Current sum is: ", current_sum, ". Threshold reached")
            #    return loop_count
            #else:
            #    pass

            print("Current sum is: ", current_sum)
            print("Threshold is: ", threshold, ". Continuing another loop")
        
# a. They must always solve the first problem, index i = 0
 
# b. After solving the i-th problem, they have a choice: solve the next problem (i + 1) or skip ahead and work the (i + 2)
#  problem.

 
# c. Students must keep solving problems until the difference between the maximum points and the minimum points questions
#  solved so far meets or exceeds a specified threshold
 
# d. If a student cannot meet or exceed the threshold, they must work through all the problems. 
 
 
# minimum_points(2, [1, 2, 3]) -> 2
# Explanation: if a student solves points[0] = 1, points[2] = 3, the difference between the minimum and the maximum points
#  solved is 3 - 1 = 2. This meets the threshold, so the student must solve at least 2 problems. Return 2. 
 
# minimum_points(4, [1, 2, 3, 5, 8]) -> 3
# If the threshold is 4, again it takes 3 problems solving problems 1, 3 and 4 where points[3] - points[0] = 5 - 1 = 1.
#  This meets the threshold, so the student must solve at least 3 problems. Return 3


#if __name__ == "__main__":

#    pass

print(minimum_points(12, [1, 2, 3, 5, 8, 13, 14, 15, 18]))
