def minimum_points(threshold, points):
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
    pass


if __name__ == "__main__":
    # write your debug code here
    pass
