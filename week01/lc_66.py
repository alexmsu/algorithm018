class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits: return [1]
        
        if digits[-1] == 9:
            return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1        
            return digits

        def plusOne(self, digits):
            """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        
        carry = 1
        for d in reversed(digits):
            new = d + carry
            res.append(new % 10)
            carry = new / 10
            
        if carry: res.append(1)
        
        return reversed(res)