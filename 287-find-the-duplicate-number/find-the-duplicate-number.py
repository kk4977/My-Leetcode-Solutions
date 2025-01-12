class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i+1]
        #     else:
        #         i += 1
        # return i
        right  = 1
        left = 0
        while(right < len(nums)):
            if nums[left] == nums[right]:
                return nums[right]
            
            else:
                right += 1
                left += 1
        return -1 

        