from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from authapp.models import User
from mainapp.forms import CommentForm, UploadVideoForm
from mainapp.models import Video, Comment


@login_required(login_url='/auth/login')
def upload(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = Video(author=request.user,
                          title=request.POST.get('title'),
                          description=request.POST.get('description'),
                          preview=request.FILES['preview'],
                          file=request.FILES['video']
                          )

            video.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadVideoForm()
    return render(request, 'upload_video.html', {'form': form})


@login_required(login_url='/auth/login')
def main_page(request):
    return render(request, 'main.html', context={
        'videos': Video.objects.all().order_by("-id"),
        'user': request.user,
    })


class VideoView(View):
    def get(self, request, pk):
        video = Video.objects.get(id=pk)
        return render(request, 'video_page.html', context={
            'user': request.user,
            'comments': Comment.objects.filter(video=video).order_by("-id"),
            'video': video,
            'dislike': request.user in video.dislikes.all(),
            'like': request.user in video.likes.all(),
        })

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.video_id = pk
            form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/auth/login')
def like(request, pk):
    video = Video.objects.get(id=pk)
    if request.user in video.likes.all():
        video.likes.remove(request.user)
    else:
        video.likes.add(request.user)
        if request.user in video.dislikes.all():
            video.dislikes.remove(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/auth/login')
def dislike(request, pk):
    video = Video.objects.get(id=pk)
    if request.user in video.dislikes.all():
        video.dislikes.remove(request.user)
    else:
        video.dislikes.add(request.user)
        if request.user in video.likes.all():
            video.likes.remove(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
