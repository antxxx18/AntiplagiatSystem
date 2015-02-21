#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql


class DataBase():
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', passwd='opexfc12', db='db')
        self.cursor = self.db.cursor()
        self.db.set_charset('utf8')
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection=utf8;')

    def set_vect(self, text_id, text):
        add_vect_query = "INSERT INTO  `o_w1` (`id`, `work_id`, `word`, `count`) VALUES (NULL, %(work_id)s, %(word)s, %(count)s);"
        for el in text.vect.keys():
            self.cursor.execute(add_vect_query, {'work_id': text_id, 'word': el.encode('utf-8'), 'count': text.vect[el]})

    def get_theme(self, text_id):
        get_theme_query = "SELECT * FROM  `o_work` WHERE  `id` =%s"
        numrows = int(self.cursor.execute(get_theme_query, text_id))
        row = self.cursor.fetchone()
        return row[2]

    def get_path(self, text_id):
        get_path_query = "SELECT * FROM  `o_work` WHERE  `id` =%s"
        numrows = int(self.cursor.execute(get_path_query, text_id))
        row = self.cursor.fetchone()
        return row[5]

    def get_vect(self, text_id):
        get_vect_query = "SELECT * FROM  `o_w1` WHERE `work_id` = %s"
        numrows = int(self.cursor.execute(get_vect_query, text_id))
        vect={}
        for x in range(0, numrows):
            row = self.cursor.fetchone()
            vect.update({row[2]: row[3]})
        return vect

    def get_list_work_of_theme(self, theme):
        get_list_query = "SELECT * FROM  `o_work` WHERE `workname_id` = %s"
        numrows = int(self.cursor.execute(get_list_query, theme))
        list=[]
        for x in range(0, numrows):
            row = self.cursor.fetchone()
            list.append(row[0])
        return list

    def set_max_coef(self, text_id, coef):
        set_max_query = "UPDATE  `o_work` SET  `originality` =  %(orig)s WHERE  `o_work`.`id` =%(id)s;"
        self.cursor.execute(set_max_query, {'orig': coef, 'id': text_id})

    def set_cur_coef(self, id1, id2, coef):
        add_cur_query = "INSERT INTO `o_same` (`id`, `work1_id`, `work2_id`, `same`) VALUES (NULL, %(work1_id)s, %(work2_id)s, %(same)s);"
        self.cursor.execute(add_cur_query, {'work1_id': id1, 'work2_id': id2, 'same': coef})

    def is_normalize(self, text_id):
        is_normalize_query = "SELECT * FROM  `o_w1` WHERE  `work_id` =%s"
        numrows = int(self.cursor.execute(is_normalize_query, text_id))
        if numrows == 0:
            return 0
        return 1

    def close(self):
        self.db.close()