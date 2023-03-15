class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        l = len(croakOfFrogs)
        count = 0
        ans = 0
        d = {'c':0, 'r':0, 'o':0, 'a':0, 'k':0}
        
        def validate():
            for i in d:
                for j in d:
                    if i==j:
                        continue
                    else:
                        if d[i] < d[j]:
                            return 0
            return 1
        
        for i in croakOfFrogs:
            if i == 'c':
                count+=1
                d[i]+=1
            elif i == 'k':
                ans = max(ans, count)
                count -= 1
                d[i]+=1
            else:
                d[i]+=1
            if not validate:
                return -1
        
        if count!=0:
            return -1
        
        
        return ans
            
                
            
            
        