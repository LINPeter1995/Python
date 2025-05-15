list1 = [1, 2, 3]
list2 = [1, 2, 3]
# list即使值相同，參照到的實例未必相同
print(f"id(list1): {id(list1)}\nid(list2): {id(list2)}")
print(f"{list1} == {list2}: {list1 == list2}")
print(f"{list1} is {list2}: {list1 is list2}")
print(f"{list1} is not {list2}: {list1 is not list2}")

# int, float, bool, str, tuple若值相同，參照到的實例也相同
int1 = 1
int2 = 1
float1 = 2.2
float2 = 2.2
bool1 = True
bool2 = True
str1 = "abc"
str2 = "abc"
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
print(f"id(int1): {id(int1)}\nid(int2): {id(int2)}")
print(f"{int1} == {int2}: {int1 == int2}")
print(f"{int1} is {int2}: {int1 is int2}")
print(f"id(float1): {id(float1)}\nid(float2): {id(float2)}")
print(f"{float1} == {float2}: {float1 == float2}")
print(f"{float1} is {float2}: {float1 is float2}")
print(f"id(bool1): {id(bool1)}\nid(bool2): {id(bool2)}")
print(f"{bool1} == {bool2}: {bool1 == bool2}")
print(f"{bool1} is {bool2}: {bool1 is bool2}")
print(f"id(str1): {id(str1)}\nid(str2): {id(str2)}")
print(f"{str1} == {str2}: {str1 == str2}")
print(f"{str1} is {str2}: {str1 is str2}")
print(f"id(tuple1): {id(tuple1)}\nid(tuple2): {id(tuple2)}")
print(f"{tuple1} == {tuple2}: {tuple1 == tuple2}")
print(f"{tuple1} is {tuple2}: {tuple1 is tuple2}")

