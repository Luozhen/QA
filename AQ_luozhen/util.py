#!usr/bin/env python
# coding:utf-8


def get_file_name(pre_path, file_name):
    return pre_path + file_name


def get_user_words(file_name):
    user_words = set([])
    with open(file_name, 'r') as src:
        for line in src:
            tmp_line = line.strip().decode('utf-8')
            if not tmp_line:
                continue
            user_words.add(tmp_line)
    return user_words
