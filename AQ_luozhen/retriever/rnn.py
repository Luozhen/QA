#!usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from math import exp
import mxnet as mx
from mxnet import nd
from mxnet import autograd
from mxnet import gluon

class RNN(object):
    def __init__(self, input_dim, hidden_dim, output_dim, std=0.01, context=mx.cpu()):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.std = std
        self.ctx = context
        self.params = None

    def get_params(self):
        # 输入门参数
        W_xi = nd.random_normal(scale=self.std, shape=(self.input_dim, self.hidden_dim), ctx=self.ctx)
        W_hi = nd.random_normal(scale=self.std, shape=(self.hidden_dim, self.hidden_dim), ctx=self.ctx)
        b_i = nd.zeros(self.hidden_dim, ctx=self.ctx)

        # 遗忘门参数
        W_xf = nd.random_normal(scale=self.std, shape=(self.input_dim, self.hidden_dim), ctx=self.ctx)
        W_hf = nd.random_normal(scale=self.std, shape=(self.hidden_dim, self.hidden_dim), ctx=self.ctx)
        b_f = nd.zeros(self.hidden_dim, ctx=self.ctx)

        # 输出门参数
        W_xo = nd.random_normal(scale=self.std, shape=(self.input_dim, self.hidden_dim), ctx=self.ctx)
        W_ho = nd.random_normal(scale=self.std, shape=(self.hidden_dim, self.hidden_dim), ctx=self.ctx)
        b_o = nd.zeros(self.hidden_dim, ctx=self.ctx)

        # 候选细胞参数
        W_xc = nd.random_normal(scale=self.std, shape=(self.input_dim, self.hidden_dim), ctx=self.ctx)
        W_hc = nd.random_normal(scale=self.std, shape=(self.hidden_dim, self.hidden_dim), ctx=self.ctx)
        b_c = nd.zeros(self.hidden_dim, ctx=self.ctx)

        # 输出层
        W_hy = nd.random_normal(scale=self.std, shape=(self.hidden_dim, self.output_dim), ctx=self.ctx)
        b_y = nd.zeros(self.output_dim, ctx=self.ctx)

        self.params = [W_xi, W_hi, b_i, W_xf, W_hf, b_f, W_xo, W_ho, b_o, W_xc, W_hc,
                  b_c, W_hy, b_y]
        for param in self.params:
            param.attach_grad()

    def lstm_rnn(self, inputs, state_h, state_c):
        # inputs: num_steps 个尺寸为 batch_size * vocab_size 矩阵
        # H: 尺寸为 batch_size * hidden_dim 矩阵
        # outputs: num_steps 个尺寸为 batch_size * vocab_size 矩阵
        [W_xi, W_hi, b_i, W_xf, W_hf, b_f, W_xo, W_ho, b_o, W_xc, W_hc, b_c,
         W_hy, b_y] = self.params

        H = state_h
        C = state_c
        outputs = []
        for X in inputs:
            I = nd.sigmoid(nd.dot(X, W_xi) + nd.dot(H, W_hi) + b_i)
            F = nd.sigmoid(nd.dot(X, W_xf) + nd.dot(H, W_hf) + b_f)
            O = nd.sigmoid(nd.dot(X, W_xo) + nd.dot(H, W_ho) + b_o)
            C_tilda = nd.tanh(nd.dot(X, W_xc) + nd.dot(H, W_hc) + b_c)
            C = F * C + I * C_tilda
            H = O * nd.tanh(C)
            Y = nd.dot(H, W_hy) + b_y
            outputs.append(Y)
        return (outputs, H, C)
