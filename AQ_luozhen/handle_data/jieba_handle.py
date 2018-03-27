#!usr/bin/env python
# coding:utf-8

import os
import jieba

class Jieba_Handle(object):
    def __init__(self, stop_file, user_dict_file=None):
        self.stop_file = stop_file
        self.user_dict_file = user_dict_file
        self.__add_user_dict()

    @staticmethod
    def get_user_words(file_name):
        if not isinstance(file_name, str) or not os.path.exists(file_name):
            return None
        user_words = set([])
        with open(file_name, 'r') as src:
            for line in src:
                tmp_line = line.strip().decode('utf-8')
                if not tmp_line:
                    continue
                user_words.add(tmp_line)
        return user_words

    def __add_user_dict(self):
        user_dict = self.get_user_words(self.user_dict_file)
        for w in user_dict:
            jieba.add_word(w)

    def remove_stop_words(self, split_words):
        stop_words = self.get_user_words(self.stop_file)
        dest_split_words = []
        for word in split_words:
            if word in stop_words or not word.strip():
                continue
            dest_split_words.append(word)
        return dest_split_words

    def split_words(self, sentence):
        raw_split = jieba.lcut(sentence, cut_all=False)
        return self.remove_stop_words(raw_split)
