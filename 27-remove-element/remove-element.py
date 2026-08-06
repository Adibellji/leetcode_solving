class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        empty=[]
        for num in nums:
            if num!=val:
                empty.append(num)

        nums[:]=empty

        return len(nums)
        
        
        
        