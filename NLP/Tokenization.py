import nltk
nltk.download()

paragraph="""Artificial Intelligence has revolutionized the way we interact with technology. From voice 
     assistants like Alexa and Siri to recommendation systems on Netflix and YouTube, AI is deeply integrated into
     our daily lives. One of the most important branches of AI is Natural Language Processing (NLP), which allows 
     machines to understand human language in both spoken and written forms. NLP uses several core techniques such
     as tokenization, stemming, lemmatization, and part-of-speech tagging to process text efficiently. Tokenization,
     in particular, is the first and most fundamental step in any NLP pipeline—it breaks a large piece of text into
     smaller units like words, phrases, or sentences. By dividing text into tokens, machines can analyze word 
     frequencies, relationships, and meanings more easily. For example, in sentiment analysis, tokenization helps
     separate the positive and negative words in a review so the system can understand the overall emotion behind 
     it. Similarly, in text summarization or chatbot systems, tokenization plays a vital role in organizing and
     structuring text before further processing. Without tokenization, it would be almost impossible for 
     computers to handle natural language effectively, as they would treat entire paragraphs as single strings 
     of characters instead of meaningful linguistic units."""

sentences=nltk.sent_tokenize(paragraph)
print(sentences)
words=nltk.word_tokenize(paragraph)
print(words)
