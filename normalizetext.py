#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from docx import Document
import ukstemmer
import prepositions
import os
import doctotxt
import codecs

class Text():
    def create_vector(self, line):
        for word in line.split():
            if not (prepositions.is_preposition(word) or prepositions.is_conjunction(word) or prepositions.is_fraction(word)):
                s = ukstemmer.UkrainianStemmer(word)
                if s.stem_word() in self.vect:
                    self.vect[s.stem_word()] += 1
                else:
                    self.vect.update({s.stem_word(): 1})

    def init_doc(self, filename):
        f = codecs.open(filename, encoding='ibm866', mode='r')
        for line in f:
            self.create_vector(line)
        f.close()

    def init_docx(self, filename):
        docx = Document(filename)
        for paragraph in docx.paragraphs:
            self.create_vector(paragraph.text)

    def __init__(self, filename):
        self.vect = {}
        if os.path.splitext(filename)[1] == '.doc':
            filenametxt = doctotxt.doc_to_text(os.path.splitext(filename)[0])
            self.init_doc(filenametxt)
            os.remove(filenametxt)
        else:
            self.init_docx(filename)