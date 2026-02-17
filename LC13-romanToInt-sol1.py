class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        # 1, 5, 10, 50, 100, 500, 1000

        lookup = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # lookup2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        corrections = {'IV': -2, 'IX': -2, 'XL': -20, 'XC': -20, 'CD': -200, 'CM': -200}

        sum = 0
        for i in range(len(s)):
            sum += lookup[s[i]]
            if i >= 1:
                if s[i-1:i+1] in corrections:
                    # print('subtracting ...')
                    sum += corrections[s[i-1:i+1]]
            # print(s[i])
            # print(sum)
        # print(sum)

        # for key, value in corrections.items():
        #     sum += s.count(key) * value
    
        return sum

        