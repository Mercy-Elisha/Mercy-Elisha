# -- coding: utf-8 --
"""
Created on Mon Oct  7 10:02:26 2024

@author: Onsate
"""

import random

# Integer: Number of sentences to process
num_sentences = 6

# Float: Threshold probability to classify a sentence as positive or negative
positive_threshold = 0.7  # If sentiment score > 0.7, classify as positive

# Boolean: Whether to use pre-processing on the text (e.g., lowercasing, removing punctuation)
use_preprocessing = True

# Set: Track unique words in the dataset (to simulate building a vocabulary)
unique_words = set()

# Dictionary: Predefined sentiment scores for certain words
word_sentiment = {
    "great": 0.9,
    "good": 0.8,
    "okay": 0.6,
    "bad": 0.2,
    "terrible": 0.1
}


# Tuple: Predefined positive and negative words (for classification)
positive_words = ("great", "good", "amazing", "wonderful")
negative_words = ("bad", "terrible", "horrible")

# List: Sentences to classify (mock dataset)
sentences = [
    "The product is great and I love it.",
    "This service is terrible, I am very unhappy.",
    "It's a good day to be productive.",
    "I had an okay experience with this app.",
    "The weather is bad and ruined my plans.",
    "This day is terrible. I am broke"
]

# String: Log start of the sentiment analysis process
print(f"Starting sentiment analysis on {num_sentences} sentences...\n")

# Mock sentiment analysis loop
for i in range(num_sentences):
    sentence = sentences[i]
    
    # Boolean: Check if text preprocessing is enabled
    if use_preprocessing:
        sentence = sentence.lower()  # Example of preprocessing (convert to lowercase)

    # Tokenize the sentence into words (split by spaces)
    words = sentence.split()

    # Update the unique words set
    unique_words.update(words)

    # Float: Calculate a random "sentiment score" for the sentence
    sentiment_score = random.uniform(0.0, 1.0)  # Random score between 0 and 1

    # Classify based on sentiment score and the threshold
    if sentiment_score >= positive_threshold:
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    # String: Log the sentiment classification for each sentence
    print(f"Sentence {i+1}: '{sentence}'")
    print(f"Sentiment Score: {sentiment_score:.4f} -> Classified as {sentiment}\n")

# Dictionary: Log word counts from the unique words collected
word_counts = {word: sentence.count(word) for word in unique_words}

# Set: Display the unique words found in all sentences
print(f"Unique words found: {unique_words}\n")

# Log the completion of sentiment analysis
print("Sentiment analysis complete. Word frequencies from the dataset:")
for word, count in word_counts.items():
    print(f"'{word}': {count} occurrence(s)")