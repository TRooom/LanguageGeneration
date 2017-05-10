import TextReader as Reader
from collections import deque
import math


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


def take_part(coefficient, sorter, list):
    result_length = math.ceil(len(list)*coefficient)
    list.sort(key=sorter)
    new_list = []
    for x in range(0, result_length):
        temp = list[x][0:len(list[x])-1]
        new_list.append(temp)
    return new_list


def make_n_gram_statistic(words, n_gram_size=3):
    n_grams = make_ngrams(words, n_gram_size)
    statistic = []
    for n_gram, count in n_grams.items():
        temp = deque(n_gram)
        temp.append(count)
        statistic.append(tuple(temp))
    #statistic.sort(key=lambda x: x[0], reverse=True)
    return statistic


def make_words_statistic(statistic):
    words_stat = {}
    for data in statistic:
        start = data[0]
        continuation = data[1:len(data)+1]
        if start in words_stat:
            words_stat[start].append(continuation)
        else:
            words_stat[start] = []
            words_stat[start].append(continuation)
    return words_stat


def take_most_freqence(words_stat):
    for key in words_stat:
        words_stat[key] = take_part(0.7, lambda x: x[len(x)-1], words_stat[key])


def make_continuation_of_words():
    words = Reader.read_words("BigText.txt")
    n_gram_statistic = make_n_gram_statistic(words)
    words_statistic = make_words_statistic(n_gram_statistic)
    take_most_freqence(words_statistic)
    return words_statistic


if __name__ == '__main__':
    pass
