##Testing for loops.
#for letter in "Fox Academy":
#    print(letter)

friends=["fox", "lion", "bear"]
for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First loop iteration")
    else:
        print("Not the first loop iteration")