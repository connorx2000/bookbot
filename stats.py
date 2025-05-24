def get_word_count(words):
    letters = words.split()
    return len(letters)

def get_char_count(words):
    uniques = {}
    for char in words:
        l_char = char.lower()
        if l_char.isalpha():
            if l_char in uniques:
                uniques[l_char] += 1
            else:
                uniques[l_char] = 1
    return uniques

def sort_on(dict):
    return dict["num"]

def dict_sort(uniques):
    char_list = []
    for char, num in uniques.items():
        temp_dict = {"char": char, "num": num}
        char_list.append(temp_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list