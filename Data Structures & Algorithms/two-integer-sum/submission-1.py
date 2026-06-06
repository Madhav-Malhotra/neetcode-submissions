class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for i in range(len(nums)): 
            n = nums[i]
            comp = complement.get(n)
            
            if comp is not None:
                return [comp, i]
            else:
                complement[target - n] = i
        
        # Should never occur
        return [-1, -1]