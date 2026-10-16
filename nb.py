## Naive Bayes using NLTK
import os

from nltk import FreqDist, ConditionalFreqDist
from nltk.corpus import stopwords
from math import log
from filters import *


## assume the training set is:
## a dictionary mapping category names to lists of files.
## e.g. t = {'spam' : ['spam/00012.381e4f512915109ba1e0853a7a8407b2', ...]
##           'easy_ham' : ['easy_ham/00011.fbcde1b4833bdbaaf0ced723edd6e355',  }
## Construct a ConditionalFrequencyDistribution that maps categories onto distributions.

## This should just work. You're welcome to adapt it if you'd like.
def train(training_set) :

    model = ConditionalFreqDist()
    for category in training_set :
        files = training_set[category]
        for name in files :
            print(name)
            try :
                word_list = apply_transforms(transforms,
                                         select_features(filters,
                                                         open(name).read().split(' ')))
            except :
                print("Unable to read " + name)
                continue
            for word in word_list :
                model[category][word] += 1
    return model


## classify
## Given a list of tokens and a model, return a dictionary mapping categories in the model
# to their log-likelihood.

def classify(model, list_of_tokens) :
    filtered_tokens = apply_transforms(transforms, select_features(filters, list_of_tokens))
    categories = list(model.keys())
    results = {}

    for c in categories:
        log_likelihood = 0
        for t in filtered_tokens:
            if t in model[c]:
                log_likelihood += (model[c][t] / model[c].N())
            else:
                log_likelihood += (1 / model[c].N())
        results[c] = log_likelihood
    return results


if __name__ == "__main__" :

    spam = ['./spam/' + item for item in os.listdir('./spam')]
    ham = ['./easy_ham/' + item for item in os.listdir('./easy_ham')]

    model = train(tset)

    for fileid in fileids :
        result = classify(model, movie_reviews.words(fileid))
        true_val = fileid[0:3]
        if result['pos'] > result['neg'] :
            predicted = 'pos'
        else :
            predicted = 'neg'
        print("%s %s" % (predicted, true_val))

