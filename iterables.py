"""create iterator and container_iterator"""
import re


class MultipleSentencesError(Exception):
    """Exception for case multi sentence in the line"""

    def __str__(self):
        return "MultipleSentencesError\n More than one sentence in the line"


class Sentence:
    """Class container"""
    def __init__(self, text: str):
        if self.line_checker(text) and self.sentence_checker(text):
            self.text = text

    @staticmethod
    def line_checker(text):
        """Check text. Text must be str, else raise TypeError"""
        if isinstance(text, str):
            return True
        raise TypeError

    @staticmethod
    def sentence_checker(text):
        """Check line. Line must have complete sentence and one sentence only. """
        checking = text[-1]
        # check last sentence symbol. it must be one of '!', '.', '?'
        if checking not in ("!", ".", "?"):
            raise ValueError
        # check that before space symbol we have no any symbol from '!', '.', '?'
        if re.search(r"([!?.]\s)", text):

            raise MultipleSentencesError
        return True

    def _words(self):
        """display one word"""
        all_words = SentenceIterator(self.text)
        for word_and_chars in iter(all_words):
            yield word_and_chars

    @property
    def words(self):
        """display all words from the text"""
        all_words = SentenceIterator(self.text)
        for word_and_chars in all_words:
            print(word_and_chars[0])

    @property
    def other_chars(self):
        """display all other chars from text"""
        all_words = SentenceIterator(self.text)
        for word_and_chars in all_words:
            print(word_and_chars[1])

    def __repr__(self):
        """display quantity of words and other chars"""
        all_words = SentenceIterator(self.text)
        word_count = 0
        other_chars_count = 0
        for position, word_and_chars in enumerate(all_words):
            word_count = position + 1
            other_chars_count += len(word_and_chars[1])
        return f"<Sentence(words={word_count}, other_chars={other_chars_count})>"

    def __iter__(self):
        return SentenceIterator(self.text)


class SentenceIterator:
    """class iterator"""
    def __init__(self, text):
        self.text = text
        self.start = 0
        self.stop = len(self.text)
        self.word_stop = 0
        self.segment = ""
        self.other_chars = ""
        self.flag_stop_iteration = False

    def gen_word(self):
        """find fist brake in sentence"""
        self.other_chars = ""
        if self.flag_stop_iteration:
            raise StopIteration
        # find first brake in checking segment
        self.word_stop = self.text.find(" ", self.start, self.stop)
        # case: if there is no any spaces in checking segment
        if self.word_stop == -1:
            # set end of checking segment to end of text
            self.word_stop = self.stop
            self.flag_stop_iteration = True
        else:
            # case: if space found - append space to other chars
            self.other_chars += " "
        # set checking segment
        self.segment = self.text[self.start: self.word_stop]
        # set start of new checking segment
        self.start = self.word_stop + 1
        return self.separate_word_and_symbols()

    def separate_word_and_symbols(self):
        """separate word from other symbols(like: .,!?)"""
        # start checking from end of the word
        for index in range(len(self.segment) - 1, 0, -1):
            if self.segment[index] in (".", ",", "!", "?", " "):
                # append other symbols
                self.other_chars += self.segment[index]
                # print(self.other_chars)
            else:
                break
            # store other chars and clear for new iteration
            other_chars = self.other_chars

        return self.segment[: index+1], other_chars

    def __next__(self):
        return self.gen_word()

    def __iter__(self):
        return self


text1 = Sentence("Hello.., world!!!")

# text1.words
# text1.other_chars
# print(text1._words())
# print(text1)
