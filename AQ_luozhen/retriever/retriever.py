#!usr/bin/env
# coding:utf-8

import os
import jieba
from whoosh.scoring import TF_IDF, BM25F
from whoosh.index import create_in
from whoosh.fields import *
from jieba.analyse import ChineseAnalyzer
from AQ_luozhen.sentence import split_handle
from AQ_luozhen.raw_data_script import term_handle
import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')


class Retriever(object):
    weighting_dict = {'tfidf': TF_IDF, 'bm25': BM25F}

    def __init__(self, question_str, doc_path='../data/tnb.txt', user_dict_path="../data/user_dict", indexdir='../data/indexdir/', weighting='tf-idf'):
        self.doc_path = doc_path
        self.question_str = question_str
        self.user_dict_path = user_dict_path
        self.indexdir = indexdir
        self.weighting = self.__init_weighting(weighting)

    @staticmethod
    def __add_str(a, b):
        first_str = a.lower() if a.isalpha() or a.isdigit() else ''
        last_str = b.lower() if b.isalpha() or a.isdigit() else ''
        return first_str + last_str

    def __init_weighting(self, weighting_str):
        weighting_obj = reduce(self.__add_str, weighting_str)
        return self.weighting_dict[weighting_obj]

    def get_schema(self):
        # 使用结巴中文分词
        jieba.load_userdict(self.user_dict_path)
        analyzer = ChineseAnalyzer()

        # 创建schema, stored为True表示能够被检索
        schema = Schema(title=TEXT(stored=True, analyzer=analyzer), path=ID(stored=False),
                        content=TEXT(stored=True, analyzer=analyzer))

        # 存储schema信息至'indexdir'目录下
        # indexdir = '../data/indexdir/'
        if not os.path.exists(self.indexdir):
            os.mkdir(self.indexdir)
        ix = create_in(self.indexdir, schema)
        return ix

    def get_searcher(self):
        ix = self.get_schema()
        # 按照schema定义信息，增加需要建立索引的文档
        # 注意：字符串格式需要为unicode格式
        writer = ix.writer()
        file_tnb2 = open('../data/tnb2.txt', 'a')
        with open(self.doc_path) as src:
            count = 0
            for line in src:
                space_index = line.strip().find(' ')
                print space_index
                title = line[: space_index].strip()
                content = line[space_index + 1:].strip()
                file_tnb2.write(title + '\t' + content + '\n')
                print title
                print content, "\n"
                writer.add_document(title=unicode(title), path=unicode(content),
                                    content=unicode(content))
                count += 1
        writer.commit()

        # 创建一个检索器
        searcher = ix.searcher(weighting=self.weighting)
        return searcher

    def get_candidate_docs(self):
        searcher = self.get_searcher()
        # 检索标题中出现'文档'的文档
        question = self.question_str if isinstance(self.question_str, unicode) else unicode(self.question_str)
        results = searcher.find("title", question)
        # question_splited = self.jieba_obj.split_words(self.question_str)
        # print question_splited
        return results

# searcher = ix.searcher()
# # 检索出来的第一个结果，数据格式为dict{'title':.., 'content':...}
# firstdoc = results[0].fields()
#
# # python2中，需要使用json来打印包含unicode的dict内容
# jsondoc = json.dumps(firstdoc, ensure_ascii=False)
#
# print jsondoc  # 打印出检索出的文档全部内容

if __name__ == "__main__":
    retriever = Retriever('糖尿病')
    results = retriever.get_candidate_docs()
    for result in results:
        print result.highlights("title")  # 高亮标题中的检索词
        print result.score  # bm25分数
