class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        
        sp = [[0 for i in range(len(words))] for j in range(len(words))]
        
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] == words[j]:
                    continue
                curr = words[i]
                for k in range(1, len(words[i])):
                    if words[j].startswith(words[i][k:]):
                        sp[i][j] = len(curr) - k
        
        