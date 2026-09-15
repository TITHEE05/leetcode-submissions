class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #find length of nums
        n = len(nums)
        #make and array with same length every values is 1
        op = [1] * n

        #everything left of an index
        leftprod = 1
        for i in range(n):
            #place existing value of leftprod into op becuase we are using concept of previously calculated values
            op[i] = leftprod
            #finding value for next calculation: multiply left prod with next value in sequence in nums
            leftprod = leftprod * nums[i]

        #everything right of index
        rightprod = 1
        #pythons way of counting backwards start , end, how much to decrease by
        for i in range(n-1, -1, -1):
            #place into op the mul of existing righprod and op exisitig value
            op[i] = op[i] * rightprod
            #prepare rightprod for next round
            rightprod = rightprod * nums[i]

        
        return op

        