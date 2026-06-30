class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        i = 0
        j = 1
        k = 1
        n = len(nums)

        while j < n:
            if nums[j - 1] == nums[j]:
                j += 1
                continue
            else:
                nums[i + 1] = nums[j]
                j += 1
                i += 1
                k += 1

        return k