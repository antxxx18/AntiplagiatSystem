#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import database
import trigonometry
import vector
import normalizetext

def anti(arg1, arg2):
    dataBase = database.DataBase()
    #main_vect = vector.get_vect(arg1) #arg1 - checking document
    main_vect = dataBase.get_vect(arg1)
    max_coef = 0
    list = dataBase.get_list_work_of_theme(arg2)
    for id in list: #arg2 - id theme of work
        if id != int(arg1):
            #current_vect = vector.get_vect(id)
            current_vect = dataBase.get_vect(id)
            if current_vect == {}:
                text = normalizetext.Text("/var/www/html" + dataBase.get_path(id))
                #vector.set_vect(id, text)
                dataBase.set_vect(id, text)
                #current_vect = vector.get_vect(id)
                current_vect = dataBase.get_vect(id)
            cur_coef = trigonometry.multi_cos(main_vect, current_vect)
            dataBase.set_cur_coef(int(arg1), id, cur_coef)
            max_coef = max(max_coef, cur_coef)
    dataBase.set_max_coef(int(arg1), max_coef)
    dataBase.close()