from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Produk, Keranjang, Transaksi
from .serializers import ProdukSerializer, KeranjangSerializer, TransaksiSerializer

class ProdukAPI(APIView):
    def get(self, request):
        produk = Produk.objects.all()
        serializer = ProdukSerializer(produk, many=True)
        return Response(serializer.data)

class KeranjangAPI(APIView):
    def post(self, request):
        serializer = KeranjangSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransaksiAPI(APIView):
    def post(self, request):
        serializer = TransaksiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
from django.http import JsonResponse
from rest_framework.decorators import api_view
import pickle
import pandas as pd

# Load model dan vectorizer
with open('knn_model.pkl', 'rb') as model_file:
    knn = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    tfidf_vectorizer = pickle.load(vectorizer_file)

# Load dataset
data = pd.read_csv('resep/resepfinal834.csv')

# Fungsi untuk rekomendasi resep
def rekomendasi_resep(input_bahan, k=5):
    input_bahan_vec = tfidf_vectorizer.transform([input_bahan])
    distances, indices = knn.kneighbors(input_bahan_vec, n_neighbors=k)
    
    hasil_rekomendasi = []
    for i in range(len(indices[0])):
        idx = indices[0][i]
        hasil_rekomendasi.append({
            'Nama Resep': data.iloc[idx]['Title'],
            'Bahan': data.iloc[idx]['Ingredients'],
            'Langkah Pembuatan': data.iloc[idx]['Steps'],
            'Kesamaan': 1 - distances[0][i]
        })
    
    return hasil_rekomendasi

# API View untuk rekomendasi resep
@api_view(['GET'])
def rekomendasi_view(request):
    input_bahan = request.GET.get('bahan', '')  # mengambil input bahan dari query string
    if input_bahan:
        rekomendasi = rekomendasi_resep(input_bahan)
        return JsonResponse(rekomendasi, safe=False)
    return JsonResponse({'error': 'Bahan masakan tidak diberikan'}, status=400)
