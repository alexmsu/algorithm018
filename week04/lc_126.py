class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not beginWord or not endWord or not wordList: return [] 
        
        L = len(beginWord)
        hash = defaultdict(set)
        
        for word in wordList:
            for i in range(L):
                hash[word[:i] + '*' + word[i+1:]].add(word)
                
        q = deque([[beginWord]])
        visited = set()
        while q:
            n = len(q)
            res = []
            for _ in range(n):
                path = q.popleft()
                if path[-1] == endWord: res.append(path)
                visited.add(path[-1])
                for i in range(L):
                    tmp = path[-1][:i] + '*' + path[-1][i+1:]
                    for nei in hash[tmp]:
                        if nei not in visited:
                            q.append(path + [nei])
            if res: return res
                    
        return []