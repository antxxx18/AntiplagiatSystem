#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def is_preposition(word):
    prepositions = {'без', 'в', 'від', 'для', 'по', 'через', 'при', 'над', 'під', 'до', 'з', 'задля', 'поза', 'щодо',
                    'про', 'на', 'із', 'у', 'за'}
    return word in prepositions


def is_conjunction(word):
    conjunction = {'і', 'та', 'й', 'але', 'як', 'або', 'чи', 'коли', 'що', 'би', 'наскільки', 'хоч', 'мов', 'наче',
                   'щоб', 'якби', 'проте', 'то', 'а'}
    return word in conjunction


def is_fraction(word):
    fraction = {'це', 'якраз', 'власне', 'майже', 'саме', 'не', 'ні', 'ані', 'тільки', 'лише', 'хоч', 'таки', 'аж',
                'вже', 'ж', 'же', 'бо', 'нехай', 'б'}
    return word in fraction