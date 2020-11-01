class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = defaultdict(list)
        
        for s in strs:
            hash[''.join(sorted(s))].append(s)
        
        return hash.values()