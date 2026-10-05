class Solution:
    # is Case insensitive, and only accounts for alphanumeric characters

    def isPalindrome(self, s: str) -> bool:
        string = ''.join(filter(str.isalnum,s))
        string=string.lower()
        string=string.strip()
        # We will use a two-pointer here.
        # One tracks the first char, moving forward
        # Second pointer tracks the last char, moving backward.
        length = len(string)
        i,j = 0,length-1
        while i<len(string):
            # if string check aborts, return False
            if string[i] != string[j]:
                return False
            i+=1
            j-=1
        # If the string check is finished
        # without an error,  return True
        return True