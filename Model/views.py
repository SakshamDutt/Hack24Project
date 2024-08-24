from django.shortcuts import render
from django.http import HttpResponse
from Core.LLMChat import generate_response
from threading import Thread
from dataclasses import dataclass

# Create your views here.
def homeView(request) -> HttpResponse:
    Question = None
    Answer = None
    if request.method == 'POST':
        Question = request.POST.get('user_input')
        Answer = generate_response(Question)
    return render(request,"index.html", {'question':Question,'answer':Answer})