from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poll


# Create your views here.
def polls_list(requset):
    MAX_OBJECTS = 5
    polls = Poll.objects.all()[:5]
    data = {"result": list(polls.values("question_text", "created_by__username", "published_date"))}
    return JsonResponse(data)


def polls_details(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"result": {
        "question": poll.question_text,
        "created_by": poll.created_by.username,
        "pub_date": poll.published_date
    }}
    return JsonResponse(data)
