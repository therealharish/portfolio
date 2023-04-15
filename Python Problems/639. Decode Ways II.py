class Solution:
    def numDecodings(self, s: str) -> int:
        
        d = {
            '1*': 18,
            '2*': 15,
            '*1': 9,
            '*2': 9,
            '*3': 9,
            '*4': 9,
            '*5': 9,
            '*6': 9,
            '*7': 9,
            '*8': 9,
            '*9': 9,
            '**': 96,
        }
        
        def createPairofTwo(index, s):
            ans = []
            i = index
            while(i < len(s)):
                ans.append(s[i:i+2])
                i+=2
            return ans

        pair1 = createPairofTwo(0, s)
        pair2 = [s[0]] + createPairofTwo(1, s)
        print(pair1, pair2)

        count = 1
        for i in pair1:
            if len(i) == 1:
                count *=1
            if i in d:
                count *= d[i]
            elif int(i) <= 26:
                count *= 1
            else:
                count *= 2
        
        count2 = 0
        for i in pair2:
            if i in d:
                continue
            elif int(i) >= 10 and int(i) <= 26:
                count2 += 1
            else:
                continue

        return count + count2