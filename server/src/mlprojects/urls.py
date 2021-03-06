
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('mnist/', include('mnist.urls')),
    path('embedding/', include('embedding.urls')),
    path('sentiment/', include('sentimentAnalysis.urls'))
]
