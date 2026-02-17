class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lt = len(s)
        loc = [0,0]
        vec = [1,0]

        # if numRows == 1:
        #     cols = lt + 1
        # else:
        #     cols = (lt // (numRows + numRows - 2)) * (numRows - 1) + 2
        #     cols = max(cols, numRows)
        # print(cols)
        # zz = [[""]*cols for i in range(numRows)]

        # Init one list row per numRows, some will go to waste
        zz = [[""] for i in range(numRows)]
        
        for i in range(lt):
            zz[loc[0]] += s[i]
            # if only one row, vec always points right
            if numRows == 1:
                vec = [0, 1]
            # bottom collision, change vec to top right
            elif (loc[0] == numRows - 1) and (vec[0] == 1):
                vec = [-1, 1]
            # top collision, change vec to down
            elif (loc[0] == 0) and (vec[0] == -1):
                vec = [1, 0]
            loc[0] += vec[0]
            loc[1] += vec[1]
        
        cols = len(zz[0])
        k = -1
        res = ""
        for i in range(numRows):
            for j in range(len(zz[i])):
                if zz[i][j] != "":
                    k += 1
                if k < lt:
                    res += zz[i][j]
                else:
                    break
        
        return res
                



