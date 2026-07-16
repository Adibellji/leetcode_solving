class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        for a in operations:
            if a=="+":
                if len(score)>=2:
                    score.append(score[-1]+score[-2])
                
            elif a=="D":
                if len(score)>=1:
                    score.append(2*score[-1])

            elif a=="C":
                if len(score)>=1:
                    score.pop()

            else:
                score.append(int(a))

        return sum(score)

                

                

            

            


        