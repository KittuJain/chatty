import sys
import logging
import random
import nltk
import json
from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC

from .sentence_parser import SentenceParser
from utils.file import File
from utils.utils import *
from utils.path import *

sys.path.append(module_path)


# BEFORE DEPLOYING TRAIN ON ALL DATA
class Glados(object):
    def __init__(self, data_filename):
        self.logger = logging.getLogger("Glados")
        self.file = File()
        self.parser = SentenceParser()
        self.data_filename = data_filename
        self.classifier = self.train_and_get_classifier(self.data_filename)

    """
    Public api
    input: user question text
    output: answer
    """

    def get_help(self, question):
        features = self.parser.extract_feature(question)
        print('features', features)
        answer = self.classifier.classify(features)
        prob = self.classifier.prob_classify(features).prob(answer)
        # self.logger.info('features for question are %s', features)
        print('Answer:', answer, "(", prob, ")")
        response = dict(question=question, answer=answer, probability=prob)
        return response

    def train_and_get_classifier(self, data_filename):
        split_ratio = 0.8
        data = self.parser.get_content(data_filename)
        data_set = self.parser.extract_feature_from_doc(data)
        random.shuffle(data_set)
        data_length = len(data)
        train_split = int(data_length * split_ratio)
        training_data = data_set[:train_split]

        self.error_analysis_for_text_input_to_feature_extraction(data)
        self.error_analysis_for_features_to_predicted_answer(training_data)

        test_data = data_set[train_split:]

        # self.logger.debug('\n'.join([str(x) for x in data_set]))

        classifier, classifier_name, test_set_accuracy, training_set_accuracy = self.train_using_naive_bayes(
            training_data, test_data)
        self.file.append(get_module_path("output/accuracy.txt"), "\n%s\t\t%s\t\t\t%.8f\t\t%.8f" % (
            classifier_name, data_length, training_set_accuracy, test_set_accuracy))
        return classifier

    def error_analysis_for_text_input_to_feature_extraction(self, data):
        text_features_answer = []
        for (text, category, answer) in data:
            sent_features = self.parser.extract_feature(text)
            text_features_answer.append((text, sent_features, answer))
            # logging.debug(datetime.datetime.now())
        # print('>>>>>>>>TEXT>>>>>>>>>FEATURES>>>>>>ANSWER:\n ', str(json.dumps(text_features_answer)))

    def error_analysis_for_features_to_predicted_answer(self, test_data):

        classifier = nltk.NaiveBayesClassifier.train(test_data)
        classifier.show_most_informative_features()
        errors = []
        for (feature, actual_output) in test_data:
            guess = classifier.classify(feature)
            if (guess != actual_output):
                errors.append((feature, actual_output, guess))
        print('>>>>>FEATURE>>>>>>>>>ACUTUAL OUTPUT><<<<<<<<PREDICTION<<<<<<<<<<<<<<<')
        print('Errors:', json.dumps(errors))

    def train_using_naive_bayes(self, training_data, test_data):
        classifier = nltk.NaiveBayesClassifier.train(training_data)
        classifier_name = type(classifier).__name__
        training_set_accuracy = nltk.classify.accuracy(classifier, training_data)
        test_set_accuracy = nltk.classify.accuracy(classifier, test_data)
        return classifier, classifier_name, test_set_accuracy, training_set_accuracy

