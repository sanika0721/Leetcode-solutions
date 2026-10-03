class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        sorted_nums=sorted(freq,key=freq.get,reverse=True)
        return sorted_nums[:k]