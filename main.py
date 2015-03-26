#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from parsefiles import text
from parsegoogle.parse import parse
from vector import create_vector
import sys

num_words = 8

t = text.Text(sys.argv[1])
res = create_vector.transform_to_vector(t.data, 1)
main_vector = res[0]
query_line = res[1]
print(main_vector)
print(query_line)
i = 0
query = [[]]
for word in query_line:
    if i > num_words:
        query = query[1:].append(word)
        parse(query)
    else:
        query[0].append(word)

"""
    max_coef = 0
    list = dataBase.get_list_work_of_theme(arg2)
    for id in list: #arg2 - id theme of work
        if id != int(arg1):
            #current_vect = vector.get_vect(id)
            current_vect = dataBase.get_vect(id)
            if current_vect == {}:
                text = text.Text("/var/www/html" + dataBase.get_path(id))
                #vector.set_vect(id, text)
                dataBase.set_vect(id, text)
                #current_vect = vector.get_vect(id)
                current_vect = dataBase.get_vect(id)
            cur_coef = trigonometry.multi_cos(main_vect, current_vect)
            dataBase.set_cur_coef(int(arg1), id, cur_coef)
            max_coef = max(max_coef, cur_coef)
    dataBase.set_max_coef(int(arg1), max_coef)
    dataBase.close()
"""