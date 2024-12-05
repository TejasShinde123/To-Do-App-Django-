from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.signup),
    path('login/', views.login_view, name='login'),  # Make sure this matches the href in your HTML
    path('todopage/',views.todo),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo' ),
    path('delete_todo/<int:srno>', views.delete_todo),
    path('signout', views.signout, name='signout'),

]
