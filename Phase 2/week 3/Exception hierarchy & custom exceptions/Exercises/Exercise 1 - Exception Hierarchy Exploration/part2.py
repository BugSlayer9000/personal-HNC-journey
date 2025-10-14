# samod subhasha
# 14/10/25

# Basic exeption catching

number_list = [2,3,4,5,6] # 5 elements inside the list

try:
    value = number_list[10]
except IndexError:
    print("Error")
    
# this works because the Index error is the specific error that's raised