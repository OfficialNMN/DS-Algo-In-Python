class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans=[]
        temp=[]
        def subset(ind):
            ans.append(temp[:])
            for i in range(ind,len(nums)):
                # to remove duplicates from answer
                if (i!=ind and nums[i]==nums[i-1]):
                    continue
                # add the nums[i]
                temp.append(nums[i])
                # recursive call for next index
                subset(i+1)
                # popping the last index
                temp.pop()
        subset(0)
        return ans