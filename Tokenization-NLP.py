#text processing: it help to remove or reduce noise and variability in text data.
#tokenisation: Divides text into individual words. Punctuation marks and spaces are often used as separators.
#structure help in sentiment analysis for instance in tweets.

import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer

text_sample = "My name is Gurpreet Purewal and I am from UK!"
text_sample1 = "this is a notebook and it is a #frame :-"
text_sample2 = "@gurpreet: This is an advertisement content!! :" 

# word tokenization:
    
x = word_tokenize(text_sample)
print(x)

tweet1 = word_tokenize(text_sample1) 
print(f'tokenized word1: {tweet1}')   

tweet2 = word_tokenize(text_sample2)
print(f'tokenized word2: {tweet2}')

#tweet tokenization 

tokenr = TweetTokenizer()                      

tweet1 = tokenr.tokenize(text_sample1)
print(f'tokenized tweet1: {tweet1}')

tweet2 = tokenr.tokenize(text_sample2)
print(f'tokenized tweet2: {tweet2}')


#case1: reduce length by removing repeated character


print('\nconfigurations case1: preserve_case=False, reduce_len=True')
t_k = TweetTokenizer(preserve_case=False, reduce_len=True)

tweet1 = tokenr.tokenize(text_sample1)
print(f'tokenized tweet1: {tweet1}')

tweet2 = tokenr.tokenize(text_sample2)
print(f'tokenized tweet2: {tweet2}')


#case2: reduce length and remove usernames


print('\nconfigurations case2: preserve_case=False, reduce_len=True, strip_handles=True')
t_k2 = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)    

tweet1 = t_k2.tokenize(text_sample1)
print(f'tokenized tweet1: {tweet1}')

tweet2 = t_k2.tokenize(text_sample2)
print(f'tokenized tweet2: {tweet2}')




