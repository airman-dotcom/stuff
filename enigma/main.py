

print("First Let's define some metadata")
rotor1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
rotor2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
rotor3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
rotations1 = 0
rotations2 = 0
reflector = {"A": "F", "B": "V", "C": "P", "D": "J", "E": "I", "G": "O", "H": "Y", "K": "R", "L": "Z", "M": "X", "N": "W", "T": "Q", "S": "U"}
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print("Rotor Rotations \n")


def find_letter(x, arr, num):
    if arr[0] == letters[x]:
        if num == 1:
            global rotor1
        elif num == 2:
            global rotor2
            rotor2 = arr
        else:
            global rotor3
            rotor3 = arr
        return
        
    else:
        arr.append(arr[0])
        arr = arr[1::]
        find_letter(x, arr, num)



start = int(input("Rotor 1: ")) - 1
find_letter(start, rotor1, 1)
start = int(input("Rotor 2: ")) - 1
find_letter(start, rotor2, 2)
start = int(input("Rotor 3: ")) - 1
find_letter(start, rotor3, 3)



print("PlugBoard Connections \n")
dict = {}
num = int(input("How many plugboards do you want to connect? (0-20) "))
if num > 0:
    print("Syntax: Letter1 Letter2")
for i in range(num):
    a = input().split(" ")
    a[0] = a[0].upper()
    a[1] = a[1].upper()

    if (a[0] in list(dict.keys()) or a[0] in list(dict.values())) or (a[1] in list(dict.keys()) or a[1] in list(dict.values())):
        print("One of letters is already in use")
        pass
    else:
        dict[a[0]] = a[1]
print("Start pressing letters!\n")
def crypt():
    global rotations1
    global rotations2
    global rotor3
    global rotor1
    global rotor2
    global letters
    global dict
    rotations1 += 1
    rotor1.append(rotor1[0])
    rotor1 = rotor1[1::]

    if rotations1 == 26:
        rotations2 += 1
        rotor2.append(rotor2[0])
        rotor2 = rotor2[1::]
        rotations1 = 0

    if rotations2 == 26:
        rotations2 = 0
        rotor3.append(rotor3[0])
        rotor3 = rotor3[1::]
    print(rotor1)
    letter = input()
    letter = letter.upper()
    if letter in list(dict.keys()):
        letter = dict[letter]
    if letter in list(dict.values()):
        letter = list(dict.keys())[(list(dict.values())).index(letter)]
    letter = rotor1[letters.index(letter)]
    letter = rotor2[rotor1.index(letter)]
    letter = rotor3[rotor2.index(letter)]
    print(list(reflector.keys()))
    if letter in list(reflector.keys()):
        i = list(reflector.keys()).index(letter)
        letter = reflector[letter]
    else:
        i = list(reflector.values()).index(letter)
        letter = list(reflector.values())[list(reflector.keys()).index(letter)]
    letter = rotor3[i]
    letter = rotor2[rotor3.index(letter)]
    letter = rotor1[rotor2.index(letter)]
    if letter in list(dict.keys()):
        letter = dict[letter]
    elif letter in list(dict.values()):
        letter = list(dict.keys())[list(dict.values()).index(letter)]
    print(letter)
    
    crypt()
crypt()