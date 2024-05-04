class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the array to simplify the boat allocation process
        people.sort()

        # Initialize two pointers, one at the beginning and one at the end of the array
        left = 0  # Pointer for the lightest person
        right = len(people) - 1  # Pointer for the heaviest person
        boats_count = 0  # Count of boats required

        # Iterate until both pointers meet or cross each other
        while left <= right:
            # If both the lightest and heaviest persons can fit in the same boat
            if people[left] + people[right] <= limit:
                boats_count += 1  # Allocate a boat
                left += 1  # Move to the next lightest person
                right -= 1  # Move to the next heaviest person
            # If only the heaviest person can fit in a boat
            elif people[right] <= limit:
                boats_count += 1  # Allocate a boat
                right -= 1  # Move to the next heaviest person

        return boats_count  # Return the total count of boats required
