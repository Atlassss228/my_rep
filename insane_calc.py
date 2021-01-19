my_string2 = "( 4 + 5 + ( 1 / 3 * ( 10 ^ 3 - 1 * ( 10 + 3 ) - 11 * ( 5 + 2 ) * 2 ) + 2 ) / 2 ) ^ 0"

string_list2 = my_string2.split()
print(string_list2)

priority = 0
priority_max = 0
operator_list = ("*", "/", "+", "-", "^")

for el in string_list2:
    index = string_list2.index(el)
    if el == "(":
        priority += 1
    elif el == ")":
        priority -= 1

    if priority > priority_max:
        priority_max = priority

    if el in operator_list:
        string_list2.pop(index)
        string_list2.insert(index, (el, priority))

print(string_list2)

while True:
    if "(" in string_list2:
        string_list2.pop(string_list2.index("("))
    elif ")" in string_list2:
        string_list2.pop(string_list2.index(")"))
    else:
        break

print(string_list2)
print(priority_max)

while priority_max >= 0:
    while True:
        if ("/", priority_max) in string_list2:
            index = string_list2.index(("/", priority_max))
            temp_res = float(string_list2[index - 1]) / float(string_list2[index + 1])

        elif ("^", priority_max) in string_list2:
            index = string_list2.index(("^", priority_max))
            temp_res = float(string_list2[index - 1]) ** float(string_list2[index + 1])

        elif ("*", priority_max) in string_list2:
            index = string_list2.index(("*", priority_max))
            temp_res = float(string_list2[index - 1]) * float(string_list2[index + 1])

        elif ("+", priority_max) in string_list2:
            index = string_list2.index(("+", priority_max))
            temp_res = float(string_list2[index - 1]) + float(string_list2[index + 1])

        elif ("-", priority_max) in string_list2:
            index = string_list2.index(("-", priority_max))
            temp_res = float(string_list2[index - 1]) - float(string_list2[index + 1])



        else:
            break

        string_list2.pop(index - 1)
        string_list2.pop(index - 1)
        string_list2.pop(index - 1)
        string_list2.insert(index - 1, temp_res)

    print(string_list2)
    priority_max -= 1

print(string_list2)
