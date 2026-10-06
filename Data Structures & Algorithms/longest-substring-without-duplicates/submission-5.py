class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # **Constraints:**
        # - `0 <= s.length <= 50,000`
        # - `s` may consist of printable ASCII characters.

        # Initial thought:
        # Use ord()
        # Use a hashset to store chars

        # Edge Cases:
        # str is empty

        charset = set()
        left = 0
        length, max_length = 0, 0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                length-=1
                left+=1
            charset.add(s[right])
            length+=1
            max_length = max(length, max_length)
        return max_length






