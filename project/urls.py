from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('crud_cbv/', include('crud_cbv.urls')),
    path('crud_fbv/', include('crud_fbv.urls')),
]
