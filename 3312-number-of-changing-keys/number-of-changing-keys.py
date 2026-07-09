class Solution:
    def countKeyChanges(self, s: str) -> int:
        count=0
        for i in range(len(s)-1):
            if s[i].lower()==s[i+1]:
                continue
            if s[i].upper()!=s[i+1]: 
                count+=1

        

        return count
            


        