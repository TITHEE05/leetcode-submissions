class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #logic: sort the words you are picking up and make a new key value entry for them in a new dict next time that word appears add it to the list
        d = {}
        for s in strs:
            #since sorted function converts a string into a list of sorted elements we need to convert it back to a string for that we use join with "" as the seperator becuase there is nothing seperating the values
            new = "".join(sorted(s))
            if new in d:
                d[new].append(s)
            else:
                d[new] = [s]
        return d.values()
