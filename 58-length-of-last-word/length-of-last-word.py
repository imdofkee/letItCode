class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_s = s.strip()
        counter = 0
        if len(new_s) == 1:
            return 1
        for i in range(len(new_s)-1, -1, -1):
            if new_s[i] == ' ':
                return counter
            else: 
                counter+=1
        return counter
