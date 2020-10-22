##some practice lists functions for me to learn to code.
##list uses () while tuples use []
lucky_num=[21, 3,4 , 33,45, 22]
print(lucky_num)

names=['kayden', 'mia', 'ursula', 'savita', 'lola', 'lolita']
print(names)
#names.extend(lucky_num)
lucky_num.append(22)
print(lucky_num)
names.insert(3, "shobha")
print(names)

names2=names
names2.remove('lolita')
print(names2)
names3=names2
print(names3)
#names3.clear()
names3.pop()
print(lucky_num.index(45))
print(lucky_num.count(22))
lucky_num.sort()
print(lucky_num)

#lucky_num1=lucky_num
#lucky_num1.reverse()
#print(lucky_num1)

lucky_num2=lucky_num.copy()
print(lucky_num2)