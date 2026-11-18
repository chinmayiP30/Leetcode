class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        XOR=0
        for i in nums:
            XOR=XOR^i
        return XOR
        