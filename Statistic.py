import TextReader as Reader
from collections import deque


def make_ngrams(words_set, n):
    n_grams = {}
    words = deque()
    for word in words_set:
        words.append(word)
        if len(words) == n:
            n_gram = tuple(words)
            if n_gram in n_grams.keys():
                n_grams[n_gram] += 1
            else:
                n_grams[n_gram] = 1
            words.popleft()
    return n_grams


def statistic_sort(tuple):
    return tuple[0]


def make_statistic(words, ngram_size=3):
    n_grams = make_ngrams(words, ngram_size)
    statistic = []
    for n_gram, count in n_grams.items():
        temp = deque(n_gram)
        temp.appendleft(count)
        statistic.append(tuple(temp))
    statistic.sort(key=lambda x: x[0], reverse=True)
    return statistic


def main():
    words = Reader.read_words("BigText.txt")
    make_statistic(words)


if __name__ == '__main__':
    main()
