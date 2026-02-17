class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        lt = len(num)

        # print(num[0])

        if lt == 1:
            return True

        for i in range(lt // 2):
            if(num[i] != num[lt - 1 - i]):
                return False
        
        return True