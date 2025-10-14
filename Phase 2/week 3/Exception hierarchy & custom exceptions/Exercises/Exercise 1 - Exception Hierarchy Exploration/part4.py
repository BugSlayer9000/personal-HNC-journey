# samod subhasha
# 14/10/25

# part 3 with Wrong order

number_list = [2,3,4,5,6] # 5 elements inside the list

try:
    value = number_list[10]
except LookupError:
    print("Look up error catched ! ")
# except IndexError:
#     print("Index error")

# index error never reached 