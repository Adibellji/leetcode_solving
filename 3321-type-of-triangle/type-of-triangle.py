class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if (nums[0]+nums[1]<=nums[2]) or (nums[1]+nums[2]<=nums[0]) or (nums[0]+nums[2]<=nums[1]):
            return "none"

        
        check=len(set(nums))

        if check==1:
            return "equilateral"
        if check==2:
            return "isosceles"
        if check==3:
            return "scalene"
        
        