from django.urls import path, include
import core.views as views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('contact/', views.contact, name='contact')
]
