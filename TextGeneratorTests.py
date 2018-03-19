import unittest
import TextGenerator as generator
import sys


class TextGenerator_Should(unittest.TestCase):
    def test_create_word_statistic(self):
        statistic = [
            ("two", "gram", 2),
            ("three", "gram", 3),
            ("four", "gram", 4),
            ("two", "nongram", 2)
        ]
        actual = generator.make_words_statistic(statistic)
        expected = {
            "two": [("gram", 2), ("nongram", 2)],
            "three": [("gram", 3)],
            "four": [("gram", 4)]
        }
        self.assertEqual(actual, expected)

    def test_freq_selection(self):
        word_stat = {
            "word":
                [("continuation1", 1),
                 ("continuation2", 2),
                 ("continuation3", 3),
                 ("continuation4", 4), ]
        }
        selected_stat = generator.take_most_frequent_n_grams(word_stat, 0.5)
        self.assertDictEqual(word_stat, {
            "word":
                [("continuation4",),
                 ("continuation3",)]
        })

    def test_adding_ngram(self):
        text = []
        previous = ""
        count = generator.add_n_gram(text, ("this", "is", "end", "."), previous)
        self.assertEqual(count, 0)
        self.assertEqual(text, ["this", "is", "end", "."])

    def test_fix_text(self):
        text = "text , with punctuation"
        self.assertEqual(generator.fix_text(text), "text, with punctuation")

    def test_create_headword(self):
        word = "word"
        self.assertEqual(generator.make_headword(word), "Word")

    def test_get_random_word(self):
        words = ["one", "two", "three", "four"]
        one = generator.random_word(words)
        another = generator.random_word(words)
        self.assertTrue(one in words)
        self.assertTrue(another in words)
        self.assertNotEqual(one, another)

    def test_counting_sentences(self):
        text = []
        previous = ""
        count = generator.add_n_gram(text, [".", "the", "start"], previous)
        self.assertEqual(count, 1)

    def test_arguments_parsing(self):
        arguments = "TextGenerator.py -f 0.7 -c 50 -s statistic".split(" ")
        sys.argv = arguments
        args = generator.parse_args()
        self.assertEqual(args.count, 50)
        self.assertEqual(args.factor, 0.7)
        self.assertEqual(args.statistic, "statistic")


if __name__ == '__main__':
    unittest.main()
