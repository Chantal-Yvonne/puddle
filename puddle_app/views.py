from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm

# Create your views here.
"""Homepage view"""
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'puddle_app/index.html', {
        'categories': categories,
        'items': items,
    })


"""Contact view"""
def contact(request):
    return render(request, 'puddle_app/contact.html')

"""Sign up form"""
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'puddle_app/signup.html', {
        'form': form
    })
