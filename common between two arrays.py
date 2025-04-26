#define two arrays(list)
array1=[1,2,3,4,5]
array2=[4,5,6,7,8]


#convert arrays o sets and find intersection
common_values=set(array1).intersection(set(array2))


#convert the result back to a list
common_values=list(common_values)


#pint the common values
print("common values between the two arrays:",common_values)
