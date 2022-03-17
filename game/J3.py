inpu = input()
arr = []
arr2 = []
while not int(inpu) == 99999:
    arr.append(inpu)
    inpu = input()
for i in range(len(arr)):
    if (int(arr[i][0]) + int(arr[i][1])) % 2 != 0:
        arr2.append("left")
    elif (int(arr[i][0]) + int(arr[i][1])) % 2 == 0 and (int(arr[i][0]) + int(arr[i][1])) != 0:
        arr2.append("right")
    else:
        arr2.append(arr2[i - 1])
for j in range(len(arr2)):
    print(arr2[j] + " " +  arr[j][2] + arr[j][3] + arr[j][4])