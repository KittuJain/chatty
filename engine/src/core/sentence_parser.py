import datetime
import nltk
import time
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import csv
from utils.file import File
from utils.path import *
import logging, sys

class SentenceParser:
    def __init__(self):
        self.file = File()
        self.stemmer = SnowballStemmer("english")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    def extract_feature_from_doc(self, line):
        features = []
        for (text, category, answer) in line:
            sent_features = self.extract_feature(text)
            # features.append((sent_features, category))
            features.append((sent_features, answer))
            # print(datetime.datetime.now())
            logging.debug('Features of Answer: ', (sent_features, answer))
            # print(datetime.datetime.now())
        return features

    def extract_feature(self, text):
        logging.debug("\nQUESTION: ", text)
        words = self.preprocess(text)
        logging.debug("After  Preprocess: ", words)
        # YOUR CODE HERE

        pass

    def preprocess(self, sentence):
        # YOUR CODE HERE

        pass

    def extract_keys(self, sentences):
        sent_keys = []
        for sent in sentences:
            keys = [x for (x, n) in sent if
                    n == 'NN' or n == 'NNS' or n == 'VBN' or n == 'VBP' or n == 'RB' or n == 'VBZ' or n == 'VBG' or n ==
                    'PRP' or n == 'JJ']
            if len(keys) == 0:
                keys = [x for (x, n) in sent]
            sent_keys.extend(keys)
        return sent_keys

    def get_feature_set(self, sent_keys):
        return {'keywords': ' '.join(sent_keys)}

    def get_content(self, fileName):
        with self.file.read(get_resource(fileName)) as content_file:
            lines = csv.reader(content_file, delimiter='|')
            res = [x for x in lines if len(x) == 3]
            return res
