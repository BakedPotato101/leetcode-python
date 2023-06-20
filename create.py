import os


def format_input(input_str):
    input_list = input_str.replace(".", "-").split()
    return "".join(input_list[0:2]) + "_" + "_".join(input_list[2:])


leetcode = input("Paste problem number and title below: \n")
formatted_leetcode = format_input(leetcode)
try:
    os.mkdir(formatted_leetcode)
except FileExistsError:
    print("Error: There is already a folder with this problem")
    exit()
print(f"Directory has been made under the name: '{formatted_leetcode}'\n")

f = open(f"{formatted_leetcode}/main.py", "+w")
print("main.py created\n")
f.write(f"#Put code below\n")
print("main.py updated\n")
f.close()
print(f"All done.")

