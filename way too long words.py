def shorten_word(word):
    if len(word) >= 10:
        return f"{word[0]}{len(word)}{word[-1]}"
    elif len(word)<10:
        return word
