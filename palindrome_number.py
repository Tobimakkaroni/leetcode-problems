class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        length = len(x)
        end = length - 1

        while end >= 0:
            for i in range(length):
                if x[i] == x[end]:
                    return True
                elif x[i] != x[end]:
                    return False
            end -= 1