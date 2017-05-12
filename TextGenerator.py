import Statistic as stat
import random as rnd


def create_text(sentence_count=10):
    continuation_of_words = stat.make_continuation_of_words()
    words = list(continuation_of_words.keys())
    current_word = random_word(words)
    text = [make_headword(current_word)]
    sentence_count -=1
    while sentence_count > 0:
        continuation = random_word(continuation_of_words[current_word])
        sentence_count -= add_n_gram(text, continuation,current_word)
        current_word = continuation[len(continuation) - 1]
    return text


def random_word(list_of_words):
    index = rnd.randint(0, len(list_of_words) -1)
    return list_of_words[index]


def add_n_gram(text, n_gram,previous):
    punctuation = ".?!"
    sentence_count = 0
    x = list(n_gram)
    for e in x:
        if previous and previous in punctuation:
            e = make_headword(e)
            sentence_count +=1
        text.append(e)
        previous = e
    return sentence_count


def make_headword(word):
    return word[0].upper() + word[1:]


def unpack_tuple(tup):
    for x in range(0, len(tup)):
        yield tup[x]


def main():
    text = create_text()
    print(" ".join(text))

if __name__ == '__main__':
    main()