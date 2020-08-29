from django.shortcuts import render

# Create your views here.

def feedback(request):
    content = {}
    return render(request, 'write/feedback.html', content)