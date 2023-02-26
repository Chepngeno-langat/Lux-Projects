my_arr = [1,2,3]

def sum_array(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

a_sum = sum(my_arr)
print(a_sum)