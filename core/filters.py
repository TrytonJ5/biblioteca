from django_filters import rest_framework as filters
from .models import Livro,Autor,Categoria

class LivroFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='autor__nome',lookup_expr='icontains')
    categoria = filters.AllValuesFilter(field_name='categoria__nome')
    
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria']


class CategoriaFilter(filters.filterset):
    name = filters.AllValuesFilter(field_name= "name")

    class Meta:
        model = Categoria
        fields = [
            "name"
        ]

class AutorFilter(filters.filterset):
    name = filters.AllValuesFilter(field_name= "name")

    class Meta:
        model = Autor
        fields = [
            "name"
        ]