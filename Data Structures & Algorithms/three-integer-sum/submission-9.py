class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        prev_i = nums[0] + 1
        for i in range(len(nums)-2):
            if nums[i] == prev_i:
                continue
            else:
                prev_i = nums[i]
            left, right = i+1, len(nums) - 1
            prev_left, prev_right = nums[i+1] + 1, nums[len(nums) - 1] + 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    result += [[nums[i], nums[left], nums[right]]]
                    prev_left = nums[left]
                    left += 1
                    while nums[left] == prev_left:
                        if left >= right:
                            break
                        left += 1
                    prev_left = nums[left]
                elif curr_sum < 0:
                    prev_left = nums[left]
                    left += 1
                    while nums[left] == prev_left:
                        if left >= right:
                            break
                        left += 1
                    prev_left = nums[left]
                elif curr_sum > 0:
                    prev_right = nums[right]
                    right -= 1
                    while nums[right] == prev_right:
                        if left >= right:
                            break
                        right -= 1
                    prev_right = nums[right]
        return result

        