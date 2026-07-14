class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=str(n)
        x=1
        y=0
        for i in range(len(a)):
            x*=int(a[i])

        for k in range(len(a)):
            y+=int(a[k])

        return x-y


        