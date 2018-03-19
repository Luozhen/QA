
from mxnet import nd
from numpy import np_random
import numpy as np
import random as rd
from mxnet import autograd
# from mxnet import autograd

num_inputs = 2
num_examples = 1000

true_w = [2, -3.4]
true_b = 4.2

X = nd.random_normal(shape=(num_examples, num_inputs))
y = true_w[0] * X[:, 0] + true_w[1] * X[:, 1] + true_b
y += .01 * nd.random_normal(shape=y.shape)

# 定义输入输出格式:
# 训练/测试数据输入数据:数据第一列为label, 其他列为特征列
num_examples = 1000
num_features = 2
true_w = [4.0, 2.5]
true_b = 1.0

class Data(object):
    def __init__(self, bucket_size=100, file_name=None, debug=True):
        self.file_name = file_name
        self.debug = debug
        self.bucket_size = bucket_size
        self.x = None
        self.y = None
        pass

    def get_imitate_train(self):
        self.x = np_random.rand(num_examples, num_features)
        self.y = np.dot(self.x, np.array(true_w).transpose()) + true_b

    def get_file_train(self):

        pass

    def get_bucket_data(self, iter_num):
        if self.debug:
            self.get_imitate_train()
            for index in range(iter_num):
                random_ls = rd.sample(xrange(num_examples), self.bucket_size)
                bucket_x = []
                bucket_y = []
                for i in random_ls:
                    bucket_x.append(self.x[i])
                    bucket_y.append(self.y[i])
                yield bucket_x, bucket_y
        else:

            pass

class LR_modle(object):
    def __init__(self, learn_rate, iter_num):
        self.train_data = None
        self.test_data = None
        self.learning_rate = learn_rate
        self.iter_num = iter_num


if __name__ == "__main__":
    learn_rate = 0.0001
    iter_num = 100

    pass