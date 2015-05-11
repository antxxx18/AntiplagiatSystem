#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from filesparse import text
from datetime import datetime
from vector import create_vector
import sys
from algorithm import trigonometry
import math
import os
import urllib.request


class TextPair():

    def idf_transform(self, sentence, vect, sentence_num):
        return {word: math.log2(sentence_num / vect[word]) for word in sentence}

    def __init__(self, trans_text1, trans_text2):
        vector_similarity = trigonometry.multi_cos(trans_text1.vector, trans_text2.vector)
        similar_sentence_number = 0
        self.similar_sentence1 = []
        self.similar_sentence2 = []
        if vector_similarity > 0.5:
            for (i, sentence1) in enumerate(trans_text1.normal_sentence_list):
                for (j, sentence2) in enumerate(trans_text2.normal_sentence_list):
                    if len(sentence1) > 2 and len(sentence2) > 2:
                        idf_vector1 = self.idf_transform(sentence1, trans_text1.word_in_sentences_vector, len(trans_text1.sentence_list))
                        idf_vector2 = self.idf_transform(sentence2, trans_text2.word_in_sentences_vector, len(trans_text2.sentence_list))
                        sentence_similarity = trigonometry.multi_cos(idf_vector1, idf_vector2)
                        if sentence_similarity > 0.6:
                            similar_sentence_number += sentence_similarity
                            self.similar_sentence1.append(trans_text1.sentence_list[i])
                            self.similar_sentence2.append(trans_text2.sentence_list[j])
        self.similarity = similar_sentence_number / len(trans_text1.sentence_list)


def get_text_pairs(trans_text1, link_list):
    textPairs = []
    for url in link_list:
        filename = write_page(url)
        if filename:
            t2 = text.Text(filename)
            trans_text2 = create_vector.TransformText(t2.data, 0)
            textPair = TextPair(trans_text1, trans_text2)
            if not textPair.similar_sentence1:
                break
            textPairs.append(textPair)
    return textPairs


def write_page(url):
    ext = os.path.splitext(url)[1]
    if ext == '.txt' or ext == '.doc' or ext == '.docx' or ext == '.pdf':
        filename = 'download' + ext
    else:
        filename = 'download.html'
    try:
        html_page = urllib.request.urlopen(url).read()
        f = open(filename, 'wb')
        f.write(html_page)
    except UnicodeEncodeError:
        filename = False
    return filename


startTime = datetime.now()
txt = text.Text(sys.argv[1])
trans_txt = create_vector.TransformText(txt.data, 1)
link_list = trans_txt.parse(num_words=7)
textPairs = get_text_pairs(trans_txt, link_list)
for (i, textPair) in enumerate(textPairs):
    print('############')
    print(link_list[i])
    print('Similarity = ')
    print(textPair.similarity)
    print('------')
    print(textPair.similar_sentence1)
    print('------')
    print(textPair.similar_sentence2)
    print('############')
print(datetime.now() - startTime)