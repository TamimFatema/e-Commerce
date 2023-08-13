
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls'))




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
