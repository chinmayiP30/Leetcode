class Solution:
    def sortedSquares(self, nums):
        a = []
        b = []

        for i in range(len(nums)):
            if nums[i] >= 0:
                b.append(nums[i])
            else:
                a.append(nums[i])

        for i in range(len(a)):
            a[i] = a[i] * a[i]
        a.reverse()

        for i in range(len(b)):
            b[i] = b[i] * b[i]

        i = 0
        j = 0
        m = len(a)
        n = len(b)

        res = [0] * (m + n)
        k = 0

        while i < m and j < n:
            if a[i] <= b[j]:
                res[k] = a[i]
                i += 1
            else:
                res[k] = b[j]
                j += 1
            k += 1

        while i < m:
            res[k] = a[i]
            i += 1
            k += 1

        while j < n:
            res[k] = b[j]
            j += 1
            k += 1

        return res