class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #attempt 2: dictionary
        #create empty dictionary
        d = {}
        #enumerate function helps return index as well as value from a list
        for i, num in enumerate(nums):
            #find complement 
            comp = target - num
            if comp in d:
                return [d[comp], i] #d[comp] returns index since in output we wnat index from the original array
            else:
                #i holds the index of the value from the original array
                d[num] = i
        
        return False
        