class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        # Calculate prefix products
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        prevSuffix = 1
        # Calculate suffix products and update ans array
        for i in range(n - 2, -1, -1):
            prevSuffix *= nums[i + 1]
            ans[i] *= prevSuffix

        return ans