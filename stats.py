def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(item):
    return item["num"]

def sorted_list(char_dict):
    result = []
    for char, count in char_dict.items():
        if char.isalpha():
            result.append({"char": char, "num": count})
    result.sort(key=sort_on, reverse=True)
    return result