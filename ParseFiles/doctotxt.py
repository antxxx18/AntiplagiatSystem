#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

def doc_to_text(filename):
    os.system('antiword -m cp866.txt ' + filename + '.doc > ' + filename + '.txt')
    return filename + '.txt'