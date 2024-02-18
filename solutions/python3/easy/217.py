class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for v in nums:
            if v in duplicates:
                return True
            else:
                duplicates[v] = None 
        return False