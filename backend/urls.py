from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('authen/', include('djoser.urls.jwt')),
    # authen/jwt/create/? [name='jwt-create']
    # authen/jwt/refresh/? [name='jwt-refresh']
    # authen/jwt/verify/? [name='jwt-verify']
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	urlpatterns += [
		path('__debug__/', include(debug_toolbar.urls)),
	]