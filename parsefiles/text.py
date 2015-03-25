#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###

import os
import codecs

from docx import Document


class Text():

    def doc_to_txt(self, filename):
        os.system('antiword ' + filename + '.doc > ' + filename + '.txt')
        return filename + '.txt'

    def init_txt(self, filename):
        f = codecs.open(filename, mode='r')
        for line in f:
            self.data += line
        f.close()

    def init_docx(self, filename):
        docx = Document(filename)
        for paragraph in docx.paragraphs:
            self.data = paragraph.text

    def __init__(self, filename):
        self.data = ""
        if os.path.splitext(filename)[1] == '.doc':
            filenametxt = self.doc_to_txt(os.path.splitext(filename)[0])
            #print(filenametxt)
            self.init_txt(filenametxt)
            os.remove(filenametxt)
        elif os.path.splitext(filename)[1] == '.docx':
            self.init_docx(filename)
        else:
            self.init_txt(filename)