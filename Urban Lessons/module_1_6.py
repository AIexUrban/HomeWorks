# Dictionary & variety

# item 2
my_dict= {'George':1981, 'John':1979, 'Sofiya':2001, 'Margo':1989}
print('Dict:',my_dict)
print('Existing value: ',my_dict['John'])
print('Not existing value: ', my_dict.get('Alex'))
my_dict.update({'Serge':52, 'Julia':33}) # Добавляем значения
a=my_dict.pop('Sofiya')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)

# item 3
my_set={1,3,1,3,'Apple', (15,16,34),4,5,6,3.1415926,8,1,3,4,5,6}
print('Set: ', my_set)
list_ = ['Tree', 2.33]
list_ = set(list_)
my_set.update (list_)
print('Modified set: ', my_set)

#END
