class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we will sort this by storing numbers in a list that has the count of numbers as indices.

        #First we count the occurences:
        numDict = defaultdict(int)
        for i in nums:
            if i in numDict:
                numDict[i] += 1
            else:
                numDict[i] = 1
        
        #Define the list:
        countDict = defaultdict(list)
        #count the occurrences, and store it accordingly in the countList
        for number in numDict:
            count = numDict[number]
            if number in countDict[count]:
                continue
            else:
                countDict[count].append(number)
        #Now we have the count:numbers relationship. lets return the top k numbers
        res=[]
        i=len(nums)
        while i>=0:
            if i not in countDict:
                i=i-1
                continue
            else:
                if len(res)==k:
                    break
                else:
                    for j in countDict[i]:
                        res.append(j)
                i = i-1
            
        return res
                    
                
