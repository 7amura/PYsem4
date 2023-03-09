

my_dict = {1: 'one', 2: 'two', 3: 'three'}
my_list = ['six', 'four', 'five']

for i in my_dict.values():
    if i in my_list:
        print(True)
        break
else:
    print(False)    