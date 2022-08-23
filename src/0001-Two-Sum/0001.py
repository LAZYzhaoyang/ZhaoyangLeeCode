class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1=0
        for i in range(len(nums)-1):
            num1 = nums[i]
            j = i+1
            while j <=len(nums)-1:
                num2 = nums[j]
                if num1+num2==target:
                    return [i,j]
                j+=1
