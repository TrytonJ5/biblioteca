from rest_framework import generics
from .models import Livro,Autor,Categoria
from .serializers import LivroSerializer,AutorSerializer,CategoriaSerializer
from .filters import LivroFilter,AutorFilter,CategoriaFilter

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-list"
    search_fields = ("^name",)
    filterset_class = CategoriaFilter
    ordering_fields = (
        'name', 
    )

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detal"

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-list"
    search_fields = ("^name",)
    filterset_class = AutorFilter
    ordering_fields = (
        'name', 
    )

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    search_fields = ("^name",)
    filterset_class = LivroFilter
    ordering_fields = (
        'titulo', 
        'autor', 
        'categoria',
    )


class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"

    