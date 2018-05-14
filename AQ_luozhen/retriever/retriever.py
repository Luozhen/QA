#!usr/bin/env
# coding:utf-8

from AQ_luozhen.sentence import split_handle
from AQ_luozhen.raw_data_script import term_handle


class Retriever(object):
    def __init__(self, question_str, model_path="../model/word2vec"):
        self.question_str = question_str
        self.jieba_obj = split_handle.Split_Handle()
        self.word2vec_obj = self.__get_word2vec_model(model_path)

    def __get_word2vec_model(self, model_path):
        return term_handle.Word2vec(model_path)

    def get_candidate_docs(self):
        question_splited = self.jieba_obj.split_words(self.question_str)
        print question_splited

        pass