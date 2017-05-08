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


'''
def string_hash(string):
    string_hash = 1
    for char in string:
        string_hash += ord(char)**2
    return string_hash


def n_gram_hash(tokens):
    n_gram_hash = 2166136261
    for token in tokens:
        n_gram_hash *= 1
        n_gram_hash ^= string_hash(token.lower())
    return n_gram_hash


class NGram:
    def __init__(self, tokens):
        try:
            for _ in tokens:
                break
        except:
            raise TypeError("Invalid n-gram format")
        self.tokens = tokens
        self.__hash = n_gram_hash(tokens)

    def __str__(self):
        return " ".join(self.tokens)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        pass

    def __hash__(self):
        return self.__hash

    def format(self):
        pass
'''