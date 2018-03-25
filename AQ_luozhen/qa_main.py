#!usr/bin/env python
# coding:utf-8

import os
import logging
logging.basicConfig(filename='log/logger.log', level=logging.INFO)
import term_handle

def get_docs(question):

    pass


def get_answer(retrieve_docs):
    pass


def qa_pipeline():
    # qa pipeline is a pipeline to get answer for given question
    question = raw_input('input the question:').strip().decode('utf-8')
    retrieve_docs = get_docs(question)
    answer = get_answer(retrieve_docs)
    print answer


def train_pipeline():
    # train pipeline is a pipeline to train model online for QA
    pass

if __name__ == "__main__":
    # qa_pipeline()
    train_pipeline()
