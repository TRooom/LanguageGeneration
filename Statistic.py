import textReader as reader
from collections import deque
import argparse
import itertools


def parse_args():
    parser = argparse.ArgumentParser(description="Create ngrams for the given text and write to file")
    parser.add_argument("-f", "--file", nargs='+', metavar="FILENAME",
                        default=["source.txt"], help="text file for creation ngrams")
    parser.add_argument("-s", "--statistic", nargs=1, metavar="FILENAME",
                        default="statistic.txt", help="file in which the statistics will be written")
    parser.add_argument("-n", "-ngram", nargs=1, type=int, metavar="SIZE",
                        default=3, help="set ngrams size")
    return parser.parse_args()


def make_n_grams(words_set):
    n_grams = {}
    words = deque()
    for word in words_set:
        words.append(word)
        if len(words) == n_gram_size:
            n_gram = tuple(words)
            if n_gram in n_grams.keys():
                n_grams[n_gram] += 1
            else:
                n_grams[n_gram] = 1
            words.popleft()
    return n_grams


def make_n_gram_statistic(n_grams):
    statistic = []
    for n_gram, count in n_grams.items():
        temp = deque(n_gram)
        temp.append(count)
        statistic.append(tuple(temp))
    statistic.sort(key=lambda x: x[-1], reverse=True)
    return statistic


def write_statistic(statistic, filename, encoding="utf-8"):
    file = open(filename, "w", encoding=encoding)
    for data in statistic:
        string = " ".join(list(data)[:-1]) + " = " + str(data[-1]) + "\n"
        file.write(string)
    file.close()


def read_statistic(filename, encoding="utf-8"):
    statistic = []
    file = open(filename, "r", encoding=encoding)
    for line in file.readlines():
        data = parse_data(line)
        statistic.append(data)
    file.close()
    return statistic


def parse_data(line):
    data = line.split(" ")
    data.remove("=")
    count = int(data.pop())
    data.append(count)
    data = tuple(data)
    return data


def main():
    args = parse_args()
    files = args.file
    stat_path = args.statistic
    n_gram_size = args.ngram
    words = []
    for file in files:
        words = itertools.chain(words, reader.read_words(file))
    n_grams = make_n_grams(words, n_gram_size)
    stat = make_n_gram_statistic(n_grams)
    write_statistic(stat, stat_path)


if __name__ == '__main__':
    main()
