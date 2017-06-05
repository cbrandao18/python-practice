def find_target_word(string, target):
    len_string = len(string)
    len_target = len(target)
    i=0
    j=1
    word_position = 0
    list_of_pos = []

    while i < len_string:
        if string[i] is ' ':
            word_position = word_position + 1
        if string[i] == target[0]:
            i = i + 1
            while j < len_target and string[i] == target[j]:
                i = i + 1
                j = j + 1
                if j == len_target:
                    list_of_pos.append(word_position)
                    j = 1
                    i = i - 1
                    word_position = word_position + 1
        i = i + 1

        
    if len(list_of_pos) > 0:
        print list_of_pos
        return True
    else:
        return False

find_target_word("we dont need no education we dont need no thought control no we dont", "dont")
