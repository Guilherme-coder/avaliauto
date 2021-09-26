from django.urls import path
from . import views

app_name = 'avaliauto'

urlpatterns = [
    path('cadastrar/', views.index, name='index'),
    path('consultorias/', views.show, name='show'),
    path('inserir', views.inserir, name='inserir'),
    path('aceitarConsultoria/<int:id>/', views.aceitarConsultoria, name='aceitarConsultoria'),
    path('', views.home, name='home'),
    path('minhasConsultorias/', views.minhas_consultorias, name='minhas_consultorias'),
]