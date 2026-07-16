class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        countsin=0
        countdou=0

        nums.sort()
        for i in range(len(nums)):
            if nums[i]<10:
                countsin+=nums[i]
            else:
                countdou+=nums[i]

        if countsin>countdou:
            return True
        elif countsin<countdou:
            return True
            

        return False
            
        