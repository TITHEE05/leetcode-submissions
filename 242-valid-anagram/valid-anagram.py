class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #check if no. of letters in both the strings are the same
        if len(s) == len(t):
            #making a dict
            d = {}
            for x in s:
                #check if value present in dict or not: if present add 1 if not make an entry into dict
                if x in d:
                    d[x] += 1
                else:
                    d[x] = 1
   
            for x in t:
                #check if x exists in dict or not: if exists -1 from value if not exists return false ie the two strings are not an anagram
                if x in d:
                    d[x] -= 1
                else:
                    return False
            
            #check if all values of the dict are 0 if yes then anagram is present
            for v in d.values():
                if v == 0:
                    pass
                else:
                    return False
            return True

        else:
            return False