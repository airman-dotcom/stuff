class Solution:
    def AbsolutelyAcidic(self, num, nums):
        nums = nums.split(" ")
        dict = {}
        dict2 = {}
        max_fre_val = 0
        max_fre_num = 0
        for i in range(len(nums)):
            nums[i] = int(nums[i])   
        for j in range(min(nums), max(nums) + 1):
            if j in nums:
                dict[j] = nums.count(j)
        for i in range(1, len(dict) + 1):
            if len(list(dict.values())) != 0:
                max_fre_val = max(dict.values())
                arr = list(dict.values())
                if arr.count(max_fre_val) == 2:
                    max_fre_num = []
                    max_fre_num.append(list(dict.keys())[arr.index(max_fre_val)])
                    max_fre_num.append(list(dict.keys())[arr.index(max_fre_val)] + 1)
                    dict.pop(max_fre_num[0])
                    dict.pop(max_fre_num[1])
                else:
                    max_fre_num = list(dict.keys())[arr.index(max_fre_val)]
                    dict.pop(max_fre_num)
                dict2[i] = max_fre_num
        for j in range(min(nums), max(nums) + 1):
            if j in nums:
                dict[j] = nums.count(j)
        if len(list(dict2.values())[1]) == 2:
            print(max(abs(list(dict2.values())[0] - list(dict2.values())[1][0]), abs(list(dict2.values())[0] - list(dict2.values())[1][1])))

        
        
        
a = Solution()
a.AbsolutelyAcidic(4, "10 6 1 8")