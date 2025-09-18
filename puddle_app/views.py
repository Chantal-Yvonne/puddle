from django.shortcuts import render

# Create your views here.
"""Homepage view"""
def index(request):
    return render(request, 'puddle_app/index.html')

"""Contact view"""
def contact(request):
    return render(request, 'puddle_app/contact.html')