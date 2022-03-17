class Solution(object):
    def removeElement(self, nums, val):
        nums2 = []
        for i in nums:
            if i != val:
                nums2.append(i)
        print(nums2)
a = Solution()
a.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
