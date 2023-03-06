my_dict = {"color": "red", "width": 17, "height": 19}
value_to_find = "red"
# Brute force solution (fastest) -- single key
for key, value in my_dict.items():
    if value == value_to_find:
        print(f'{key}: {value}')
        break
# Brute force solution -- multiple keys
for key, value in my_dict.items():
    if value == value_to_find:
        print(f'{key}: {value}')