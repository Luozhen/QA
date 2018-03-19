#!usr/bin/env python
# coding:utf-8

import mxnet as mx
from mxnet import nd
from mxnet import ndarray

mx.random.seed(1)

print nd.empty((3, 4))
print ndarray([[1, 2, 3], [4, 5, 6]])