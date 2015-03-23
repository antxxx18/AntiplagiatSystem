#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

from ParseFiles import normalizetext
import database
import antiplagiarism


dataBase = database.DataBase()

# if not os.path.isfile("/var/www/html/vectors/" + sys.argv[1] + ".txt"):
#     text = normalizetext.Text("/var/www/html" + dataBase.get_path(int(sys.argv[1]))) #arg1 - file id
#     vector.set_vect(sys.argv[1], text)
# antiplagiarism.anti(sys.argv[1], dataBase.get_theme(int(sys.argv[1])))
if not dataBase.is_normalize(sys.argv[1]):
    text = normalizetext.Text("/var/www/html" + dataBase.get_path(int(sys.argv[1]))) #arg1 - file id
    dataBase.set_vect(sys.argv[1], text)
    antiplagiarism.anti(sys.argv[1], dataBase.get_theme(int(sys.argv[1])))

dataBase.close()