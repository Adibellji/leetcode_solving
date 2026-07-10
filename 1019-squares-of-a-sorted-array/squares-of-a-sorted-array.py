class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square=[]
        
        for i in range(len(nums)):
            square.append(nums[i]*nums[i])

        square.sort()

        return square

        