class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(0, len(nums)) :
            complement = target - nums[i]
            hash[i] = nums[i]
            if complement  in hash.values() and nums.index(complement) != i :
                return [nums.index(complement), i]