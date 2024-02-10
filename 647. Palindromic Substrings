class Solution:
    def countSubstrings(self, s: str) -> int:
        # total number of palindromic substrings
        total = 0
        n = len(s)

        for mid in range(n):
            total += 1  # as each single character is a palindrome

            # odd palindrome substrings keeping s[mid] as center of
            # palindromic substring
            left, right = mid-1, mid+1

            while left >=0 and right < n and s[left] == s[right]:
                total += 1
                left -= 1
                right += 1
            
            # even palindrome substrings keeping s[mid] and s[mid+1] as
            # center of palindromic substring
            left, right = mid, mid+1

            while left >=0 and right < n and s[left] == s[right]:
                total += 1
                left -= 1
                right += 1
        
        return total
