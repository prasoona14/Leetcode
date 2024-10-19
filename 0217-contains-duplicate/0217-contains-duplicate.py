class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        index_map={}
        for i,nums in enumerate(nums):
            if nums in index_map:
                return True
            index_map[nums]=i
        return False

        