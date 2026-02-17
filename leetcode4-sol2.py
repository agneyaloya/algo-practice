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

        combinedArray = []

        j = k = 0

        for i in range(totalLen):
            # if both remaining, compare and add
            if j < len1 and k < len2:
                if (nums1[j] < nums2[k]):
                    nextNum = nums1[j]
                    j += 1
                else: 
                    nextNum = nums2[k]
                    k += 1
                combinedArray.append(nextNum)
            # if num1 over, assign remaining num2
            elif j >= len1 and k < len2:
                combinedArray.extend(nums2[k:])
                break
            # if num2 over, assign remaining num1
            elif j < len1 and k >= len2:
                combinedArray.extend(nums1[j:])
                break
            # if both over, end loop
            else:
                break

        
        print(combinedArray)
        if (totalLen % 2 == 0):
            print('averaging ...')
            middle = totalLen // 2 - 1
            return float(combinedArray[middle] + combinedArray[middle + 1])/2
        else:
            middle = totalLen // 2
            return combinedArray[middle]
            
            
            