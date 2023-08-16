from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

# Create your views here.
def produto(request):
    # novo_produto = Produto(nome='Caio')
    # novo_produto.save()
    produto = Produto.objects.all()
    print(produto)
    return render(request, 'produto.html', {'produto': produto})
