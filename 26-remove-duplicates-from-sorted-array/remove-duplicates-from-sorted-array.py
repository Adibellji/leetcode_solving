class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        empty=[]
        
        for i in range(len(nums)):
            if nums[i] not in empty:
                empty.append(nums[i])

        nums[:]=empty

        return len(nums)
            

        




        
        
        