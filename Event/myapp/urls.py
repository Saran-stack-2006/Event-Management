from django.conf.urls.static import static
from django.conf import settings 
from . import views
from django.urls import path


urlpatterns = [
   
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-event/', views.add_event, name='add_event'),
    path('book/<int:id>/', views.book_event, name='book_event'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)