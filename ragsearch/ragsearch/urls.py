from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pipeline.urls')),  # ✅ This includes all pipeline routes
]
