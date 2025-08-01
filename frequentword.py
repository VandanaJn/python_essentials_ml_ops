def get_words_count(file_name):
    words_count = {}
    with open(file_name, "r", encoding="utf-8") as file:
        words = file.read().split()
    for word in words:
        word = word.lower().strip('.,!?";:()[]{}<>')
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return words_count


def get_top_words_dict(words_count, top_n=10):
    sorted_words = sorted(words_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:top_n]


def get_top_words(words_count, top_n=10):
    sorted_words = sorted(
        words_count.keys(), key=lambda key: words_count[key], reverse=True
    )
    return sorted_words[:top_n]


if __name__ == "__main__":
    w_count = get_words_count("sample.txt")
    get_top_words = get_top_words(w_count, 10)

    for wrd in get_top_words:
        print(f"{wrd}: {w_count[wrd]}")
