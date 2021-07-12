lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
list1 = list()
list1 = [list1.append(i) for i in lst if i not in list1]
print(list1)

print(list(set(lst)))
