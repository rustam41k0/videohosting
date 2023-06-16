from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from authapp.models import User
from mainapp.models import Video, Comment


def index(request):
    context = {
        'videos': Video.objects.all().order_by("-id")
    }
    return render(request, 'main.html', context)


class VideoView(View):
    def get(self, request, pk):
        video = Video.objects.get(id=pk)
        user = request.user
        if user.is_authenticated and user not in video.viewed.all():
            video.viewed.add(user)
        context = {
            'user': [User],
            'usernames': ['kar', 'unclear legacy', 'lender', 'cyreh', 'cyreh', 'cyreh', 'cyreh', 'cyreh'],
            'video': video,
            'comments': Comment.objects.filter(video=video).order_by("-id"),
            'like': request.user in video.likes.all(),
            'dislike': request.user in video.dislikes.all()
        }
        return render(request, 'view.html', context)


class AddComment(VideoView):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.username = request.user
            form.video_id = pk
            form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/login')
def upload(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = Video(username=request.user,
                          title=request.POST.get('title'),
                          description=request.POST.get('description'),
                          image=request.FILES['image'],
                          file=request.FILES['video']
                          )

            video.save()
            # messages.success(request, 'Вы успешно загрузили видео')
            return HttpResponseRedirect('/')
    else:
        form = UploadVideoForm()
    context = {'form': form}
    return render(request, 'upload.html', context)


@login_required(login_url='/users/login')
def like(request, pk):
    video = Video.objects.get(id=pk)
    if request.user in video.likes.all():
        video.likes.remove(request.user)
    else:
        video.likes.add(request.user)
        if request.user in video.dislikes.all():
            video.dislikes.remove(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/login')
def dislike(request, pk):
    video = Video.objects.get(id=pk)
    if request.user in video.dislikes.all():
        video.dislikes.remove(request.user)
    else:
        video.dislikes.add(request.user)
        if request.user in video.likes.all():
            video.likes.remove(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
