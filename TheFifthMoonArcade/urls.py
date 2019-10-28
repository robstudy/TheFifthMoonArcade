from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

#Views from apps
from UserPanel import views as userpanel

urlpatterns = [
	path('', userpanel.user_panel, name="userpanel"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
