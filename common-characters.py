string1 = raw_input("Input your first string: ")
string2 = raw_input("Input your second string: ")

def get_common_chars(string1, string2):
    string1_len = len(string1)
    i=0
    common_chars = []
    while (i < string1_len):
        if (string1[i] in string2):
            if (string1[i] not in common_chars):
                common_chars.append(string1[i])
        i = i + 1

    return common_chars

print get_common_chars(string1,string2)
