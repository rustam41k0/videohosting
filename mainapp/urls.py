from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import main_page, VideoView, upload, like, dislike

urlpatterns = [
    path('', main_page, name='home'),
    path('video/<int:pk>/', VideoView.as_view(), name='video'),
    path('upload/', upload, name='upload'),
    path('video/<int:pk>/like', like, name='like'),
    path('video/<int:pk>/dislike', dislike, name='dislike'),
    path('comment/<int:pk>/', VideoView.as_view(), name='add_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
