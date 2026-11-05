class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {} # {complement: index}
        for i, num in enumerate(nums):
            complement = target - num
            if num in complement_map:
                return [complement_map[num], i]
            complement_map[complement] = i
        return []
