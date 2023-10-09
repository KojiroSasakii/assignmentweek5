input_str = input("please Enter string: ")

num_count = 0
upper_count = 0
lower_count = 0
other_count = 0

for char in input_str:
    if char.isdigit():
        num_count += 1
    elif char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    else:
        other_count += 1

print("uppercase letters:", upper_count)
print("lowercase letters:", lower_count)
print("numbers:", num_count)
print("other characters:", other_count)
