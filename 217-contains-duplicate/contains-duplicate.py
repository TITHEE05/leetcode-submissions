class Solution(object):
    #attempt 2 through sets
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #sets have O(1) lookup time
        #start with an empty set 
        match = set()
        #then iterate over every value
        for num in nums:
            if num in match:
                return True
            else:
                match.add(num)
        
        return False
        