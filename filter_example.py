
list1 = ['RRR', 'AAA', 'Rcsc', 'Aadsa']

new_list1 = filter(lambda x: x.startswith('R'), list1)
# print(list(new_list1), )

for i in new_list1:
    print(i)

new_list2 = (i for i in list1 if i.startswith('R'))
print(list(new_list2))