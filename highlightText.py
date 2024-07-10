import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# Function to tokenize the text into sentences
def tokenize_text(text):
    return sent_tokenize(text)

# Function to calculate similarity between sentences
def calculate_similarity(sentences):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

# Function to generate HTML code with highlighted sentences
def generate_highlighted_html(text, similarity_matrix):
    sentences = tokenize_text(text)
    html = "<html><head><style>span { background-color: %s; }</style></head><body>" % get_random_color()

    for i, sentence in enumerate(sentences):
        similarity_scores = similarity_matrix[i]
        max_similarity = max(similarity_scores)
        similarity_percentage = int(max_similarity * 100)
        color = get_color(similarity_percentage)
        html += "<span style='background-color: %s;'>%s</span>" % (color, sentence)

    html += "</body></html>"
    return html

# Function to generate a random color
def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return '#%02x%02x%02x' % (r, g, b)

# Function to get color based on similarity percentage
def get_color(similarity_percentage):
    hue = int((similarity_percentage / 100) * 120)
    return 'hsl(%d, 100%%, 80%%)' % hue

# Example usage
text = "This is a sample text. It contains multiple sentences. Some sentences may be similar."
similarity_matrix = calculate_similarity(tokenize_text(text))
highlighted_html = generate_highlighted_html(text, similarity_matrix)
print(highlighted_html)