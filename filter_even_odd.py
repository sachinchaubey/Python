

# FILTTER : ODD AND EVEN AND RETURN:

def filter_odd_even(l):
    odd_nums = []      # here we make a empty even_num var : for assinge to even valuse 
    even_nums = []      # here we make a empty odd_nums var for assings to odd no:
    for i in l:
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output = [odd_nums,even_nums]
    return output

nums = [1,2,3,4,5,6,7]
print(filter_odd_even(nums))

