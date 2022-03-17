class Solution:
    def SumGame(self, num, s1, s2):
        s12 = s1.split(" ")
        s22 = s2.split(" ")
        arr1 = []
        arr2 = []
        new = []
        print(s12[1])
        for i in range(len(s12)):
            s12[i] = int(s12[i])
            if i == 0:
                arr1.append(s12[i])
            else:
                print("Hi")
                print(i)
                print(s22[i])
                print(s22[i - 1])
                arr1.append(s12[i] + s12[i - 1])
        for i in range(len(s22)):
            s22[i] = int(s22[i])
            if i == 0:
                arr2.append(s22[i])
            else:
                arr2.append(s22[i] + s22[i - 1])
        print(arr1)
        print(arr2)
        for i in range(len(arr1)):
            if arr1[i] == arr2[i]:
                new.append(arr1[i])
        if len(new) == 0:
            return 0
        else:
            return max(new)
a = Solution()
print(a.SumGame(4, "1 2 3 4", "1 3 2 4"))