num_of_bids = int(input("How many bids are there? "))
dict = {}
for i in range(num_of_bids):
    hi = {input("What is the name of the bidder? "): int(input("How much does he/she want to bid? "))}
    dict.update(hi)
    hi = {}
values = list(dict.values())
names = list(dict.keys())

print(names[values.index(max(values))])
