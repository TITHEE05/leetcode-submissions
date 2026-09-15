class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #attempt 2 using conters
        op = []
        count = Counter(nums)
        most_freq = count.most_common(k)
        for f in most_freq:
            op.append(f[0])

        return op

        
        

        