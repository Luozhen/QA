#!usr/bin/env python
# coding:utf-8

import jieba
from ..util import get_user_words


class Raw_Handle(object):
    def __init__(self, stop_file, user_dict_file=None):
        self.stop_file = stop_file
        self.user_dict_file = user_dict_file
        self.__add_user_dict()

    def __add_user_dict(self):
        user_dict = get_user_words(self.user_dict_file)
        for w in user_dict:
            jieba.add_word(w)

    def remove_stop_words(self, split_words):
        stop_words = get_user_words(self.stop_file)
        dest_split_words = []
        for word in split_words:
            if word in stop_words:
                continue
            dest_split_words.append(word)
        return dest_split_words

    def split_words(self, sentence):
        raw_split = jieba.lcut(sentence, cut_all=False)
        return self.remove_stop_words(raw_split)
