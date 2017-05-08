import re


def read_words(filename):
    file = open(filename, encoding="cp1251")
    valid_words = re.compile("[^А-Яа-я0-9,.:;-?! ]")
    for line in file.readlines():
        correct_string = fix_sentence(valid_words.sub("", line.lower()))
        words = correct_string.split(" ")
        for word in words:
            if not is_empty(word):
                yield word
    file.close()


def fix_sentence(sentence):
    punctuation = "?!.,:;"
    word_ended = False
    chars = []
    for char in sentence:
        if is_letter(char) and not word_ended:
            chars.append(char)
        elif is_letter(char) and word_ended:
            chars.append(" ")
            chars.append(char)
            word_ended = False
        elif char == " ":
            word_ended = True
        elif char == "-" and not word_ended:
            chars.append(char)
        elif char in punctuation and len(chars) > 0:
            previous = chars.pop()
            chars.append(previous)
            if is_letter(previous):
                chars.append(" ")
                chars.append(char)
                word_ended = True
    new_sentence = "".join(chars).strip()
    return new_sentence


def is_letter(char):
    letters = re.compile("[А-Яа-я0-9eEёЁ\-]")
    if len(char) != 1:
        return False
    return letters.search(char) is not None


def is_empty(string):
    regex = re.compile("\s*")
    if regex.fullmatch(string) is  None:
        return False
    else:
        return True


def print_words():
    for w in read_words("Text.txt"):
        print(w)


def main():
    print_words()


if __name__ == '__main__':
    main()
