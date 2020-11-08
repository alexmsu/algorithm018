class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(n, k, start, l, res):
            if k == 0:
                res.append(l[:])
                return
            for i in range(start, n + 1):
                l.append(i)
                helper(n, k - 1, i + 1 , l, res)
                l.pop()
        
        res = []
        helper(n, k, 1, [], res)
        return res