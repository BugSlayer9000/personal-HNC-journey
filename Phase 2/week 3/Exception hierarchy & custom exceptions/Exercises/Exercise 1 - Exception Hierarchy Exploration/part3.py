# samod subhasha
# 14/10/25

# Multiple exept blocks 

number_list = [2,3,4,5,6] # 5 elements inside the list

try:
    value = number_list[10]
except IndexError:
    print("Index error raised")
except LookupError:
    print("Look up error raised")
except Exception:
    print("exeption error raised")
    
# Index error raised
    