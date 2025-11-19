def get_num_words(texts):
    list_of_words = texts.split()
    num_words = len(list_of_words)
    return num_words

def chars_count(texts):
    count = {}

    for c in texts:
        if not c.isalpha():
            continue
        
        c = c.lower()

        count[c] = count.get(c, 0) + 1
    
    return count

def sort_on(items, col = "cnt"):
    return items[col]

def sort_list_of_dict(dict_counts):
    ls = []
    
    for k, v in dict_counts.items():
        ls.append({"char": k, "cnt": v})

    ls.sort(reverse=True, key = sort_on)
    return ls