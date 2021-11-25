# Simple list
#              0    , 1 ,  2  ,    3   , 4 ,   5
list1 = ['Mitnik', 23, 1.65, 'Kevin', 20, 1.55]
#              -6   , -5,  -4 ,   -3   , -2,  -1

print(list1,'\n')

# List of List
list2 = [
            ['Joe', 23, 1.65],
            ['Tars', 20, 1.55],
            ['Mary', 50, 2.00]
           ]

print(list2,'\n')

# Access methods to list elements
print(list1[-4],'\n')
print(list1[1:4],'\n')
print(list1[3:],'\n')
print(list1[-6],'\n')
print(list1[:-2],'\n')

print(list2[0:1],'\n')
print(list2[1:2],'\n')
print(list2[:2],'\n')
print(list2[2:],'\n')

print(list2[0][1])
print(list2[1][0])
print(list2[2][2])
