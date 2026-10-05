class Solution:
    # 0 <= strs.length < 100
    # 0 <= strs[i].length < 200
    # strs[i] contains any possible characters out of
    # 256 valid ASCII characters.
    # strs = ["hi", "hello", "* &%.", "SMT"]

    def encode(self, strs: List[str]) -> str:
        # we use ord to retrieve ascii
        # How are we going to iterate through the list?
        # How are we going to delimit the str elements?
        if len(strs) == 0:
            return chr(1)
        # --> Add a delimiter character at the end of our string
        # That never appears in our original string
        ascii_set = set(i for i in range(256))
        for str in strs:
            for char in str:
                if ord(char) in ascii_set:
                    ascii_set.remove(ord(char))
        #now we can select any delimiter except for the "" from the ascii list
        delimiter = chr(list(ascii_set)[-1])
        res = delimiter.join(strs)
        res = res+delimiter
        return res

    def decode(self, s: str) -> List[str]:
        delimiter = s[-1]
        if delimiter == chr(1):
            return []
        res = []
        buffer = ""
        for char in s:
            if char == delimiter:
                res.append(buffer)
                buffer = ""
                continue
            buffer = buffer+char
        return res
