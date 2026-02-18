class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # get total length
        len1 = len(nums1)
        len2 = len(nums2)
        totalLen = len1 + len2
        isEven = (totalLen % 2 == 0)
        counter = 0
        # Track indices for each array and the median
        k1 = 0
        k2 = 0
        middle = totalLen // 2
        # vals = [nums1[0] if nums1 else 0, nums2[0] if nums2 else 0]
        vals = []
        # print(vals)

        # totalLen is 0
        if totalLen == 0:
            return 0
        # totalLen is 1
        if middle == 0: 
            return sum(vals)

        for i in range(totalLen):
            print("i")
            print(i)
            print(vals)
            workWith = ""
            
            # Both lists over - handled by for loop
            # First list finished
            if k1 >= len1 and k2 < len2:
                workWith = "l2-only"
                nextNum = nums2[k2]
                k2 += 1
            # Second list finished
            elif k2 >= len2 and k1 < len1:
                workWith = "l1-only"
                nextNum = nums1[k1]
                k1 += 1
            # Both lists remaining, compare
            else:
                workWith = "both"
                if nums1[k1] > nums2[k2]:
                    nextNum = nums2[k2]
                    k2 += 1
                elif nums1[k1] <= nums2[k2]:
                    nextNum = nums1[k1]
                    k1 += 1
        
            vals.append(nextNum)
            if len(vals) > 2:
                vals.pop(0)
            counter += 1

            print(counter == middle + 1)
            if (counter == middle + 1) and isEven:
                return sum(vals)/2
            elif (counter == middle + 1) and not isEven:
                return vals[0]
            

            
            
        