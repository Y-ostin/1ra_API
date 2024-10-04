from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoriaListView, ProductoListView, ProductoDetailView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView

app_name = 'tienda'
urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:producto_id>/', views.producto, name='producto'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),

    path('api/categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('api/productos/', ProductoListView.as_view(), name='producto-list'),
    path('api/productos/<int:producto_id>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('api/productos/create/', ProductoCreateView.as_view(), name='producto-create'),
    path('api/productos/<int:producto_id>/update/', ProductoUpdateView.as_view(), name='producto-update'),
    path('api/productos/<int:producto_id>/delete/', ProductoDeleteView.as_view(), name='producto-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)