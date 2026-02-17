class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # List of sets
        indexedSets = []
        # Dict of set lengths by index
        indexedLengths = {}
        # Array of indices
        indexedBools = []

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        for i, letter in enumerate(s):
            # Declare a new set for the current index, and set its values
            indexedSets.append(set())
            indexedBools.append(True)
            indexedLengths[i] = 0

            # update all sets that have not seen duplicates in a loop
            for j in range(len(indexedBools)):
                # skip where duplicates are already detected, lengths are frozen
                if indexedBools[j] is False:
                    continue
                # store length before element addition
                lenBefore = indexedLengths[j]
                # try adding an element
                indexedSets[j].add(letter)
                # compare length after element addition
                if(len(indexedSets[j]) == lenBefore):
                    indexedBools[j] = False
                else:
                    indexedLengths[j] = len(indexedSets[j])
        
        return max(indexedLengths.values())