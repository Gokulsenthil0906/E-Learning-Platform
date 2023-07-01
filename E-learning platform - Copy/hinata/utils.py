from django.db import connection
import random
import nltk
import numpy as np
import base64
from io import BytesIO
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout


nltk.download('omw-1.4')

# downloading model to tokenize message
nltk.download('punkt')
# downloading stopwords
nltk.download('stopwords')
# downloading wordnet, which contains all lemmas of english language
nltk.download('wordnet')

from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

from nltk.stem import WordNetLemmatizer


def clean_corpus(corpus):
    # lowering every word in text
    corpus = [doc.lower() for doc in corpus]
    cleaned_corpus = []

    stop_words = stopwords.words('english')
    wordnet_lemmatizer = WordNetLemmatizer()

    # iterating over every text[a,b,c]='a b c'
    for doc in corpus:
        # tokenizing text
        tokens = word_tokenize(doc)
        cleaned_sentence = []
        for token in tokens:
            # removing stopwords, and punctuation
            if token not in stop_words and token.isalpha():
                # applying lemmatization
                cleaned_sentence.append(wordnet_lemmatizer.lemmatize(token))
        cleaned_corpus.append(' '.join(cleaned_sentence))
    return cleaned_corpus

import json
with open(r'D:\pyquiz\subjects\jurish.json','r') as file:
    intents = json.load(file)


corpus = []
tags = []

for intent in intents['intents']:
    # taking all patterns in intents to train a neural network
    for pattern in intent['patterns']:
        corpus.append(pattern)
        tags.append(intent['tag'])

cleaned_corpus = clean_corpus(corpus)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_corpus)

from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()
y = encoder.fit_transform(np.array(tags).reshape(-1,1))



model = Sequential([
                    Dense(128, input_shape=(X.shape[1],), activation='relu'),
                    Dropout(0.2),
                    Dense(64, activation='relu'),
                    Dropout(0.2),
                    Dense(y.shape[1], activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

history = model.fit(X.toarray(), y.toarray(), epochs=20, batch_size=1)

# if prediction for every tag is low, then we want to classify that message as noanswer

INTENT_NOT_FOUND_THRESHOLD = 0.40


def predict_intent_tag(message):
    message = clean_corpus([message])
    X_test = vectorizer.transform(message)
    # print(message)
    # print(X_test.toarray())
    y = model.predict(X_test.toarray())
    # print (y)
    # if probability of all intent is low, classify it as noanswer
    if y.max() < INTENT_NOT_FOUND_THRESHOLD:
        return 'noanswer'

    prediction = np.zeros_like(y[0])
    prediction[y.argmax()] = 1
    tag = encoder.inverse_transform([prediction])[0][0]
    return tag


def get_intent(tag):
  for intent in intents['intents']:
    if intent['tag'] == tag:
      return intent


def chat_g(x):
    # get message from user
    message = x
    # predict intent tag using trained neural network
    tag = predict_intent_tag(message)
    # get complete intent from intent tag
    intent = get_intent(tag)
    # generate random response from intent
    response = random.choice(intent['responses'])
    with connection.cursor() as cursor:
        cursor.execute("UPDATE subjects_chat SET message = %s WHERE id = 1 ", [response])
        cursor.fetchone()
