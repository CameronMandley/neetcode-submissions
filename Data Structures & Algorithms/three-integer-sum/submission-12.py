class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        prev_num = float("inf")
        results = []

        for i in range(len(nums) - 2):
            if prev_num == nums[i]:
                i += 1
                continue
            prev_num = nums[i]
            left = i+1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum < 0:
                    left += 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    results += [[nums[i], nums[left], nums[right]]]
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return results



        