class Solution(object):
    def romanToInt(self, s):
        dct = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        spec_dct = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IV": 4,
            "IX": 9,
        }

        ans = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in spec_dct:
                ans += spec_dct[s[i:i + 2]]
                i += 2
            else:
                ans += dct[s[i]]
                i += 1

        return ans