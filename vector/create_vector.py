from vector import ukstemmer, prepositions
from searchengineparse import parse
import nltk.data


class TransformText():
    def __init__(self, text, mode):
        sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        self.vector = {}
        self.query_list = []
        self.word_in_sentences_vector = {}
        self.sentence_list = sent_detector.tokenize(text.strip())
        self.normal_sentence_list = []
        for sentence in self.sentence_list:
            word_list = sentence.split()
            sentence = []
            for word in set(word_list):
                if len(word) > 2 and not (prepositions.is_preposition(word) or prepositions.is_conjunction(word) or prepositions.is_fraction(word)):
                    s = ukstemmer.UkrainianStemmer(word)
                    stem_word = s.stem_word()
                    if stem_word != '':
                        if stem_word in self.word_in_sentences_vector:
                            self.word_in_sentences_vector[stem_word] += 1
                        else:
                            self.word_in_sentences_vector.update({stem_word: 1})
            for word in word_list:
                if len(word) > 2 and not (prepositions.is_preposition(word) or prepositions.is_conjunction(word) or prepositions.is_fraction(word)):
                    if mode and ukstemmer.ukstemmer_search_preprocess(word) != "":
                        self.query_list.append(ukstemmer.ukstemmer_search_preprocess(word))
                    s = ukstemmer.UkrainianStemmer(word)
                    stem_word = s.stem_word()
                    if stem_word != '':
                        sentence.append(stem_word)
                        if stem_word in self.vector:
                            self.vector[stem_word] += 1
                        else:
                            self.vector.update({stem_word: 1})
            self.normal_sentence_list.append(sentence)

    def parse(self, num_words):
        query = [[]]
        for (i, word) in enumerate(self.query_list):
            if i > num_words:
                t = query[-1][1:]
                t.append(word)
                query.append(t)
            else:
                query[0].append(word)
        parsed_tuples = parse.parse(query)
        return [a for (a, b) in parsed_tuples]