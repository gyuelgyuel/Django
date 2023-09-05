from django.urls import path
from . import views


app_name = 'QnA'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:q_id>/', views.question, name='question'),
    path('<int:q_id>/<int:user_id>/<int:bool>/next_question/', views.next_question, name='next_question'),
    path('result/', views.result, name='result'),
]