#!usr/bin/env
# coding:utf-8

from AQ_luozhen.sentence import split_handle
from AQ_luozhen.raw_data_script import term_handle
import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')


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



import os
import jieba
from whoosh.scoring import TF_IDF
from whoosh.index import create_in
from whoosh.fields import *
from jieba.analyse import ChineseAnalyzer
import json


# 使用结巴中文分词
jieba.load_userdict("../data/user_dict")
analyzer = ChineseAnalyzer()

# 创建schema, stored为True表示能够被检索
schema = Schema(title=TEXT(stored=True, analyzer=analyzer), path=ID(stored=False),
                content=TEXT(stored=True, analyzer=analyzer))

# 存储schema信息至'indexdir'目录下
indexdir = '../data/indexdir/'
if not os.path.exists(indexdir):
    os.mkdir(indexdir)
ix = create_in(indexdir, schema)

# 按照schema定义信息，增加需要建立索引的文档
# 注意：字符串格式需要为unicode格式
writer = ix.writer()
with open("../data/tnb.txt") as src:
    count = 0
    for line in src:
        space_index = line.strip().find(' ')
        # print space_index
        title = line[: space_index].strip()
        content = line[space_index + 1:].strip()
        # print title
        # print content, "\n"
        writer.add_document(title=unicode(title), path=unicode(content),
                            content=unicode(content))
        count += 1
writer.commit()

# 创建一个检索器
searcher = ix.searcher(weighting=TF_IDF)
# searcher = ix.searcher()


# 检索标题中出现'文档'的文档
results = searcher.find("title", u"糖尿病")

# # 检索出来的第一个结果，数据格式为dict{'title':.., 'content':...}
# firstdoc = results[0].fields()
#
# # python2中，需要使用json来打印包含unicode的dict内容
# jsondoc = json.dumps(firstdoc, ensure_ascii=False)
#
# print jsondoc  # 打印出检索出的文档全部内容
for result in results:
    print result.highlights("title")  # 高亮标题中的检索词
    print result.score  # bm25分数