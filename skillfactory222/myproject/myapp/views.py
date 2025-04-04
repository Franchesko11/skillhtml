from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def repeat_content(request):
    context = {'flatpage_content': 'Повторяющий текст'}
    return render(request, 'repeat.html', context)

@login_required
def admin_only(request):
    return render(request, 'admin_only.html')