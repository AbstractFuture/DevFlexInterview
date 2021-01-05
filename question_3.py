def minimum_points(threshold, points):
    min_point = points[0]
    current_sum = 0
    # if sum of points between points[0] and current iterable is greater than threshold
    # store and return the number of elements summed as the answer
    # since it is possible to solve i + 1 or i + 2, i can use modulus to determine min points


    # if there is only a single point and it is smaller than the threshold
    # immediately return that student must solve all (1) questions
    if (len(points) == 1): #and (threshold > points[0]):
        return 1
    
    # if points array has more than one element in it
    elif (len(points) == 2):
        return 2

    else: # if points array has 3 or more elements in it
        for i in points:
            current_sum = current_sum + i
            print("Current sum is: ", current_sum)
        


    #for i in range(len(points)):
    #    print(points[i])
    #    print(points[i] + 1)

    #return min_point

# a. They must always solve the first problem, index i = 0
 
# b. After solving the i-th problem, they have a choice: solve the next problem (i + 1) or skip ahead and work the (i + 2)
#  problem.

# does this mean I need to create a sum of all permutations of the points based on b's criteria?
# I need to loop through the points array and calculate if threshold has been reached
 
# c. Students must keep solving problems until the difference between the maximum points and the minimum points questions
#  solved so far meets or exceeds a specified threshold
 
# d. If a student cannot meet or exceed the threshold, they must work through all the problems. 
 
 
# minimum_points(2, [1, 2, 3]) -> 2
# Explanation: if a student solves points[0] = 1, points[2] = 3, the difference between the minimum and the maximum points
#  solved is 3 - 1 = 2. This meets the threshold, so the student must solve at least 2 problems. Return 2. 
 
# minimum_points(4, [1, 2, 3, 5, 8]) -> 3
# If the threshold is 4, again it takes 3 problems solving problems 1, 3 and 4 where points[3] - points[0] = 5 - 1 = 1.
#  This meets the threshold, so the student must solve at least 3 problems. Return 3
    pass


if __name__ == "__main__":

    pass

print(minimum_points(2, [1, 2, 3]))
