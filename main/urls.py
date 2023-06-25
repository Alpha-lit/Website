from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('About', About_Page, name='about'),
    path('Services', ServicesView.as_view(), name="services"),
    path('contact', ContactView.as_view(), name="contact"),
    path('success/', ContactSuccessView.as_view(), name="success"),
    path('Terms', Terms_Page, name='terms'),
    path('Privacy', Privacy_Page, name='privacy'),
    path('details', Details_Page, name='details'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
]