import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pickle

# Load data CSV
data = pd.read_csv('resep/resepfinal834.csv')


# Ambil kolom bahan masakan
bahan_masakan = data['Ingredients Cleaned']

# TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(bahan_masakan)

# KNN Model
knn_model = NearestNeighbors(n_neighbors=5, metric='cosine')
knn_model.fit(tfidf_matrix)

# Simpan model dan vectorizer ke dalam file pickle
with open('knn_model.pkl', 'wb') as model_file:
    pickle.dump(knn_model, model_file)

with open('tfidf_vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(tfidf_vectorizer, vectorizer_file)

print("Model dan vectorizer berhasil disimpan!")
