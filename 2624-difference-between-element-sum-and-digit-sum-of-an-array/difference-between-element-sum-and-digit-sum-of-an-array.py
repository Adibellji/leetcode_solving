class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum=0
        add=0
        
        for i in range(len(nums)):
            sum+=nums[i]

        for num in nums:
            for digit in str(num):
                add+=int(digit)

        return abs(sum-add)



