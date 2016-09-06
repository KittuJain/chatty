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
            print('Features of Answer: ', (sent_features, answer))
            # print(datetime.datetime.now())
        return features

    def extract_feature(self, text):
        print("\nQUESTION: ", text)
        words = self.preprocess(text)
        print("After  Preprocess: ", words)
        # YOUR CODE HERE

        # Tag words
        tagged_words = [nltk.pos_tag(word_tokenize(words))]

        # Extract keys
        keys = self.extract_keys(tagged_words)

        # Stemming
        stemmed_words = [self.stemmer.stem(key) for key in keys]
        return self.get_feature_set(stemmed_words)

    def preprocess(self, sentence):
        # YOUR CODE HERE
        # make all lower case
        sentence = sentence.lower()

        #tokenize / segment the words & remove punctuations
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(sentence)

        # stop words
        set_of_stopwords = set(stopwords.words('english'))
        filtered_words = [word for word in tokens if not word in set_of_stopwords]

        # join the words
        return " ".join(filtered_words)

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
