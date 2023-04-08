from django.urls import path
from app import views

urlpatterns = [
    path('',views.index.as_view()),
    path('table/',views.table.as_view()),
    path('delete/<int:pk>/',views.delete.as_view()),
    path('update/<int:pk>/',views.update.as_view(),name='edit'),
]