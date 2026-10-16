
#### Lab 4, part 2. Naive Bayes for spam classification

#### Due Oct 27, 11:59pm

In this lab, we'll be using the bag-of-words approach to classifying words.
We'll use Naive Bayes to do the classification, and look at the way in which feature
selection affects learning.

Add a PDF including your answers to the repo. Please **do not** include the SpamAssassin corpus in 
the version you submit, though - we don't need lots of copies of the data.

To begin, download the SpamAssassin public corpus from here:

 https://spamassassin.apache.org/old/publiccorpus/

You want one version of spam, one version of easy ham, and one version of hard ham.
1. Unzip each of these files and look at some of the emails in each directory. What are some 
features that you notice that distinguish each category? 

 
2. nb.py contains a basic bag-of-words implementation for a Naive Bayes classifier. To begin,
take a look at train().
It takes as input a dictionary representing a training set, and produces a ConditionalFreqDist.

Create a ConditionalFreqDist in the Python interpreter and load in the spam and easy_ham
Take a look at the tokens that have been captured and their counts. What do you notice?

3. I've also provided a classify method for you. It takes as input a trained model and a list of
tokens, and computes the log-likelihood of each class. 

Try it out on a few emails. What does it seem to get right and wrong? 

There are two things to notice in classify:
a. This line:
```
              else:
                log_likelihood += (1 / model[c].N())
```
- What is going on here? What case are we accounting for? 

b. Naive Bayes multiplies conditional probabilities together to get an estimate. Here we are
instead adding the log of these values. Why is this? 

4. Train uses a set of filters and transforms to process the input. Filters remove tokens, and transforms
change them. I've provided two filters - alphabetic, which throws away words with non-alphabetic
characters, and stopword, which removes stopwords. I've also provided two transforms, trim and lowercase.

Based on what you've seen of the data so far, develop two filters and two transforms of your 
own. Feel free to stop using any of the provided ones if you don't like them. 

5. We have not set this up carefully as a learning problem. Our data is unbalanced, and we don't 
have training and test sets. Update the code in main to

      a) make sure that spam and ham have the same size training sets.
   
     b) Break the data into 80/20 training/test splits. You can either do this by hand or use sklearn.

Test your classifier out with the new configuration, and compute the accuracy. Look at the misclassified
examples. Do you notice anything helpful? Also look at the features for each class - does that tell you 
anything? 
