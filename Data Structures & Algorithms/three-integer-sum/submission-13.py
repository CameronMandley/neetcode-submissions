class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        prev_num = float("inf")
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if prev_num == nums[i]:

                continue
            prev_num = nums[i]

            left, right = i+1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    results += [[nums[i], nums[left], nums[right]]]
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return results
                


        