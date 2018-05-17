#!usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv

from AQ_luozhen.util import get_file_name
from AQ_luozhen.sentence.split_handle import Split_Handle


class Split_Word(object):
    def __init__(self, obj_file, dest_file, stop_file="../data/stop_words.txt", user_dict_file="../data/user_dict", is_qa=False):
        self.obj_file = obj_file
        self.dest_file = dest_file
        self.is_qa = is_qa
        self.jieba_handle = Split_Handle(stop_file, user_dict_file)

    def split_file_line(self, line):
        if self.is_qa:
            space_index = line.find(' ')
            q = line[: space_index]
            a = line[space_index + 1:]
            q_split = self.jieba_handle.split_words(q)
            a_split = self.jieba_handle.split_words(a)
        else:
            q_split = self.jieba_handle.split_words(line)
            a_split = None
        return q_split, a_split

    def split_word(self):
        with open(self.dest_file, 'wa') as dest_src:
            csv_writer = csv.writer(dest_src, delimiter=' ')
            with open(self.obj_file, 'r') as obj_src:
                for line in obj_src:
                    q_split, a_split = self.split_file_line(line)
                    if a_split:
                        csv_writer.writerow(q_split + [":"] + a_split)
                    else:
                        csv_writer.writerow(q_split)


if __name__ == "__main__":
    pre_path = "data/"
    raw_data_file = "tnb.txt"
    split_file = "split.txt"
    stop_words_file = "stop_words.txt"
    dict_file = "user_dict"

    obj_file = get_file_name(pre_path, raw_data_file)
    dest_file = get_file_name(pre_path, "qa_split.txt")
    split_obj = Split_Word(obj_file, dest_file, get_file_name(pre_path, stop_words_file), get_file_name(pre_path, dict_file), True)
    split_obj.split_word()