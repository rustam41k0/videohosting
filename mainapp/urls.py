from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from .views import main_page, VideoView, upload, like, dislike, AddComment

urlpatterns = [
    path('', main_page, name='home'),
    path('view/<int:pk>/', VideoView.as_view(), name='view'),
    path('upload/', upload, name='upload'),
    path('view/<int:pk>/like', like, name='like'),
    path('view/<int:pk>/dislike', dislike, name='dislike'),
    path('comment/<int:pk>/', AddComment.as_view(), name='add_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
