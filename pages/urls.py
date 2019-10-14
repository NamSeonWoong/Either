from django.urls import path
from . import views

app_name='pages'

urlpatterns = [
    path('',views.index, name="index"),

    path('create/',views.create, name="create"),
    path('<int:id>/detail/',views.detail, name="detail"),
    path('<int:id>/update/',views.update, name="update"),
    path('<int:id>/delete/',views.delete, name="delete"),
    
    path('<int:question_id>/detail/<int:choice_id>/choice_delete/', views.choice_delete, name="choice_delete"),
    path('<int:question_id>/answer_create/', views.answer_create, name="answer_create"),
    path('show/',views.show, name="show")
]