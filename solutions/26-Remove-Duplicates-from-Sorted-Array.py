class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        pointer = 1

        while pointer < len(nums):
            # elements are the same
            if nums[pointer] == nums[pointer - 1]:
                pointer += 1
            else:
                nums[count] = nums[pointer]
                count += 1
                pointer += 1
        
        return count
