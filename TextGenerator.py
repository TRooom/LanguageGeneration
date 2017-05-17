import statistic as stat
import random as rnd
import math
import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", default=50, type=int, help="set sentence count")
    parser.add_argument("-f", "--factor", type=int, default=0.7, help="set selective factor")
    parser.add_argument("-s", "--statistic", type=str, help="statistic file")
    return parser.parse_args()


def create_text(continuation_of_words, sentence_count):
    words = list(continuation_of_words.keys())
    current_word = random_word(words)
    text = [make_headword(current_word)]
    sentence_count -= 1
    while sentence_count > 0:
        continuation = random_word(continuation_of_words[current_word])
        sentence_count -= add_n_gram(text, continuation, current_word)
        current_word = continuation[-1]
    return text


def fix_text(text):
    regex = re.compile(" (?=[,.?!])")
    return regex\
        .sub("", text)


def random_word(list_of_words):
    index = rnd.randint(0, len(list_of_words) - 1)
    return list_of_words[index]


def add_n_gram(text, n_gram, previous_word):
    punctuation = ".?!"
    sentence_count = 0
    x = list(n_gram)
    for e in x:
        if previous_word and previous_word in punctuation:
            e = make_headword(e)
            sentence_count += 1
        text.append(e)
        previous_word = e
    return sentence_count


def make_headword(word):
    return word[0].upper() + word[1:]


def unpack_tuple(tup):
    for x in range(0, len(tup)):
        yield tup[x]


def take_most_frequent_n_grams(words_stat, factor):
    for key in words_stat:
        schedule = words_stat[key]
        result_length = int(math.ceil(len(schedule) * factor))
        schedule.sort(key=lambda z: z[len(z) - 1])
        new_list = []
        for x in range(0, result_length):
            temp = schedule[x][0:len(schedule[x]) - 1]
            new_list.append(temp)
        words_stat[key] = new_list


def make_continuation_of_words(n_gram_statistic):
    words_statistic = make_words_statistic(n_gram_statistic)
    return words_statistic


def make_words_statistic(statistic):
    words_stat = {}
    for data in statistic:
        start = data[0]
        continuation = data[1:len(data) + 1]
        if start in words_stat:
            words_stat[start].append(continuation)
        else:
            words_stat[start] = []
            words_stat[start].append(continuation)
    return words_stat


def main():
    args = parse_args()
    statistic = stat.read_statistic(args.statistic)
    words = make_continuation_of_words(statistic)
    take_most_frequent_n_grams(words, args.factor)
    text = create_text(words, args.count)
    text = " ".join(text)
    print(fix_text(text))


if __name__ == '__main__':
    main()
