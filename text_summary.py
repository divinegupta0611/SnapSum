import spacy
import heapq
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# text = """Machine Learning tutorial covers basic and advanced concepts, specially designed to cater to both students and experienced working professionals.
# This machine learning tutorial helps you gain a solid introduction to the fundamentals of machine learning and explore a wide range of techniques, including
# supervised, unsupervised, and reinforcement learning.Machine learning (ML) is a subdomain of artificial intelligence (AI) that focuses on developing systems that 
# learn—or improve performance—based on the data they ingest. Artificial intelligence is a broad word that refers to systems or machines that resemble human intelligence.
# Machine learning and AI are frequently discussed together, and the terms are occasionally used interchangeably, although they do not signify the same thing. A 
# crucial distinction is that, while all machine learning is AI, not all AI is machine learning. """

def summarizer(text):
    stopwords = list(STOP_WORDS)
    # print(stopwords)

    nlp = spacy.load('en_core_web_sm') #loading smallest module of spacy
    doc = nlp(text)     # text passes to nlp and stores in doc

    # print(doc)
    tokens = [token.text for token in doc] #create a list ,consists of each word present in doc
    # print(tokens)

    word_freq = {}      #create a dictionary(word : count)
    for word in doc:    #pick each word from doc ->convert it to text and lowercase
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1        #if word is already not in dict.
            else:
                word_freq[word.text] += 1       #if present then raise freq.

    # print(word_freq)

    max_freq = max(word_freq.values())  #return max freq.
    # print(max_freq)

    # cal.normalised freq. {freq of each word/max freq}

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

    # print(word_freq)

    #-------------------------------- creating sentence token list similar to words---------------------------------------------------------

    sent_tokens = [sent for sent in doc.sents] #list of sent.
    # print(sent_tokens)

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]    #sent_Score saves the normalise freq of each word in a sent and add it
                else:
                    sent_scores[sent] += word_freq[word.text]
            
    # print(sent_scores)        # print normalise freq of each sent

    select_len = int(len(sent_tokens)*0.3)      #using 30% len of sent tokens
    # print(select_len)

    summary = heapq.nlargest(select_len,sent_scores,key = sent_scores.get)#it'll pick those sent whose freq in sent_score is largest
    # print(summary)

    final_Summary = [word.text for word in summary] #creating list of words from summary
    summary = ' '.join(final_Summary)
    # print(summary)

    # print("Length of text :",len(text.split(' ')))
    # print("Length of summary :",len(summary.split(' ')))
    return summary,doc.text,len(doc.text.split(' ')),len(summary.split(' '))