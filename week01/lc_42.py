class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        
        stack = [(100001, -1)]
        res = 0
        
        i = 0
        while i < len(height):
            if height[i] != 0:
                stack.append((height[i], i))
                break
            i += 1
                        
        i += 1
        while i < len(height):
            #print(stack)
            if height[i] == stack[-1][0]:
                stack[-1] = (height[i], i)
                i += 1
                continue
            elif height[i] > stack[-1][0]:
                low = stack.pop()
                while len(stack) > 1:
                    if height[i] >= stack[-1][0]:
                        new_low = stack.pop()
                        res += (new_low[0] - low[0]) * (i - new_low[1] - 1)
                        low = new_low
                    else:
                        res += (height[i] - low[0]) * (i - stack[-1][1] - 1)
                        break
            stack.append((height[i], i))
            i += 1
        
        return res