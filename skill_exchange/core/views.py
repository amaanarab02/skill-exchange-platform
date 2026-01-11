from django.shortcuts import render,redirect

# Create your views here.
from .models import Skill
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('skill_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'core/skill_list.html', {'skills': skills})

@login_required
def add_skill(request):
    if request.method == 'POST':
        Skill.objects.create(
            user=request.user,
            name=request.POST['name'],
            level=request.POST['level'],
            description=request.POST['description']
        )
        return redirect('skill_list')
    return render(request, 'core/add_skill.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('skill_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

from .models import ExchangeRequest

@login_required
def send_request(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    ExchangeRequest.objects.create(
        sender=request.user,
        receiver=skill.user,
        skill=skill
    )
    return redirect('skill_list')

