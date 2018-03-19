import unittest
import Statistic as stat
import sys


class StatisticsShould(unittest.TestCase):

    def test_create_ngrams(self):
        words = ["набор", "слов", "для", "построения", "н-грамм", ",", "с", "пунктуацией"]
        expected = [
            ("набор", "слов", "для"),
            ("слов", "для", "построения"),
            ("для", "построения", "н-грамм"),
            ("построения", "н-грамм", ","),
            ("н-грамм", ",", "с"),
            (",", "с", "пунктуацией")
        ]
        actual = [x for x in stat.make_n_grams(words, 3)]
        expected.sort()
        actual.sort()
        self.assertSequenceEqual(expected, actual)

    def test_count_ngram(self):
        words = ["ла", "ла", "ла"]
        ngrams = stat.make_n_grams(words, 2)
        self.assertEqual(2, ngrams[("ла", "ла")])

    def test_create_statistic(self):
        ngrams = {
            ("hey", "ho"): 2,
            ("let's", "go"): 3,
            ("this", "test"): 5,
            ("go", "this"): 1
        }
        expected = [
            ("this", "test", 5),
            ("let's", "go", 3),
            ("hey", "ho", 2),
            ("go", "this", 1),
        ]
        actual = stat.make_n_gram_statistic(ngrams)
        self.assertEqual(expected, actual)

    def test_statistic_parsing(self):
        line = "one two three four = 5"
        self.assertEqual(("one", "two", "three", "four", 5), stat.parse_data(line))

    def test_read_write_statistic(self):
        statistic = [
            ("this", "test", 5),
            ("let's", "go", 3),
            ("hey", "ho", 2),
            ("go", "this", 1),
        ]
        stat.write_statistic(statistic, "test")
        result_stat = stat.read_statistic("test")
        self.assertEqual(statistic, result_stat)

    def test_arguments_parsing(self):
        arguments = "Statistics.py -f filename -s statistic -n 3".split(" ")
        sys.argv = arguments
        args = stat.parse_args()
        self.assertEqual(args.file[0], "filename")
        self.assertEqual(args.statistic[0], "statistic")
        self.assertEqual(args.ngram[0], 3)
        pass


if __name__ == '__main__':
    unittest.main()
