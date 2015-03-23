#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import codecs

PATH = "/var/www/html/vectors/"
def set_vect(text_id, text):
    f = open(PATH + str(text_id) + ".txt", 'w')
    for el in text.vect.keys():
        if el != '':
            #f.write(str(b''.join(el)) + ' ' + str(text.vect[el]) + '\n')
            f.write(str(el.encode('utf-8')) + ' ' + str(text.vect[el]) + '\n')
            #print(el + ' ' + str(text.vect[el]) + '\n')
            #f.write(el + ' ' + str(text.vect[el]) + '\n')
    f.close()
def get_vect(text_id):
    try:
        vect = {}
        f = codecs.open(PATH + str(text_id) + ".txt", encoding="utf-8", mode='r')
        #f = open(PATH + str(text_id) + ".txt", 'r')
        for line in f:
            print(line)
            word = line.split()
            vect.update({word[0]: int(word[1])})
        f.close()
        return vect
    except IOError:
        return {}