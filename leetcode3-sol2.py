class Solution(object):
    def lengthOfLongestSubstring(self, s:str) -> int:
        """
        :type s: str
        :rtype: int
        """
        left = 0
        best = 0
        seen_chars = set()

        for i, character in enumerate(s):
            while character in seen_chars:
                seen_chars.remove(s[left])
                left = left + 1
            
            seen_chars.add(character)
            best = max(best, len(seen_chars))
        
        return best



# Paper test
# abcdbcdbcd
# 0, a | seen = a; best = 1
# 1, b | seen = ab; best = 2
# 2, c | seen = abc; best = 3
# 3, d | seen = abcd; best = 4
# 4, b | seen = bcd
#         seen = cd
#         seen = cdb; best = 4
# 5, c | seen = db
#         seen = dbc; best = 4 

# Possible improvements:
# 1. Use type hints (e.g., def lengthOfLongestSubstring(self, s: str) -> int:) to make the code clearer and help static analysis tools.
# 2. Rename variables to be more descriptive (e.g., "right" instead of "i", "char" instead of "letter") to better communicate the sliding window idea.
# 3. Add a brief high-level comment above the loop explaining the sliding-window invariant (substring s[left:i+1] always has unique characters).
# 4. Extract the core logic into a standalone function (outside the class or as @staticmethod) to make it easier to unit test without instantiating Solution.
# 5. Replace "left = left + 1" with "left += 1" for conciseness, and consider using more Pythonic naming (e.g., "seen_chars").
# 6. Add a few unit tests or doctests demonstrating behavior on edge cases (empty string, all same characters, very long strings) to validate correctness.
