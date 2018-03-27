#!usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Classifier(object):
    def __init__(self, p_i, q):
        self.p_i = p_i
        self.q = q

    def get_probability(self):
        pass