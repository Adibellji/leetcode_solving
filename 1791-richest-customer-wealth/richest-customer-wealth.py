class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max=0
        for wealth in accounts:
            current=sum(wealth)

            if current>max:
                max=current

        return max
        