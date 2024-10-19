class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map={}

        for i, nums in enumerate(nums):

            if nums in index_map and i-index_map[nums]<=k:
                return True
            index_map[nums]=i
        
        return False