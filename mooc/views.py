from django.shortcuts import render
from mooc.models import Topic
# Create your views here.

def topic(request):
    topic_id = 1
    topic = Topic.objects.filter(id=topic_id).first()
    if topic:
        topic_content = topic.content
    else:
        topic_content =None
    return render(request, 'mooc/topic.html',context={'topic_id':topic_id, 'content': topic_content})