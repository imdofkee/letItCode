class Solution(object):
    def isValid(self, s):
        stack = []

        dct = {'(': ')',
               '[': ']',
               '{': '}',
               '<': '>'}

        for i in s:                    
            if i in dct.keys():
                stack.append(i)
            elif i in dct.values():
                if not stack:
                    return False
                if dct[stack[-1]] != i:
                    return False
                stack.pop()

        return stack == []            