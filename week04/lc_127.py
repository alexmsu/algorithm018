class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """        
        hash = defaultdict(list)
        L = len(beginWord)
        
        for word in wordList:
            for i in range(L):
                hash[word[:i] + "*" + word[i+1:]].append(word)
        
        q = deque([beginWord])
        
        visited = set()
        level = 1
        
        while q:
            level += 1
            n = len(q)
            while n > 0:
                n -= 1
                current_word = q.popleft()
                for i in range(L):
                    intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                    for word in hash[intermediate_word]:
                        if word == endWord: return level
                        if word not in visited:
                            visited.add(word)
                            q.append(word)
                            
        return 0