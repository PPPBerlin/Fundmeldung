from django.urls import path
from . import views

urlpatterns = [
    path('fundmeldung/', views.fundmeldung, name='fundmeldung'),
    path('linksammlung/', views.linksammlung, name='linksammlung'),
    path('login/', views.loginSeite, name='login'),
    path('logout/', views.logoutBenutzer, name ="logout"),
    path('reg/', views.regBenutzer, name ="reg"),
    path('', views.start, name="start"),
]