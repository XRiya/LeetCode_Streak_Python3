class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = sum(range(1, n + 1))  # Calculate the total sum of all integers from 1 to n
        sum1 = 0
        for i in range(1, n + 1):  # Iterate through each integer from 1 to n
            # Calculate the sum of the integers before the current integer
            if sum1 == total_sum - sum1 - i:
                return i  # Return the current integer if it is a pivot integer
            sum1 += i  # Update the sum1 for the next iteration
        return -1  # Return -1 if there is no pivot integer
