#!usr/bin/env python
# coding:utf-8

import os
import csv
import logging
import gensim


class Sentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        with open(self.dirname, 'r') as src:
            csv_reader = csv.reader(src, delimiter=' ')
            for line in csv_reader:
                yield line


class Term_Model(object):
    def __init__(self, model_path, src_file):
        self.model_path = model_path
        self.src_file = src_file
        self.model = None

    def get_model(self):
        return self.model


class Word2vec(Term_Model):
    def __init__(self, model_path, src_file):
        super(Word2vec, self).__init__(model_path, src_file)


class TF_IDF(Term_Model):
    def __init__(self, model_path, src_file):
        super(TF_IDF, self).__init__(model_path, src_file)


class TermHandle(object):
    def __init__(self, model_path):
        self.model_path = model_path
        # self.src = src
        self.model = None
        pass

    def encode_sentence(self):
        pass

    def similary(self):
        pass

    def get_sentences(self):
        split_file = ""
        with open(split_file, 'r') as src:
            csv_reader = csv.reader(src, delimiter=' ')
            for line in csv_reader:
                yield line

    def train_model(self):
        split_file = "../data/split.txt"
        my_sentences = Sentences(split_file)
        self.model = gensim.models.Word2Vec(my_sentences, window=5, iter=100, min_count=5, size=200)
        self.model.save(self.model_path)

    def get_model(self):
        # if 0 or os.path.exists(self.model_path):
        #     self.model = gensim.models.Word2Vec.load(self.model_path)
        # else:
        self.train_model()
        return self.model

    def get_vec(self, word):
        model = self.get_model()
        return model[word]

if __name__ == "__main__":
    # model_path = "../model/word2vec"
    # termHandle = TermHandle(model_path)
    # model = termHandle.get_model()
    # print "糖尿病 vec:", model['糖尿病']
    # similar_ls = model.wv.most_similar('糖尿病')
    # print "糖尿病 相近："
    # for ele in similar_ls:
    #     print ele[0], "score:", ele[1]
    file_name = "../data/tnb.txt"

    pass