# HighlightText
A tool that takes a set of text files as input and highlights each sentence (using HTML tags), such that the more two sentences are similar, the more their highlight colors are also similar.

The tokenize_text function uses NLTK's sent_tokenize to split the text into individual sentences. The calculate_similarity function calculates the similarity matrix using TF-IDF vectors and cosine similarity. The generate_highlighted_html function generates the HTML code with highlighted sentences based on their similarity scores. The get_random_color and get_color functions generate random colors and assign colors based on similarity percentages, respectively.
