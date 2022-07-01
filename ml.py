
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer


#Preprocess
def remove_hyperlinks_marks_styles(tweet):
    # remove old style retweet text "RT"
    new_tweet = re.sub(r'^RT[\s]+', '', tweet)

    # remove hyperlinks
    new_tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', new_tweet)

    # remove hashtags
    # only removing the hash # sign from the word
    new_tweet = re.sub(r'#', '', new_tweet)

    return new_tweet


# instantiate tokenizer class
tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                           reduce_len=True)


def tokenize_tweet(tweet):
    tweet_tokens = tokenizer.tokenize(tweet)

    return tweet_tokens


stemmer = PorterStemmer()


def get_stem(tweets_clean):
    tweets_stem = []

    for word in tweets_clean:
        stem_word = stemmer.stem(word)
        tweets_stem.append(stem_word)

    return tweets_stem


def process_tweet(tweet):
    processed_tweet = remove_hyperlinks_marks_styles(tweet)
    tweet_tokens = tokenize_tweet(processed_tweet)
    tweets_stem = get_stem(tweet_tokens)

    return tweets_stem

#Naive Bayes
import pickle
filename = 'logs.pkl'
with open(filename, 'rb') as f:
    loglikelihood = pickle.load(f)

logprior = 0.0

def naive_bayes_predict(tweet, logprior, loglikelihood):
    word_l = process_tweet(tweet)
    p = 0
    p += logprior

    for word in word_l:

        if word in loglikelihood:
          p+= loglikelihood[word]

    return p



def score(l):
    s=0.0
    for i in l:
        p = naive_bayes_predict(i, logprior, loglikelihood)
        s = s+p

    s=s/len(l)

    return s

l = ['I am good','Great Great Great']
print(score(l))