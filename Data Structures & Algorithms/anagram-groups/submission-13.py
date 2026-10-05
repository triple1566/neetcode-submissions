class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first define a dictionary as {indexed keys : list of strings}
        anaHash = defaultdict(list)

        #second, go through the list of strings to map them into an array of indexes based on letter count
        for string in strs:
            countList = [0] * 26 #number of alphabets
            for char in string:
                #turn each char's ascii code into list index
                #then, add count to the count list
                countList[ord(char)-ord("a")] += 1
            #now that we have an index key for our current string, we add it in the hashmap
            anaHash[tuple(countList)].append(string)
        
        #after looping for all strings in the given list, we have a tructure of anaHash = {index key : [word1, word2...]...}
        
        #Now, we will convert our structure into a list.
        res = []
        for l in anaHash:
            res.append(anaHash[l])
        return res


