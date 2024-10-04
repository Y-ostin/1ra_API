from django.shortcuts import get_object_or_404, render
from .models import Categoria, Producto
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializer import CategoriaSerializer, ProductoSerializer



# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.all()
    context = {
        'product_list': product_list,
        'categorias': categorias,  # Asegúrate de incluir las categorías en el contexto
    }
    return render(request, 'index.html', context)

def producto (request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias= Categoria.objects.all()
    return render(request, 'producto.html', {'producto': producto
                                             , 'categorias': categorias})


def listar_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'layout.html', {'categorias': categorias})
    


def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    context = {
        'productos': productos,
        'categoria': categoria,  
        'categorias': Categoria.objects.all(),  
    }
    return render(request, 'productos_por_categoria.html', context)


class CategoriaListView(APIView):   
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)


class ProductoListView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

class ProductoDetailView(APIView):
    def get(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

class ProductoCreateView(APIView):
    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
                        

class ProductoUpdateView(APIView):
    def put(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    
class ProductoDeleteView(APIView):
    def delete(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        producto.delete()
        return Response(status=204)