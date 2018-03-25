#!usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv
import jieba
import jieba.analyse

import util


pre_path = "data/"

raw_data_file = "tnb.txt"

split_file = "split.txt"

stop_words_file = "stop_words.txt"

dict_file = "tnb_dict"



def add_user_dict(dict_file_name):
    dicts = set([])
    with open(util.get_file_name(pre_path, dict_file_name), 'r') as src:
        for line in src:
            tmp_line = line.strip().decode('utf-8')
            dicts.add(tmp_line)
    for ele in dicts:
        jieba.add_word(ele)


def get_stop_words(stop_file_name):
    stop_words = set([])
    with open(util.get_file_name(pre_path, stop_file_name), 'r') as src:
        for line in src:
            tmp_line = line.strip().decode('utf-8')
            stop_words.add(tmp_line)
    return stop_words


def remove_stop_word(words_ls, stop_words):
    new_words = []
    for word in words_ls:
        tmp_word = word.strip()
        if tmp_word in stop_words:
            continue
        new_words.append(tmp_word)
    return new_words


# jieba.load_userdict(get_file_name(dict_file))
# jieba.analyse.set_stop_words(get_file_name(stop_words_file))

add_user_dict(dict_file)
stop_words = get_stop_words(stop_words_file)
with open(util.get_file_name(pre_path, split_file), 'wa') as split_src:
    csv_writer = csv.writer(split_src, delimiter=' ')
    with open(util.get_file_name(pre_path, raw_data_file), 'r') as raw_src:
        for line in raw_src:
            tmp_line = line.strip()
            tmp_split = jieba.lcut(tmp_line, cut_all=False)
            dest_ls = remove_stop_word(tmp_split, stop_words)
            print dest_ls
            csv_writer.writerow(dest_ls)
