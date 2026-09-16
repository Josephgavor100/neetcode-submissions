class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, val in enumerate(nums):
            pair = target - val
            if pair not in dict:
                dict[val] = i
            else:
                return [dict[pair], i]
        return []
        