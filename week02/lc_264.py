class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        primes = [2, 3, 5]
        index = [0, 0, 0]
        while n > 1:
            n -= 1
            candidates = [p * ugly[index[i]] for i, p in enumerate(primes)]
            target = min(candidates)
            ugly.append(target)
            for i in range(len(index)):
                if candidates[i] == target: index[i] += 1
            
        return ugly[-1]