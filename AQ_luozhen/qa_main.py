#!usr/bin/env python
# coding:utf-8

import logging
logging.basicConfig(filename='log/logger.log', level=logging.INFO)

from retriever.retriever import Retriever


def get_docs(question):

    pass


def retrieve_candidate_docs(question_str):
    retriever_obj = Retriever(question_str)
    docs = retriever_obj.get_candidate_docs()
    return docs


def reader_module(retrieve_res):
    pass


def qa_pipeline(question_str):
    # qa pipeline is a pipeline to get answer for given question
    retrieve_res = retrieve_candidate_docs(question_str)
    reader_res = reader_module(retrieve_res)
    print reader_res


if __name__ == "__main__":
    question_str = "糖尿病是什么？"
    qa_pipeline(question_str)
    # train_pipeline()
