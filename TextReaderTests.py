import unittest
import TextReader as reader


class Reader_Should(unittest.TestCase):
    def test_detect_empty_string(self):
        self.assertTrue(reader.is_empty(""))
        self.assertTrue(reader.is_empty(" "))
        self.assertTrue(reader.is_empty("   "))
        self.assertTrue(reader.is_empty("\r"))
        self.assertTrue(reader.is_empty("\r\n\t       "))

    def test_detect_letter(self):
        alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя"
        for letter in alphabet:
            self.assertTrue(reader.is_letter(letter))

    def test_detect_nonletter(self):
        non_alphabet = "!"  # $%&\'()*+,'"
        for sym in non_alphabet:
            self.assertFalse(reader.is_letter(sym))
        self.assertFalse(reader.is_letter("аа"))

    def test_trim_sentence(self):
        self.assertEqual("слово слово", reader.fix_sentence(" слово слово "))

    def test_separate_punctuation(self):
        self.assertEqual("слово , слово", reader.fix_sentence("слово,слово"))

    def test_read_from_file(self):
        self.write("test", "это самое обычное предложение")
        self.assertListEqual(["это", "самое", "обычное", "предложение"], [x for x in reader.read_words("test")])

    def write(self, filename, text):
        with open(filename, "w") as file:
            file.write(text)

    def test_fix_sentence_with_endash(self):
        sentence = "Предложение с-дефисом"
        self.assertEqual(sentence, reader.fix_sentence(sentence))


if __name__ == '__main__':
    unittest.main()
