import random as rn
list_og = [1,2,3,4,5,6]
new_list = []

time_itsgonnabeon = 1
for j in range(1,len(list_og)+1):
    time_itsgonnabeon *= j

while len(new_list) < time_itsgonnabeon:
    templist = list_og.copy()
    rn.shuffle(templist)
    if templist not in new_list:
        # print("in newlist")
        new_list.extend([templist])
    # print(len(new_list))
print(f"{new_list}\n") 