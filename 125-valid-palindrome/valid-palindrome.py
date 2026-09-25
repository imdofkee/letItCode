class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ''.join(ch.lower() for ch in s if ch.isalnum())
        return new_s == new_s[::-1]
