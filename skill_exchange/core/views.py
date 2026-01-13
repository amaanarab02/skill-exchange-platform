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


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import ExchangeRequest

@login_required
def my_requests(request):
    received = ExchangeRequest.objects.filter(receiver=request.user)
    sent = ExchangeRequest.objects.filter(sender=request.user)
    return render(request, 'core/my_requests.html', {
        'received': received,
        'sent': sent
    })

@login_required
def update_request(request, req_id, action):
    req = get_object_or_404(ExchangeRequest, id=req_id, receiver=request.user)

    if action == 'accept':
        req.status = 'Accepted'
    elif action == 'reject':
        req.status = 'Rejected'

    req.save()
    return redirect('my_requests')

from .models import Message

@login_required
def chat(request, username):
    other = get_object_or_404(User, username=username)
    messages = Message.objects.filter(
        sender__in=[request.user, other],
        receiver__in=[request.user, other]
    ).order_by('timestamp')

    if request.method == 'POST':
        Message.objects.create(
            sender=request.user,
            receiver=other,
            text=request.POST['text']
        )
        return redirect('chat', username=other.username)

    return render(request, 'core/chat.html', {
        'messages': messages,
        'other': other
    })

