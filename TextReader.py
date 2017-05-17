import re
EXAMPLE_FILENAME = "Example.txt"
REGEX_EMPTY_STRING = re.compile("\s*")
REGEX_LETTER = re.compile("[А-Яа-я0-9eEёЁ\-]")
REGEX_VALID_WORDS = re.compile("[^А-Яа-я0-9,.:;-?! ]")
PUNCTUATION = "?!.,:;"


def read_words(filename, encoding="utf-8"):
    file = open(filename, encoding=encoding)
    for line in file.readlines():
        correct_string = fix_sentence(REGEX_VALID_WORDS.sub("", line.lower()))
        words = correct_string.split(" ")
        for word in words:
            if not is_empty(word):
                yield word
    file.close()


def fix_sentence(sentence):
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
        elif char in PUNCTUATION and len(chars) > 0:
            previous = chars.pop()
            chars.append(previous)
            if is_letter(previous):
                chars.append(" ")
                chars.append(char)
                word_ended = True
    new_sentence = "".join(chars).strip()
    return new_sentence


def is_letter(char):
    if len(char) != 1:
        return False
    return REGEX_LETTER.search(char) is not None


def is_empty(string):
    return not REGEX_EMPTY_STRING.fullmatch(string) is None


def print_words(filename=EXAMPLE_FILENAME):
    words = list(read_words(filename))
    print(" ".join(words))


def main():
    print_words()


if __name__ == '__main__':
    main()
