from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeView(request) -> HttpResponse:
    if request.method == 'POST':
        Question = request.POST.get('user_input')
        
        # Do something with the input, e.g., process it, save it, etc.
        # For demonstration, you can print it or send it back as a response
        print(f"User Input: {Question}")
        
        # You can render the same page with some context or redirect to another view
        return HttpResponse(f"You entered: {Question}")

    return render(request,"index.html")