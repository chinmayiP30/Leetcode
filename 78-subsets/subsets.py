class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        ans=[]
        for num in range(0,2**n):
            sub=[]
            for i in range(0,n):
                if num &(1<<i):
                    sub.append(nums[i])
            ans.append(sub)
        return ans    
        