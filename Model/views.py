from django.shortcuts import render
from django.http import HttpResponse
from Core.LLMChat import generate_response, generate_notes_from_pdf
from threading import Thread
from dataclasses import dataclass
from django.core.files.storage import FileSystemStorage

Notes = ""
Title = ""

# Create your views here.
def homeView(request) -> HttpResponse:
    Question = None
    Answer = None
    global Title, Notes
    if request.method == 'POST' or request.FILES.get('file'):
        if request.FILES.get('file'):
            file = request.FILES['file']
            if file.content_type == 'application/pdf':
                fs = FileSystemStorage(location='Frontend/uploads/')
                filename = fs.save(file.name, file)
                global Notes 
                Notes = generate_notes_from_pdf(file.name)
                Title = file.name
            else:
                return HttpResponse("Only PDF files are allowed.")
        Question = request.POST.get('user_input')
        if Question not in ["None",None]:
            Answer = generate_response(Question, Notes)
        else:
            Question = None
    return render(request,"index.html", {'question':Question,'answer':Answer, 'title':Title, 'notes':Notes})