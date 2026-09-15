class Solution(object):
    #attempt - 1
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #sort the array
        nums.sort()
        #check if adjacents are equal
        for i in range(len(nums) - 1):
            if nums[i]==nums[i+1]:
                return True
        return False
        