from django.shortcuts import render

# Create your views here.

def topic(request):
    return render(request, 'mooc/topic.html',context={'topic_id':1})