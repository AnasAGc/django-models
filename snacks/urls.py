from django.urls import path
from .views import SnackListView, SnackDetailView,DrinkslistView,DrinksDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', SnackListView.as_view(), name="snack_list"),
    path('<int:pk>/', SnackDetailView.as_view(), name="snack_detail"),
    path('drinks/',DrinkslistView.as_view(), name='drinklist'),
    path('drinks/<int:pk>',DrinksDetailView.as_view(), name='drinkDetail')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)