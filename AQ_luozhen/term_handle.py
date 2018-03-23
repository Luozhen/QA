#!usr/bin/env python
# coding:utf-8

import os
import gensim


class TermHandle(object):
    def __init__(self, model_path, src):
        self.model_path = model_path
        self.src = src
        self.model = None
        pass

    def encode_sentence(self):
        pass

    def similary(self):
        pass

    def train_model(self):

        pass

    def get_model(self):
        if os.path.exists(self.model_path):
            self.model = gensim.models.Word2Vec.load('/tmp/mymodel')
        else:
            self.train_model()
        return self.model
