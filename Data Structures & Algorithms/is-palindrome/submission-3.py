class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(filter(str.isalnum, s)).lower()
        print(cleaned_s)

        start_index = 0
        end_index = len(cleaned_s) - 1

        while start_index < end_index:
            if cleaned_s[start_index] != cleaned_s[end_index]:
                return False
            start_index += 1
            end_index -= 1
        
        return True