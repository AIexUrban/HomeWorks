my_list = ['apple', 'watermelon', 'banana', 'cherry']
print(my_list)

new_list=my_list[:3] # третий элемент из my_list не входит
print(new_list)

new_list[2]='pineapple'
print(new_list)

new_list.append ('cherry1')
print(new_list)

new_list[0], new_list[3] = new_list[3], new_list[0]
print(new_list)


