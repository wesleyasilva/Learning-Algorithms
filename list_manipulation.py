my_list = ['apple','banana','pear']
my_matrix = [['ps1','ps2','ps3'],['NES','SNES','N64']]

print('my_list: ',my_list)
print('\nmy_matrix: ',my_matrix)

# Add values in the same list/matrix
my_list += ['mango','coconut','cucumber']

my_matrix += [['x-box360','x-box','x-one']]

print('\n-------------------------\nNEW VALUES WAS ADD\n')
print('my_list: ',my_list)
print('\nmy_matrix: ',my_matrix)

# Delete values in the same list/matrix

del(my_list[-1])
del(my_matrix[2:])

print('\n-------------------------\nSOME VALUES WAS REMOVED\n')
print('my_list: ',my_list)
print('\nmy_matrix: ',my_matrix)

# Manipuling only values of list_copy/matrix_copy
# without make changes in the original lists/matrix
list_copy = list(my_list)
matrix_copy = my_matrix

del(list_copy[2])
del(matrix_copy[1][:2])

print('\n-------------------------\n')
print('my_matrix: ',my_matrix)
print('matrix_copy: ',matrix_copy)
