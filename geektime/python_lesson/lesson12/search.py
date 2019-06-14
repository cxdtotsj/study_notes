import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_1 = os.path.join(BASE_DIR, '1.txt')
path_2 = os.path.join(BASE_DIR, '2.txt')
path_3 = os.path.join(BASE_DIR, '3.txt')
path_4 = os.path.join(BASE_DIR, '4.txt')
path_5 = os.path.join(BASE_DIR, '5.txt')

class SearchEngieBase:
    def __init__(self):
        pass
    
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)
    
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')
    
    def search(self, query):
        raise Exception('search not implemented.')

def main(search_engine):
    for file_path in [path_1, path_2, path_3, path_4, path_5]:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print(f'found {len(results)} result(s):')
        for result in results:
            print(result)

class SimpleEngine(SearchEngieBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_text = {}
    
    def process_corpus(self, id, text):
        self.__id_to_text[id] = text
    
    def search(self, query):
        results = []
        for id, text in self.__id_to_text.items():
            if query in text:
                results.append(id)
        return results

class BOWEngine(SearchEngieBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True
    
    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词列表
        word_list = text.split(' ')
        # 去除空白符
        word_list = filter(None, word_list)
        # 返回单词列表
        return set(word_list)

class BOWInvertedIndexEngine(SearchEngieBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.inverted_index = {}
    
    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(id)
    
    def search(self, query):
        pass
    
    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词列表
        word_list = text.split(' ')
        # 去除空白符
        word_list = filter(None, word_list)
        # 返回单词列表
        return set(word_list)


if __name__ == '__main__':
    # search_engine = SimpleEngine()
    search_engine = BOWEngine()
    main(search_engine)