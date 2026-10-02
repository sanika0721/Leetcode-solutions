class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        for ch in t:
            if count.get(ch,0)==0:
                return False
            count[ch]-=1
        return True