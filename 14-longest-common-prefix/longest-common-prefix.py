class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=sorted(strs)
        n=len(a)
        common=[]
        if a[0] and a[n-1] and a[0][0]==a[n-1][0]:
            b=min(len(a[0]),len(a[n-1]))

            for i in range(b):
                if a[0][i]!=a[n-1][i]:
                    break
                common.append(a[0][i])

            return "".join(common)

        else:
            return ""

        