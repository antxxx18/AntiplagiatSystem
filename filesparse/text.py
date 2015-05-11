#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import codecs
from docx import Document
from bs4 import BeautifulSoup


class Text():

    def pdf_to_txt(self, filename):
        os.system('pdftotext ' + filename + '.pdf ' + filename + '.txt')
        return filename + '.txt'

    def doc_to_txt(self, filename):
        os.system('wvText ' + filename + '.doc ' + filename + '.txt')
        return filename + '.txt'

    def init_txt(self, filename):
        f = codecs.open(filename, mode='r')
        for line in f:
            self.data += line
        f.close()

    def init_docx(self, filename):
        docx = Document(filename)
        for paragraph in docx.paragraphs:
            self.data += paragraph.text + " "

    def init_html(self, filename):
        try:
            page = codecs.open(filename, 'rb')
            soup = BeautifulSoup(page)
        except UnicodeDecodeError:
            win = codecs.open(filename, 'rb', 'windows-1251')
            uni = codecs.open(filename, 'wb', 'utf-8')
            uni.write(win.read())
            uni.close()
            page = codecs.open(filename, 'rb')
            soup = BeautifulSoup(page.read())
        all_text = soup.find_all('p')
        for one in all_text:
            self.data += one.text + '\n'

    def __init__(self, filename):
        self.data = ""
        name = os.path.splitext(filename)[0]
        extension = os.path.splitext(filename)[1]
        if extension == '.doc':
            filenametxt = self.doc_to_txt(name)
            self.init_txt(filenametxt)
            os.remove(filenametxt)
        elif extension == '.docx':
            self.init_docx(filename)
        elif extension == '.pdf':
            filenametxt = self.pdf_to_txt(name)
            self.init_txt(filenametxt)
            os.remove(filenametxt)
        else:
            self.init_html(filename)