from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

#Views from apps
from UserPanel import views as userpanel

urlpatterns = [
	path('', userpanel.user_panel, name="userpanel"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', userpanel.register_user, name="register"),
    path('confirm_registration', userpanel.confirm_registration, name="confirm_registration"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
