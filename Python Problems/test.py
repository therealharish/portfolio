class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = s1.split(" ")
        l2 = s2.split(" ")
        d1 = Counter(l1)
        d2 = Counter(l2)
        ans = []
        for i in l1:
            if i not in d2 and d1[i] == 1:
                ans.append(i)
        for i in l2:
            if i not in d1 and d2[i] == 1:
                ans.append(i)
        return ans
        