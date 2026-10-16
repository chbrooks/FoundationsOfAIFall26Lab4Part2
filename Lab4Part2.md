
#### Lab 4, part 2. Naive Bayes for spam classification

#### Due Oct 27, 11:59pm

```
In this lab, we'll be using the bag-of-words approach to classifying words.
We'll use Naive Bayes to do the classification, and look at the way in which feature
selection affects learning.

```

## To begin, download the SpamAssassin public corpus from here:
## https://spamassassin.apache.org/old/publiccorpus/
## You want one version of spam, one version of easy ham, and one version of hard ham.
## 1. Unzip each of these files and look at some of the emails in each directory. What are some
## features that you notice that distinguish each category?


1. Download spam and ham. Look at them by
hand. What do you notice?

2. Run the basic trainer.

3. Run the classifier on a few examples. For cases that it gets
wrong, look at the data. What might be going on?

4. Extend the filters and transforms:
- add in strip and trim
- replace alpha with alnum
Are there custom filters you would suggest?

5. switch to embeddings.
step 2, step 3 (heatmap)

step 5, step 6, step 8.