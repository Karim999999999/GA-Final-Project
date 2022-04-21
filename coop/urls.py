from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include("jwt_auth.urls")),
    path('coopcreate/', include("coopcreator.urls")),
    path('coopmanage/', include("coopmanager.urls")),
    path('ordermanage/', include("ordermanager.urls")),
]