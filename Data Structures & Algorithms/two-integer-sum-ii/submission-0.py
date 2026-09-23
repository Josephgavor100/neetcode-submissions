class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i, j = 0, len(nums) - 1

        while i < j:
            val = nums[i] + nums[j]
            if val == target:
                return [i+1, j+1]
            elif val < target:
                i+=1
            else:
                j-=1