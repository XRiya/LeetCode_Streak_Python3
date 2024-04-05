class Solution:
    def makeGood(self, s: str) -> str:
        end_position = 0  # Represents the end position of the modified string
        char_array = list(s)  # Convert the string to a list of characters
        
        # Loop through each character in the string
        for current_position in range(len(s)):
            # Check if the current character can be removed
            if end_position > 0 and abs(ord(char_array[current_position]) - ord(char_array[end_position - 1])) == 32:
                end_position -= 1  # Decrement the end position if the current character can be removed
            else:
                # Otherwise, keep the current character and increment the end position
                char_array[end_position] = char_array[current_position]
                end_position += 1
        
        # Convert the modified character list to a string and return only the valid portion
        return ''.join(char_array[:end_position])
