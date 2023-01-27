'''WAP to Sort the List [3,4,2,1,5]'''


'''Using sort function'''
# l=[2,77,33,44,55,64,90,6,34,22,10]
# l.sort()
# print(l)

'''Without using sort function'''

data_list=[2,77,33,44,55,64,90,6,34,22,10]
new_list=[]
while data_list:
    minimum=data_list[0]
    for x in data_list:
        if x<minimum:
            minimum=x
    new_list.append(minimum)
    data_list.remove(minimum)
print(new_list)
