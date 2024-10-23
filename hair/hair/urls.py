from django.conf import settings
from django.contrib import admin
from django.urls import path
from posts.views import html_view, login_view, post_change_view
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/test', test_view),
    path('', html_view),
    path('login/', login_view),
    path('html/<int:post_id>/', post_change_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
