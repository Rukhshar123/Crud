from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('load_form',views.load_form,name="load_form"),
    path('add',views.add,name="add"),
    path('show',views.show,name="show"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]
