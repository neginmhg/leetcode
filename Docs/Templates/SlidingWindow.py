class Solution:
    def slidingWindow(self, nums, k):
        # 1. L to 0
        l=0
            
        # 2. frequency if window of L and R
        countEachChar={}

        maxFrequency=0
        res=0

        # 3. for r in range(len(nums))
        for r in range(len(nums)):
            # 4. L+=1 based on Logic

            countEachChar[s[r]]=countEachChar.get(s[r],0) +1
            maxFrequency=max(maxFrequency, countEachChar[s[r]])
            if((r-l+1)- maxFrequency > k):  
                countEachChar[s[l]]-=1   
                l+=1
            res=max(r-l+1, res)
        return res