string = input("Enter the sentence: ").replace(" ", "")


# sorted_str = [x for x in string[1:] if x < string[0]]  + list(string[0]) + [x for x in string[1:] if x >= string[0]]

# sorted_str = ("".join(sorted_str))
# rev_sorted_str = sorted_str[::-1]

# empty_list.append(sorted_str)
# empty_list.append(rev_sorted_str)

# print(empty_list)

string = list(string)

for i in range(len(string)):
    for j in range(len(string)-1):
        if string[j] > string[j + 1]:
            string[j] , string[j + 1] = string[j+1], string[j]
        
new_str = "".join(string)
rev_str = new_str[::-1]

sorted_str = [new_str, rev_str]

print(sorted_str)

