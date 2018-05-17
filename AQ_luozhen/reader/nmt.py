#!usr/bin/env python
# coding:utf-8

import mxnet as mx
from mxnet import autograd, gluon, nd
from mxnet.gluon import nn, rnn, Block
from mxnet.contrib import text

from io import open
import collections
import datetime


PAD = '<pad>'
BOS = '<bos>'
EOS = '<eos>'


epochs = 50
epoch_period = 10

learning_rate = 0.005
# 输入或输出序列的最大长度（含句末添加的EOS字符）。
max_seq_len = 5

encoder_num_layers = 1
decoder_num_layers = 2

encoder_drop_prob = 0.1
decoder_drop_prob = 0.1

encoder_hidden_dim = 256
decoder_hidden_dim = 256
alignment_dim = 25

ctx = mx.cpu(0)