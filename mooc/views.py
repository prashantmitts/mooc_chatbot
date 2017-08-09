from django.shortcuts import render
from mooc.models import Topic

# Create your views here.


def home(request):
    print('home')
    return render(request, 'mooc/home.html')


def search(request):
    print('search')
    search_results = None
    if request.GET and request.GET.get('query'):
        search_results = Topic.objects.filter(
            title__icontains=request.GET.get('query'))
    return render(request, 'mooc/search_results.html', context={'results': search_results})


def topic(request):
    topic_id = request.GET.get('id')
    topic = Topic.objects.filter(id=topic_id).first()
    if topic:
        topic_content = topic.content
    else:
        topic_content =None
    video_d = str(topic.video)
    if video_d == 'video':
        video_d =None
    return render(request, 'mooc/topic.html', context={'topic_id': topic_id, 'topic': topic, 'content': topic_content, 'video': video_d})
