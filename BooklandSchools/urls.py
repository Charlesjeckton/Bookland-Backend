from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# =====================================================
# OPTIONAL: Simple API root for testing
# =====================================================
@api_view(["GET"])
def api_root(request):
    return Response({
        "message": "Welcome to Bookland Backend API!",
        "endpoints": {
            "admin": "/admin/",
            "app_urls": "/api/ (defined in booklandapp.urls)",
        }
    })


# =====================================================
# OPTIONAL: Simple root view for browser access
# =====================================================
def home(request):
    return JsonResponse({"message": "Bookland Backend is live!"})


# =====================================================
# URL PATTERNS
# =====================================================
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),  # Root URL
    path("api/", include("booklandapp.urls")),  # App API endpoints
    path("api-root/", api_root),  # Optional API test endpoint
]

# =====================================================
# MEDIA & STATIC FILES (DEVELOPMENT ONLY)
# =====================================================
if settings.DEBUG:
    # Serve media files (uploaded images) locally
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Serve static files locally
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
